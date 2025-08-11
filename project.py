import requests
from dotenv import load_dotenv
import os

restrictions_list=["None","Vegetarian","Vegan","Gluten Free"]

load_dotenv()
API_KEY = os.getenv("SPOONACULAR_API_KEY")
url = "https://api.spoonacular.com/recipes/complexSearch"

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
    ingredientsCount=length(ingredients)
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


def length(ingredients):
    ingredients=ingredients.split(",")
    return len(ingredients)

def searchHeadingOutput():
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
        return restrictions_list[restriction]

if __name__ == "__main__":
    main() 