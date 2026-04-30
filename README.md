# 🍽️ Band Meeting Summarizer

Automatically reads meeting note photos posted in your Band group, summarizes them using Claude Vision AI, and lets you review/edit before posting the summary as a comment — all from your own account.

---

## How It Works

```
Band Post (image) → Playwright scrapes it → Claude Vision reads it
     → Summary draft saved → YOU approve/edit → Playwright posts comment
```

---

## Project Structure

```
band_summarizer/
├── band_watcher.py      ← Main watcher daemon (runs on schedule)
├── approve.py           ← CLI reviewer: approve, edit, post
├── inspect_band.py      ← Run this FIRST to find correct HTML selectors
├── requirements.txt
├── .env.example         ← Copy to .env and fill in your credentials
├── images/              ← Downloaded meeting note photos
├── drafts/              ← Saved summary text files
├── logs/                ← Watcher logs
└── data/
    └── band_summarizer.db  ← SQLite database (auto-created)
```

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. Configure your `.env`

```bash
cp .env.example .env
```

Edit `.env`:
```
BAND_EMAIL=your_email@example.com
BAND_PASSWORD=your_password
BAND_ID=XXXXXXX          # from band.us/band/XXXXXXX
ANTHROPIC_API_KEY=sk-ant-...
CHECK_INTERVAL_MINUTES=30
```

### 3. Find your Band group's HTML selectors (IMPORTANT)

Band's HTML structure varies by group. Run the inspector first:

```bash
python inspect_band.py
```

This opens a real browser, logs in, and tells you which CSS selectors exist in your group. Then update the selector lists in `band_watcher.py` → `fetch_posts_with_images()`.

---

## Usage

### Run the watcher (background daemon)

```bash
python band_watcher.py
```

This checks your Band group every 30 minutes (configurable). It:
- Detects new posts with images
- Downloads the image
- Sends it to Claude Vision
- Saves a draft summary
- Stores it as "pending" in the database

### Review and approve drafts

```bash
# See what's pending
python approve.py --list

# Review pending posts interactively
python approve.py

# Review AND post to Band in one step
python approve.py --post

# Post already-approved summaries
python approve.py --post-queued
```

During review you can:
- **[A]** Approve the summary as-is
- **[E]** Edit in your terminal text editor (nano, vim, etc.) before approving
- **[S]** Skip (leave as pending for later)
- **[X]** Discard permanently
- **[Q]** Quit the reviewer

---

## Running as a Background Service (Linux/Mac)

### Using screen (simple)

```bash
screen -S band-watcher
python band_watcher.py
# Ctrl+A, D to detach
```

### Using systemd (persistent across reboots)

Create `/etc/systemd/system/band-watcher.service`:

```ini
[Unit]
Description=Band Meeting Summarizer
After=network.target

[Service]
User=YOUR_USERNAME
WorkingDirectory=/path/to/band_summarizer
ExecStart=/usr/bin/python3 band_watcher.py
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable band-watcher
sudo systemctl start band-watcher
sudo systemctl status band-watcher
```

---

## Troubleshooting

### Scraper finds 0 posts
Run `inspect_band.py` and update the selectors in `band_watcher.py`.
Band occasionally changes their HTML class names.

### Login fails
Band may use Google/Kakao OAuth. If so, log in manually once in the browser
with `headless=False`, save cookies, and load them in the scraper:
```python
page.context.storage_state(path="auth.json")
# Then on next run:
context = browser.new_context(storage_state="auth.json")
```

### Comment posting doesn't work
Band's comment system is dynamic. You may need to:
1. Run `inspect_band.py` to screenshot the post page
2. Find the comment input selector manually
3. Update `post_comment()` in `band_watcher.py`

### Rate limiting
If Band blocks your account, increase `CHECK_INTERVAL_MINUTES` to 60+
and add longer `time.sleep()` delays in the scraper.

---

## Customizing the Summary Format

Edit the `prompt` string inside `summarize_meeting_image()` in `band_watcher.py`.

Example additions:
- "Always end with a motivational closing line for the team."
- "Note any upsell targets or featured items to push."
- "Include section headers in Spanish."

---

## Tech Stack

| Component | Tool |
|-----------|------|
| Browser automation | Playwright (Python) |
| AI vision + summarization | Claude Vision (Anthropic API) |
| Scheduling | `schedule` library |
| Storage | SQLite3 |
| Config | python-dotenv |
