# 🍽 WHAT TO EAT? – Smart CLI Meal Recommender

A Python command-line application that recommends recipes based on **available time**, **ingredients you have**, and **dietary restrictions** — powered by the [Spoonacular API](https://spoonacular.com/food-api/console#Dashboard).

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
   - Sign up at [Spoonacular](https://spoonacular.com/food-api/console#Dashboard)
   - Generate your API key

3. **Install dependencies**  
   Run:
   ```bash
   pip install -r requirements.txt

4. **Environment Variables**
   1. Change file name from `.env.example` to `.env`
   2. Replace `your_api_key_here` with your own Spoonacular API key

--- 

## 🚀 How to Use

1. **Clone this repository**
2. Run the script:

   ```bash
   python project.py

--- 

## 🛠 Tech Stack
- **Python** – Core language
- **Libraries:** Requests, python-dotenv, pytest
- **API:** Spoonacular API

---

## ⚠️ Notes

Free Spoonacular API tier has daily request limits — be mindful while testing.
