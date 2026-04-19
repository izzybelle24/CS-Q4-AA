username = "username"
password = "password"

print("Guardian Angel Login System")
print("1 - Sign Up")
print("2 - Login")

choice = int(input("Choose an option: "))

if choice == 1:
    username = input("Create username: ")
    password = input("Create password: ")
    print("Account created!")

elif choice == 2:
    login_user = input("Enter username: ")
    login_pass = input("Enter password: ")

    while login_user != username or login_pass != password:
        print("Incorrect username or password.")
        login_user = input("Enter username: ")
        login_pass = input("Enter password: ")

    print("Login successful!")

else:
    print("Invalid option.")


health_data = {}

health_data["Name"] = input("Enter your name: ")
health_data["Age"] = int(input("Enter your age: "))
health_data["Sex"] = input("Enter your sex: ")
health_data["Weight"] = float(input("Enter your weight (kg): "))
health_data["Height"] = float(input("Enter your height (cm): "))


fever_fatality = {
    "URL": ".gov",
    "Author": "Carlous (PhD)",
    "Citation": "Centers for Disease Control and Prevention",
    "Currency": "Last updated 2 months ago",
    "Miracle Cure": True
}


def Reliability_Verifier():

    URL_reliability = ""
    Author_reliability = ""
    Citation_reliability = ""
    Currency_reliability = ""
    MiracleCure_reliability = ""

    for key, reliability in fever_fatality.items():

        match key:

            case "URL":
                URL_reliability = "Reliable" if reliability == ".gov" else "Unreliable"

            case "Author":
                Author_reliability = "Reliable" if reliability == "Carlous (PhD)" else "Unreliable"

            case "Citation":
                Citation_reliability = "Reliable" if reliability == "Centers for Disease Control and Prevention" else "Unreliable"

            case "Currency":
                Currency_reliability = "Reliable" if reliability == "Last updated 2 months ago" else "Unreliable"

            case "Miracle Cure":
                MiracleCure_reliability = "Reliable" if reliability else "Unreliable"

    reliabilities = [
        URL_reliability,
        Author_reliability,
        Citation_reliability,
        Currency_reliability,
        MiracleCure_reliability
    ]

    reliable = reliabilities.count("Reliable")
    unreliable = reliabilities.count("Unreliable")

    if reliable > unreliable:
        print("Source evaluation: Accurate")
    else:
        print("Source evaluation: Inaccurate")


def Disease_significance_estimator():

    seriousness = 0
    temperature = 38.5

    if 37.8 <= temperature <= 38.0:
        seriousness += 1
    elif temperature <= 38.5:
        seriousness += 2
    else:
        seriousness += 3

    presence_of_convulsions = True
    seriousness += 1 if presence_of_convulsions else 2

    fever_duration = 3

    if fever_duration <= 3:
        seriousness += 1
    elif fever_duration <= 5:
        seriousness += 2
    else:
        seriousness += 3

    response_to_treatment = True

    if not response_to_treatment:
        seriousness += 1

    if seriousness <= 4:
        print("The fever is not too serious, it can be treated at home.")
    elif seriousness <= 7:
        print("The fever has unusual symptoms. Drink water and consider seeing a doctor.")
    else:
        print("Seek medical help immediately!")


def Disease_Determiner():

    print("Between Headache, coughs, high temperature, and hard to breathe.")

    HT = int(input("High temperature? Enter 1 if yes: "))
    HB = int(input("Hard to breathe? Enter 1 if yes: "))
    HA = int(input("Headaches? Enter 1 if yes: "))
    CC = int(input("Coughing? Enter 1 if yes: "))

    if HT == 1 and HB == 1 and HA == 1 and CC == 1:
        print("Possible Flu")

    elif HT == 1 and HA == 1:
        print("Possible Fever")

    elif CC == 1:
        print("Possible Common Cold")

    elif HB == 1:
        print("Possible Respiratory Infection")

    elif HA == 1:
        print("Possible Headache")


def Diet_Tracker():

    health_data2 = {'Daily_Steps': 0, 'Calories': 0, 'Water_Intake': 0}
    Workout = {}

    health_data2['Daily_Steps'] = int(input("Input Daily Steps: "))
    health_data2['Calories'] = int(input("Input Calories: "))
    health_data2['Water_Intake'] = int(input("Input Water Intake: "))

    Current = input("Have you done any exercises? Yes/No: ").title()

    while Current != "No":

        Exercise = input("Enter workout: ").title()
        BPM = int(input("Enter BPM for that workout: "))
        Workout[Exercise] = BPM

        Current = input("Would you like to continue? Enter No if not: ").title()

    print("Daily Health Data")
    for key, value in health_data2.items():
        print(f"{key}: {value}")

    if Workout:
        print("Workout Log")
        for key, value in Workout.items():
            print(f"{key}: {value} BPM")
    else:
        print("No workout indicated.")

    # --------- DIET PLAN ANALYZER ---------

    DietGFoods = {}
    DietNValues = {}

    print("""Enter the foods you've eaten this week.
First input the food name and type (Go Grow Glow),
then input Carbohydrates, Protein, and Fat values.""")

    while True:

        FName = input("Input food name: ")
        GType = input("Input if the food is Go Grow or Glow: ")
        Carbo = int(input("Input Carbohydrate values: "))
        Protein = int(input("Input Protein values: "))
        Fats = int(input("Input fat values: "))

        DietGFoods[FName] = GType
        DietNValues.setdefault(FName, []).append(Carbo)
        DietNValues[FName].append(Protein)
        DietNValues[FName].append(Fats)

        Addition = input("Add another food? Type Continue if yes: ").title()

        if Addition != "Continue":
            break

    WCarbo = 0
    WFats = 0
    WProteins = 0

    for key, value in DietNValues.items():
        WCarbo += value[0]
        WProteins += value[1]
        WFats += value[2]

    def Calculator():

        if WProteins > 1050 and WFats > 546 and 1575 > WCarbo:
            return "Eat less fats and proteins, and more carbohydrates"
        elif WFats > 546 and 350 > WProteins and WCarbo > 2275:
            return "Eat more protein, and less carbohydrates and fats."
        elif WProteins > 1050 and 308 > WFats and WCarbo > 2275:
            return "Eat more fat, and less carbohydrates and proteins."
        elif 308 > WFats and 350 > WProteins and WCarbo > 2275:
            return "Eat more fats and proteins, and less carbohydrates"
        elif 308 > WFats and 350 > WProteins and 1575 > WCarbo:
            return "Eat more protein, carbohydrates, and fats."
        elif WProteins > 1050 and WFats > 546 and WCarbo > 2275:
            return "Eat less protein, carbohydrates, and fats."
        elif 1575 > WCarbo:
            return "Increase carbohydrates."
        elif WCarbo > 2275:
            return "Lessen your carbohydrates."
        elif 308 > WFats:
            return "Eat more fats."
        elif WFats > 546:
            return "Eat less fats."
        elif 350 > WProteins:
            return "Increase your proteins"
        elif WProteins > 1050:
            return "Lessen your proteins."
        else:
            return "Healthy Current Diet!"

    print("Meals taken this week")
    for key, value in DietGFoods.items():
        print(f"Name: {key} || Type: {value}")

    print(f"Final Advisory: {Calculator()}")

def Health_Monitor():
        
    heart_rate = int(input("Enter current Heart Rate (BPM): "))
    blood_sugar = int(input("Enter Blood Sugar (mg/dL): "))
    print("1 - Fasting")
    print("2 - Post-Meal")
    meal_status = int(input("Select your status (1 or 2): "))
    temp = float(input("Enter Body Temperature (Celsius): "))
    
    print("""
~~~Blood Pressure Entry~~~""")
    systolic = int(input("Enter Systolic (Top number): "))
    diastolic = int(input("Enter Diastolic (Bottom number): "))

    print("""
~~~HEALTH MONITOR REPORT~~~""")

    if heart_rate > 100: #checks heart rate
        print("WARNING: High Heart Rate (Tachycardia)")
        print("Tip: Sit down, breathe slowly, and drink some cool water.")
    elif heart_rate < 60:
        print("WARNING: Low Heart Rate (Bradycardia)")
        print("Tip: If you feel dizzy, lie down and keep your legs elevated.")
    else:
        print("Heart Rate: Normal")

    if meal_status == 1: #checks blood sugar if fasting
        if blood_sugar > 125:
            print("WARNING: Elevated Blood Sugar")
            print("Tip: Limit sugar and focus on drinking more water.")
        elif blood_sugar < 70:
            print("WARNING: Low Blood Sugar.")
            print("Tip: Consume fast-acting carbs like fruit juice.")
        else:
            print("Blood Sugar: Normal (Fasting)")
     else:  # checks blood sugar if post-meal
        if blood_sugar > 180:
            print("WARNING: Elevated Blood Sugar.")
            print("Tip: Try a light walk to help process glucose.")
        elif blood_sugar < 70:
            print("WARNING: Low Blood Sugar.")
            print("Tip: Eat a small piece of fruit immediately.")
        else:
            print("Blood Sugar: Normal (Post-Meal)")
            
    if systolic >= 130 or diastolic >= 80: #checks blood pressure
        print("WARNING: Elevated Blood Pressure (Hypertension)")
        print("Tip: Avoid salty foods and caffeine. Try to relax.")
    elif systolic < 90 or diastolic < 60:
        print("WARNING: Low Blood Pressure (Hypotension)")
        print("Tip: Drink a glass of water and sit down slowly to avoid dizziness.")
    else:
        print("Blood Pressure: Normal")  

    if temp >= 38.0: #checks body temperature
        print("WARNING: Fever detected.")
        print("Tip: Rest and use a cold compress on your forehead.")
    elif temp < 35.0:
        print("WARNING: Low Body Temperature (Hypothermia)")
        print("Tip: Move to a warm area and wrap yourself in a blanket.")
    else:
        print("Temperature: Normal")


repeat = "Yes"

while repeat == "Yes":

    print("""
======== GUARDIAN ANGEL MENU ========

1 - Diet Tracker
2 - Disease Determiner
2.1 - Disease Significance Estimator
3 - Reliability Verifier
4 - Health Monitor
""")

    option = float(input("Select feature: "))

    if option == 1:
        Diet_Tracker()

    elif option == 2:
        Disease_Determiner()

    elif option == 2.1:
        Disease_significance_estimator()

    elif option == 3:
        Reliability_Verifier()

    else:
        Health_Monitor()

    repeat = input("Return to menu? Yes/No: ").title()
