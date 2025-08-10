valid_mood=["happy","tired","adventurous"]
restrictions_list=["None","Vegetarian","Vegan","Gluten-free","Dairy-free","Nut-free"]

def main():
    print("🍽  WHAT TO EAT? - Smart CLI Meal Recommender")
    userInput()
    print("🔍 Searching recipes...")
    print("💡 Applying mood and ingredient filters...")
    print("⚡ Scoring recipes for best match...")

def userInput():
    # Mood
    while True:
        try:
            mood=input("How are you feeling? (happy/tired/adventurous)? → ").strip().lower()
            if mood not in valid_mood:
                raise ValueError
            break
        except:
            print("❌ Oops! Please enter one of: happy, tired, adventurous.")
    # Time needed
    while True:
        try:
            time=int(input("How much time do you have? (minutes) → ").strip())
            if time<=0:
                raise ValueError
            break
        except:
            print("❌ Oops! Please enter a valid number of minutes (positive whole number only)")
    # Budget 
    while True:
        try:
            budget=input("Budget level? (low/medium/high) → ").strip().lower()
            if budget not in ["low","medium","high"]:
                raise ValueError
            break
        except:
            print("❌ Oops! Please enter one of: low, medium, high.")
    # Ingredients
    while True:
        try:
            ingredients=input("Ingredients you have? (comma-separated, optional) → ")
            ingredients=ingredients.split(",")
            for i in range(len(ingredients)):
                ingredients[i]=ingredients[i].strip().lower()
            print(ingredients)
            break
        except EOFError:
            break
    # Restrictions
    while True:
        try: 
            print("Dietary Restrictions:")
            for i in range(len(restrictions_list)):   
                print(str(i)+". "+restrictions_list[i])
            restriction=int(input("Select your dietary restriction (or type 0 for none): ").strip())
            if restriction < 0 or restriction > 5:
                raise ValueError
            restriction=restrictions_list[restriction]
            break
        except:
            print("❌ Oops! Please enter one of: 0, 1, 2, 3, 4, 5.")


if __name__ == "__main__":
    main() 