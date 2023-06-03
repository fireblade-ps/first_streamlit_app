import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#app_code
streamlit.title('My Parents healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build your own Smoothie 🥝🍇')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.Fruit), ['Avocado','Strawberries'])
streamlit.text(fruits_selected)
fruits_to_show = my_fruit_list.loc['Avocado']
streamlit.dataframe(fruits_to_show)
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
#streamlit.dataframe(fruits_selected)
