# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
st.title('My Parents New Healthy Diner')



st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """
    Choose the Fruits you want in your Custom Smoothie!
    """
)


name_on_order =st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be ',name_on_order)


