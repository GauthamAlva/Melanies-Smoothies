# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col



# Write directly to the app
st.title(f"Customize your Smoothie :cup_with_straw: {st.__version__}")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)






cnx=st.connection("snowflake")
name_on_order=st.text_input("Name on Smoothie","")
st.write("Name is",name_on_order)


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect("Choose up to 5 ingredients:",my_dataframe,max_selections=5)


if ingredients_list:
    st.write(ingredients_list)
    st.text(ingredients_list)

    ingredient_string=''
    for i in ingredients_list:
        ingredient_string+=i+' '
    st.write(ingredient_string)

    add_btn=st.button("Submit Order")

    my_insert_stmt = """ insert into smoothies.public.orders(name_on_order,ingredients)
            values ('""" +name_on_order+"""','"""+ ingredient_string+"""')"""

    #st.write(my_insert_stmt)
   

    if add_btn:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
    

