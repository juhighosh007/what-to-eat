# 🍽 WHAT TO EAT? — Smart CLI Meal Recommender

Have you ever stood in front of your fridge trying to decide what to make with what you have? 

**WHAT TO EAT?** is a Python command-line application that helps you find a recipe quickly. It gives you meal suggestions based on what ingredients you have, time required to prepare it, and dietary restrictions. Bon Appétit!😋

Click [here](https://youtu.be/rnSELn1zy-g?si=qGWc-_azk5wgsUlu) to watch the demo video.

Created as the final project for Harvard’s CS50P (Introduction to Programming with Python). 

---

## ✨ Features
- ⏱ Filters recipes by your available cooking time.
- 🥗 Suggests recipes that match your dietary restrictions (**Vegetarian**, **Vegan**, **Gluten Free**, or none).
- 🧾 Lets you list the ingredients you already have to find matching recipes.
- 📜 Displays **step-by-step cooking instructions** for each recipe.
- 🌐 Provides direct links to the original recipe source.

---

## 📋 Prerequisites

Before you run the program, make sure you have:

1. **Python 3.7+** installed  
   [Download Python](https://www.python.org/downloads/)

2. **Spoonacular API Key**  
   - Sign up for free at [Spoonacular](https://spoonacular.com/food-api/console#Dashboard)
   - Generate your API key

3. **Install dependencies**  
   Run:
   ```bash
   pip install -r requirements.txt

4. **Environment Variables**
   1. Change file name from `.env.example` to `.env`
   2. Replace `your_api_key_here` with your own Spoonacular API key (without quotes)

--- 

## Usage
Use [python](https://www.python.org/) to run the application
```
$ python project.py
```
Use [pytest](https://docs.pytest.org/en/7.2.x/) to test the application
```
$ pytest test_project.py
```

--- 

## 🛠 Tech Stack
- **Python** – Core language
- **Libraries:** Requests, python-dotenv, pytest
- **API:** Spoonacular API

---

## ⚠️ Notes

Free Spoonacular API tier has daily request limits — be mindful while testing.
