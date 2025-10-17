# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
import snowflake.connector

from snowflake.snowpark.functions import col


cnx = snowflake.connector.connect(
    user=st.secrets["snowflake"]["user"],
    password=st.secrets["snowflake"]["password"],
    account=st.secrets["snowflake"]["account"],
    database=st.secrets["snowflake"]["database"],
    schema=st.secrets["snowflake"]["schema"],
    warehouse=st.secrets["snowflake"]["warehouse"]
)


cursor = cnx.cursor()
cursor.execute("SELECT CURRENT_VERSION()")
st.write(cursor.fetchone())

cnx=st.connection("snowflake")
session=cnx.session()

st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """
    Choose the Fruits you want in your Custom Smoothie!
    """
)


name_on_order =st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be ',name_on_order)


my_dataframe=session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#my_dataframe(data=my_dataframe,use_container_width=True)

ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:',my_dataframe
    ,max_selections=5
)
