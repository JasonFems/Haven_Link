
  import streamlit as st
  import pandas as pd
  import joblib

# 1. Load the robot's brain that was saved earlier
model = joblib.load('house_model_pkl')

# 2. Make the website look pretty
st.title('Nigeria House Price Robot')
st.write("Type in the house details below to see the estimated price!")

# 3. Create boxes for people to type in
bedrooms = st.number_input("How many bedrooms?", min_value=1, value=3)
bathrooms = st.number_input("How many bathrooms?", min_value=1, value=2)
toilets = st.number_input("How many toilets?", min_value=1, value=2)

# 4. The "Magic Button"
if st.button("Predict Price"):
  # Put the numbers into a tiny table for the robot
  clues = pd.DataFrame([[bedrooms, bathrooms, toilets]], columns=['bedrooms', 'bathrooms', 'toilets'])

  @ Ask the robot to guess
  prediction = model.predict(clues)

  @ Show thw answer in big green text
  st.success(f"The estimated price of this house is: ₦{float(prediction):,.2f}")
