import streamlit as st
from prompt import input_prompt
from genai_utils import gemini_response

# Function to generate the diet plan
def generate_diet_plan(prompt):

    # passing prompt to gemini
    return gemini_response(prompt)

#page config
st.set_page_config(page_title="7Nutrition",page_icon='🥗',layout='wide',)
# Streamlit App
st.title("7Nutrient 🥗 : 7 Day Nutrition Based Meal Planner")

# Sidebar inputs
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120, value=25)
weight = st.sidebar.number_input("Enter your weight (in kg):", min_value=1, max_value=200, value=70)
food_type = st.sidebar.multiselect("Select your dietary preference:", ["Vegetarian", "Non-Vegetarian", "Vegan", "Pescatarian", "Gluten-Free"])
activity_level = st.sidebar.selectbox("Select your activity level:", ["Sedentary", "Moderate", "Active"])
fitness_goals = st.sidebar.selectbox("Select your fitness goal:", ["Weight Loss", "Muscle Gain", "Maintenance"])
cuisine_preferences = st.sidebar.multiselect("Select your cuisine preferences:", ["Indian", "Italian", "Chinese", "Mexican", "Japanese"])

# Combine inputs into a prompt
user_prompt = input_prompt.format(
    age=age,
    weight=weight,
    food_type=food_type,
    activity_level=activity_level,
    fitness_goals=fitness_goals,
    cuisine_preferences=cuisine_preferences
)

# Button to generate the plan
if st.button("Generate Meal Plan"):
    with st.spinner("Genrating Meal Plan") :
        plan = generate_diet_plan(user_prompt)
        st.subheader("Your Personalized 7-Day Plan 🥗")
        st.write(plan)

