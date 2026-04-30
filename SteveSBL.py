#Creating a Science Based Lifter Object named Steve

class Steve(): 

    def __init__(self, name, strength=0, age=0, weight=0, height=0, sleep_hours=0, preworkout_carbs=0, caffine=0, warmed_up=False, hydrated=False, training_days=0, steps = 0, calories = 0, goal = "maintain", program = "None"):
        self.name = name
        self.strength = strength
        self.age = age
        self.weight = weight
        self.height = height
        self.sleep_hours = sleep_hours
        self.preworkout_carbs = preworkout_carbs
        self.caffine = caffine
        self.warmed_up = warmed_up
        self.hydrated = hydrated
        self.training_days = training_days
        self.steps = steps
        self.calories = calories
        self.goal = goal
        self.program = program

        self.current_lifts = {
            "Squat": 0,
            "Bench": 0,
            "Deadlift": 0,
            "OHP": 0,
            "Row": 0
            }

    def get_stats(self):
        stats = {
            "Name": self.name,
            "Weight": self.weight,
            "Age": self.age,
            "Height": self.height,
            "Strength": self.strength,
            "Sleep": self.sleep_hours,
            "Preworkout_carbs": self.preworkout_carbs,
            "Warmed Up": self.warmed_up,
            "Caffine": self.caffine,
            "Hydrated": self.hydrated,
            "Training Days": self.training_days
        }
        return stats
    def is_ready_to_train(self):
        if self.caffine > 0 and self.warmed_up and self.preworkout_carbs > 0 & self.hydrated:
            return True
        return False
    
    def check_missing(self):
        stats = self.get_stats()
        missing = []

        for stat in stats: 
            if stats[stat] == False or stats[stat] == 0:
                missing.append(stat)
        return missing
        
    def calculate_bmi(self):
        BMI_value = self.weight / self.height ** 2
        return BMI_value

    def calculate_bmr(self):
        bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        return bmr
    def calculate_tdee(self):
        bmr = self.calculate_bmr()

        if self.training_days <= 1:
            tdee = bmr * 1.2
        elif self.training_days <= 3:
            tdee = bmr * 1.375
        elif self.training_days <= 5:
            tdee = bmr * 1.55
        else:
            tdee = bmr * 1.725
        return round(tdee)
    
    def check_macros(self):
        protein_target = round(self.weight * 0.8)
        fat_target = round(self.weight * 0.3)

        protein_calories = protein_target * 4
        fat_calories = fat_target * 9

        remaining_calories = self.calories - protein_calories  - fat_calories
        carb_target = round(remaining_calories / 4)

        macros = {
            "Protein": protein_target,
            "Fats": fat_target,
            "Carbs": carb_target
        }
        return macros

    def check_recovery(self):
        recovery_issues = []

        if self.sleep_hours < 7:
            recovery_issues.append("Insufficient sleep — aim for 7-9 hours")

        if self.steps < 7500:
            recovery_issues.append("Low daily steps — aim for 7500-10000")
        elif self.steps > 50000: 
            recovery_issues.append("Very high step count — may impact recovery, but isn't significant")

        if self.calories < self.calculate_tdee() - 500: 
            recovery_issues.append("Calorie deficit too aggressive — risk of muscle loss")

        if len(recovery_issues) == 0:
            return "Recovery is optimal"
        else: 
            return recovery_issues
    
    def adjust_calories(self):
        tdee = self.calculate_tdee()

        if self.goal == "cut":
            adjusted = tdee - 500
            label = "Cut"
        elif self.goal == "bulk":
            adjusted = tdee + 250
            label = "Bulk"
        elif self.goal == "maintain":
            adjusted = tdee
            label = "Maintain"
        else:
            return "Invalid goal — choose cut, bulk, or maintain"
        self.calories = adjusted
        return f"Goal: {label} | TDEE: {tdee} | Target Calories: {adjusted}"
    
    def log_lift(self, lift, weight):        
        if lift in self.current_lifts:
            old_weight = self.current_lifts[lift]
            self.current_lifts[lift] = weight
            return f"{lift} updated: {old_weight}lbs -> {weight}lbs"
        else:
            self.current_lifts[lift] = weight 
            return f"{lift} added: {weight}lbs"
        
    def __str__(self):
        macros = self.check_macros()
        recovery = self.check_recovery()
        tdee = self.calculate_tdee()
        adjusted = self.adjust_calories()

        report = ""
        report += "=" * 50 + "\n"
        report += "         ATHLETE TRAINING REPORT\n"
        report += "=" * 50 + "\n"

        # Identity
        report += f"  Name:     {self.name}\n"
        report += f"  Age:      {self.age}\n"
        report += f"  Weight:   {self.weight}lbs\n"
        report += f"  Height:   {self.height}in\n"
        report += f"  Goal:     {self.goal.upper()}\n"
        report += "\n"

        # Training
        report += "--- TRAINING ---\n"
        report += f"  Program:       {self.program}\n"
        report += f"  Training Days: {self.training_days} days/week\n"
        report += "\n"

        # Current Lifts
        report += "--- CURRENT LIFTS ---\n"
        for lift in self.current_lifts:
            report += f"  {lift}: {self.current_lifts[lift]}lbs\n"
        report += "\n"

        # Nutrition
        report += "--- NUTRITION ---\n"
        report += f"  TDEE:     {tdee} calories\n"
        report += f"  Target:   {self.calories} calories\n"
        report += f"  Protein:  {macros['Protein']}g\n"
        report += f"  Fats:     {macros['Fats']}g\n"
        report += f"  Carbs:    {macros['Carbs']}g\n"
        report += "\n"

        # Recovery
        report += "--- RECOVERY ---\n"
        report += f"  Sleep:    {self.sleep_hours} hours\n"
        report += f"  Steps:    {self.steps}\n"
        if isinstance(recovery, list):
            for issue in recovery:
                report += f"  ⚠️  {issue}\n"
        else:
            report += f"  ✅ {recovery}\n"
        report += "\n"

        # Readiness
        report += "--- Workout READINESS ---\n"
        report += f"  {'✅' if self.preworkout_carbs > 0 else '❌'} Pre Workout Carbs\n"
        report += f"  {'✅' if self.hydrated else '❌'} Hydrated\n"
        report += f"  {'✅' if self.warmed_up else '❌'} Warmed Up\n"
        report += "\n"

        # Overall status
        if self.is_ready_to_train():
            report += "  🟢 READY TO TRAIN\n"
        else:
            report += "  🔴 NOT READY TO TRAIN\n"

        report += "=" * 50 + "\n"
        return report

if __name__ == "__main__":
    steve = Steve(
        name="Steve",
        age=25,
        weight=180,
        height=70,
        training_days=4,
        sleep_hours=8,
        preworkout_carbs=50,
        caffine=200,
        warmed_up=True,
        hydrated=True,
        steps=9000,
        goal="bulk",
        program="5/3/1"
    )
    steve.adjust_calories()

    # Log Steve's current lifts
# Interactively log lifts
    lifts = ["Squat", "Bench", "Deadlift", "OHP", "Row"]
    for lift in lifts:
        weight = int(input(f"Enter weight for {lift}: "))
        print(steve.log_lift(lift, weight))

    print()
    print(steve)
    print()
    print(steve)
