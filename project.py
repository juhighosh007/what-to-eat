valid_mood=["happy","tired","adventurous"]
restrictions_list=["None","Vegetarian","Vegan","Gluten-free","Dairy-free","Nut-free"]

def main():
    print("🍽  WHAT TO EAT? - Smart CLI Meal Recommender")

    # Mood
    while True:
        try:
            mood=input("How are you feeling? (happy/tired/adventurous)? → ").strip().lower()
            mood=validateMood(mood)
            break
        except:
            print("❌ Oops! Please enter one of: happy, tired, adventurous.")

    # Time req
    while True:
        try:
            time=int(input("How much time do you have? (minutes) → ").strip())
            time=validateTime(time)
            break
        except:
            print("❌ Oops! Please enter a valid number of minutes (positive whole number only)")

    # Budget
    while True:
        try:
            budget=input("Budget level? (low/medium/high) → ").strip().lower()
            budget=validateBudget(budget)
            break
        except:
            print("❌ Oops! Please enter one of: low, medium, high.")

    # Ingredients
    ingredients=input("Ingredients you have? (comma-separated, optional) → ")
    ingredients=validateIngredients(ingredients)
    
    # Restrictions
    while True:
        try: 
            print("Dietary Restrictions:")
            for i in range(len(restrictions_list)):   
                print(str(i)+". "+restrictions_list[i])
            restriction=int(input("Select your dietary restriction (or type 0 for none) → ").strip())
            restriction=validateRestrictions(restriction)
            break
        except:
            print("❌ Oops! Please enter one of: 0, 1, 2, 3, 4, 5.")

    searchHeadingOutput()

def searchHeadingOutput():
    print("🔍 Searching recipes...")
    print("💡 Applying mood and ingredient filters...")
    print("⚡ Scoring recipes for best match...")
    print()
    print("Top 3 suggestions:")
    print("──────────────────────────────────────────────────────────")
    print()

def validateIngredients(ingredients):
    if (ingredients):
        ingredients=ingredients.split(",")
        for i in range(len(ingredients)):
            ingredients[i]=ingredients[i].strip().lower()
        return ingredients
    else:
        return []

def validateTime(time):
    if time<=0:
        raise ValueError
    else:
        return time
    
def validateRestrictions(restriction):
    if restriction < 0 or restriction > 5:
        raise ValueError
    else:
        return restrictions_list[restriction]

def validateBudget(budget):
    if budget not in ["low","medium","high"]:
        raise ValueError
    else:
        return budget
    
def validateMood(mood):
    if mood not in valid_mood:
        raise ValueError
    else:
        return mood

if __name__ == "__main__":
    main() 