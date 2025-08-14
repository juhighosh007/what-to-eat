import requests
from dotenv import load_dotenv
import os
import sys

restrictions_list=["None","Vegetarian","Vegan","Gluten Free"]

load_dotenv()
API_KEY = os.getenv("SPOONACULAR_API_KEY")
url = "https://api.spoonacular.com/recipes/complexSearch"

if not API_KEY or API_KEY.strip().lower() == "your_api_key_here":
    print("❌ API key not found! Please set SPOONACULAR_API_KEY in your .env file.")
    print("👉 Create a .env file in the project root with the following format:")
    print("SPOONACULAR_API_KEY=your_api_key_here")
    input("\nPress Enter to exit...")
    sys.exit()

def main():
    print("🍽  WHAT TO EAT? - Smart CLI Meal Recommender")

    # Time req
    while True:
        try:
            time=int(input("How much time do you have? (minutes >= 15) → ").strip())
            time=validateTime(time)
            break
        except:
            print("❌ Oops! Please enter a valid number of minutes (please input a whole number greater than/equal to 15)")

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
            print("❌ Oops! Please enter one of: 0, 1, 2, 3.")

    searchHeadingOutput()
    data = getRecipe(ingredients, time, restriction)
    if data["results"]:
        displayRecipe(data)
    else:
        print("No tasty matches found this time... Try adding different ingredients or adjusting your filters!")
        input("\nPress Enter to exit...")
        sys.exit()

def displayRecipe(data):
    count=1
    ids=[]
    title=[]
    for i in data["results"]:
        ids.append(i["id"])
        title.append(i["title"])
        print(str(count) + ". " + i["title"])
        print("→ Time: " + str(i["readyInMinutes"]) + " mins")
        print("→ View recipe: " + i["sourceUrl"])
        print()
        count+=1
    displayInstructions(ids,title)

def displayInstructions(ids,title):
    while True:
        try:
            recipeNumber=int(input("Choose an option (1-3) → "))
            validateRecipeNumber(recipeNumber)
            break 
        except:
            print("❌ Oops! Please enter one of: 1, 2, 3.")
    print()

    idNumber=ids[recipeNumber-1]
    recipeName=title[recipeNumber-1]

    recipeUrl = f"https://api.spoonacular.com/recipes/{idNumber}/analyzedInstructions"

    params = {"apiKey": API_KEY}

    response = requests.get(recipeUrl,params=params)
    data=response.json()

    # Display 
    print("📜 "+ recipeName + " - Recipe Steps")
    for i in data[0]["steps"]:
        print(f"Step {i['number']}: {i['step']}")

    print()
    print("Bon Appétit 😋")


def validateRecipeNumber(recipeNumber):
    if recipeNumber not in [1,2,3]:
        raise ValueError

def getRecipe(ingredients, time, restriction):
    params = {
    "apiKey": API_KEY,
    "instructionsRequired": True,         # must have instructions
    "maxReadyTime": time,                 # minutes
    "addRecipeInformation": True,         # extra details like servings, summary
    "addRecipeInstructions": True,        # analyzed instructions
    "number":3                            # returns 3 meal ideas
}
    
    if ingredients and restriction:
        params["diet"]=restriction
        params["includeIngredients"]=ingredients
        
    elif restriction:
        # no ingredients
        params["diet"]=restriction
    elif ingredients:
        # no restriction
        params["includeIngredients"]=ingredients

    response = requests.get(url,params=params)
    return response.json()

def searchHeadingOutput():
    print()
    print("🔍 Searching recipes...")
    print("💡 Applying mood and ingredient filters...")
    print("⚡ Scoring recipes for best match...")
    print()
    print("Our suggestions:")
    print("──────────────────────────────────────────────────────────")
    print()

def validateIngredients(ingredients):
    ingredientsList=""
    if (ingredients):
        ingredients=ingredients.split(",")
        for i in range(len(ingredients)):
            ingredients[i]=ingredients[i].strip().lower()
        for i in ingredients:
            ingredientsList+=i+","
        return ingredientsList[:-1]
    else:
        return ""

def validateTime(time):
    if time<15:
        raise ValueError
    else:
        return time
    
def validateRestrictions(restriction):
    if restriction < 0 or restriction > 3:
        raise ValueError
    elif restriction==0:
        return ""
    else:
        return restrictions_list[restriction].lower()

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
    sys.exit()