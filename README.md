
# 🥗 7Nutrient : A Simple 7 Day Meal Planner

## Overview

The 7-Nutrient Meal Planner is a personalized meal planning application that leverages AI to generate a 7-day diet plan based on user inputs. The app focuses on catering to individual dietary preferences, fitness goals, and nutritional needs, making healthy eating both accessible and sustainable.




## 🌟Features
- Personalized Meal Plans: Tailored recommendations based on age, weight, activity level, and fitness goals.

- Dietary Preferences: Support for Vegetarian, Vegan, Non-Vegetarian, Gluten-Free, and more.

- Cuisine Selection: Choose from a variety of cuisines, such as Indian, Italian, Chinese, and Mexican.

- Interactive UI: User-friendly interface built with Streamlit.

## 💻Technologies Used
- Python: Core programming language.
- Streamlit: For building an interactive web app.
- Google Gemini API: For generating personalized diet plans.
- Environment Management: .env file for API key security.

## 🚀 Getting Started

### Environment Setup

1. **Create a Python Virtual Environment**

    ```bash
    # Using venv
    python -m venv venv
    ```

2. **Activate the Environment**

    - **On Windows**
    ```bash
    venv\Scripts\activate
    ```

    - **On Unix or macOS**
    ```bash
    source venv/bin/activate
    ```

3. **Install Dependencies**

    After activating the environment, install the required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    Create a `.env` file in the root directory of the project and add the necessary API keys:

    ```bash
    # API Keys
    GOOGLE_API_KEY=your_gemini_api_key
    ```

    Replace the placeholders (`your_gemini_api_key`) with your actual API keys.

5. **Running the Application**

    To run the application, use the following command:

    ```bash
    streamlit run main.py
    ```
## 📦 Dependencies

- `streamlit`
- `python-dotenv`
- `google-generativeai`

## ⚙️ Usage

### Input Details
Enter the following details in the sidebar:
- **Age**: Your age in years.
- **Weight**: Your weight in kilograms.
- **Dietary Preferences**: Select your food preference (e.g., Vegetarian, Non-Vegetarian, Vegan, etc.).
- **Activity Level**: Choose your activity level (e.g., Sedentary, Moderate, Active).
- **Fitness Goals**: Choose your fitness goal (e.g., Weight Loss, Muscle Gain, Maintenance).

### Generate Meal Plan
After entering the details, click the **"Submit"** button to generate a personalized 7-day meal plan based on your input. The meal plan will include:
- Three main meals (breakfast, lunch, and dinner).
- Two snacks per day.
- Nutritional insights and recommendations.

The meal plan is customized to match your dietary preferences and fitness goals.


## Acknowledgments

- [Google Generative AI](https://cloud.google.com/gen-ai) for providing the powerful AI services to generate personalized meal plans.
- [Streamlit](https://streamlit.io/) for offering an easy and interactive framework to build the web application.


## 🏛️ License

[MIT](https://choosealicense.com/licenses/mit/)

## 👨‍💻 Authors

## Made with ❤️ by  [Yash Gondaliya](https://www.github.com/YashGondaliya36)  



