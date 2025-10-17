# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
import snowflake.connector

from snowflake.snowpark.functions import col


cnx = snowflake.connector.connect(
    user=st.secrets["snowflake"]["pranavi"],
    password=st.secrets["snowflake"]["Chinna1818$12345678"],
    account=st.secrets["snowflake"]["YWJUAQJ-ZMB87297"],
    database=st.secrets["snowflake"]["SMOOTHIES"],
    schema=st.secrets["snowflake"]["PUBLIC"],
    warehouse=st.secrets["snowflake"]["COMPUTE_WH"]
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
