import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
import joblib


#------------------Basic syntax code----------------------

# name = "Ekta"

# number = 16

#--------------------st.write() method-----------------------------

# st.write("Hello", name, "!")  
# st.write("Here's a random number: ", number)

#------------------st.button() method----------------------------------

# if st.button("Click me!"):   st.button() creates a button in app
#     st.write("You clicked the button!")

#---------------------st.checkbox() method-----------------------------------

# checked = st.checkbox("Check me!")    #st.checkbox creates a checkbox in app

# if checked:
#     st.write("You checked the checkbox!")

#--------------------------st.slider() method---------------------------

# age = st.slider("Select your age: ", 0, 100, 25)
# st.write("Your age is: ", age)

#-------------------------st.text_input method-----------------------------------

# name = st.text_input("Enter your name: ", value = "")
# st.write("Hello!", name)

#----------------------st.title() method---------------------------------

# st.title("Greeting Application.")
# name = st.text_input("Enter your name: ")
# age = st.slider("Select your age: ", 0, 100)

# if st.button("Submit"):
#     st.write(f"Hello {name}! You are {age} years old.")

#-------------------------Practice Task:---------------------------------------------

# Use what you have learned to create a simple app that asks for user input (name, age, favorite number) and dynamically displays the result.

# st.title("Greeting Application.")

# name = st.text_input("Enter your name: ")
# age = st.slider("Select your age: ",0, 100)
# favorite_number = st.text_input("Enter your favorite number: ")

# if st.button("Submit"):
#     st.write(f"Hello {name}! You are {age} years old. Your favorite number is {favorite_number}.")

# -------------------st.number_input() method--------------------------

# age = st.number_input("Enter your age: ", value = 20)

# st.write(f"You are {age} years old.")

# ------------------------Data frame concept in streamlit----------------------------

# data = {
#     "Name" : ["John", "Anna", "Peter", "Linda"],
#     "Age" : [28, 24, 35, 32],
#     "City" : ["New York", "Paris", "Berlin", "London"],
#     "Score": [95, 85, 90, 88]
# }

# df = pd.DataFrame(data)
# st.dataframe(df)  # It is interactive so it is scrollable and resizable on the app.
# st.table(df) # It is static so it is not scrollable and resizable on the app.

# #----------------------------------selectbox method in streamlit----------------------------

# city = st.selectbox("Choose a city to filter", df ["City"].unique())  #it returns the unique cities in the dataframe fro the above city element.
# filtered_data = df[df["City"] == city] #it filters the dataframe based on the selected city.

# st.write(f"Data for city: {city}")
# st.dataframe(filtered_data) #it displays the filtered data in a dataframe format.

# styled_df = df.style.applymap(lambda x: "background-color : yellow" if isinstance(x, int) and x > 90 else "")

# st.dataframe(styled_df)



# -------------------------------------Displaying JSON Data Structures using Dictionaries-------------------------------------------------
# Json_data = {
# "foo": "bar",
#         "stuff": [
#             "stuff 1",
#             "stuff 2",
#             "stuff 3",
#         ],
#         "level1": {"level2": {"level3": {"a": "b"}}},
# }

# st.json(Json_data) # Displays the JSON data in a readable format.

#--------------------------------------------Practice Task---------------------------------------------------------------

#Get an user input as number input and filter based on that number defaultly its going to be 80.

# number = st.number_input("Enter a number to filter scores: ", value = 80)
# Styled_df = df.style.applymap(lambda x: "background-color : yellow" if isinstance(x, int) and x > number else "")
# st.write(f"Data with scores greater than or equal to {number}:")
# st.dataframe(Styled_df)

#-------------------------------------Data Visulaization in Streamlit----------------------------------------------------

#---------- Line Chart in Streamlit---------------
# st.write("Data Visualization of random 100 points across 3 columns on Line Chart")

# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns = ["A", "B", "C"]
# )
# st.line_chart(data)

#---------------Bar Chart in Streamlit------------------

# st.write("Data Visualization of random 50 points across 3 columns on Bar Chart")
# data = pd.DataFrame(
#     np.random.randn(50, 3),
#     columns = ["A", "B", "C"]
# )
# st.area_chart(data)

#---------------------Plotly Bar Chart in streamlit----------------------

# st.write("Data Visualization of Fruit Sales on Bar Chart using Plotly")

# data = pd.DataFrame({
#     "Fruit": ["Apples", "Bananas", "Cherries", "Onions"],
#     "Amount": [10, 20, 30, 40],

# }

# )

# fig = px.bar(data, x = "Fruit", y = "Amount", title = "Fruit Sales")
# st.plotly_chart(fig)

#---------------------Matplotlib Bar Chart in streamlit----------------------
# st.write("Data Visualization of Random numbers on Scatter Chart using Matplotlib")
# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns = ["A", "B", "C"]

# )
# plt.figure(figsize = (10, 6))
# sns.scatterplot(x = data["A"], y = data["B"])
# plt.title("Scatter Plot of A and B")

# st.pyplot(plt)

# ---------------------Layout and Teaming in Streamlit----------------------

# In streamlit, we can create a layout for our app using columns to place fidgets and content side by side. 
# This helps in creating a more organized and responsive layouts.

#In this, we will be using only one library which is streamlit to create a layout of our app.

# st.title("Layout and Teaming in Streamlit")

# col1, col2, col3 = st.columns(3)
# with col1:
#     st.header("Column 1")
#     st.write("This is the First Column.")
#     if st.button("Button 1"):
#         st.write("You clicked Button 1 in Column 1!")


# with col2:
#     st.header("Column 2")
#     st.write("This is the Second Column.")
#     if st.button("Button 2"):
#         st.write("You clicked Button 2 in Column 2!")


# with col3:
#     st.header("Column 3")
#     st.write("This is the Third Column.")
#     if st.button("Button 3"):
#         st.write("You clicked Button 3 in Column 3!")

# -------------------------------Expander Widgets in Streamlit--------------------------------
# st.title("Expander widgets in Streamlit")

# with st.expander("See more details"):
#     st.write("Here are some additional details that can be toggled.")
#     st.line_chart([1, 2, 3, 4, 5])

# --------------------------------Sidebars for navigation in  streamlit--------------------------------

# st.title("Sidebars for Navigation in Streamlit")
# st.sidebar.title("Navigation")
# option = st.sidebar.selectbox("Choose a page", ["Home", "About", "Contact"])

# if option == "Home":
#     st.write("Welcome to the Home page!")
# elif option == "About":
#     st.write("This is the About page. Here you can find information about the app.")
# elif option == "Contact":
#     st.write("This is the Contact page. You can reach us at.")

# ---------------------------------Themes in Stremalit------------------------------------------------------


# st.set_page_config(page_title = "Themed App", page_icon = ":smiley:", layout = "wide", initial_sidebar_state = "expanded")
# st.title("Themed Streamlit App")
# st.write("This app has a customized theme!")

# -------------------------------------Machine Learning Model in Streamlit------------------------------------------------------

model = joblib.load("linear_regression_model.pkl")
st.title("Machine Learning Model Prediction App")
st.write("Enter the feature value to get the prediction.")

feature_value = st.number_input("Enter the value for feature: ", min_value = 0, max_value = 100, value = 2)

if st.button("Predict"):
    prediction = model.predict([[feature_value]]) [0] [0]
    st.write(f"The Predicted target value is: {prediction:.2f}.")