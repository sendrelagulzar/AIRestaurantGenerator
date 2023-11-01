import streamlit as st
import ResturantLLM as rllm

#List of crusine
cuisine_list = [
    "Italian Cuisine",
    "Chinese Cuisine",
    "Japanese Cuisine",
    "Mexican Cuisine",
    "French Cuisine",
    "Indian Cuisine",
    "Thai Cuisine",
    "Greek Cuisine",
    "Spanish Cuisine",
    "Korean Cuisine",
    "Vietnamese Cuisine",
    "Turkish Cuisine",
    "Mediterranean Cuisine",
    "Middle Eastern Cuisine",
    "American Cuisine",
    "Brazilian Cuisine",
    "Peruvian Cuisine",
    "Russian Cuisine",
    "British Cuisine",
    "Ethiopian Cuisine",
    "Caribbean Cuisine",
    "Moroccan Cuisine",
    "Indonesian Cuisine",
    "African Cuisine",
    "Lebanese Cuisine"
]
cuisine_list.sort()
cuisine_list[0]='Any'

st.sidebar.title("Resturant Suggestor")

cuisine=st.sidebar.selectbox('Select Type of crusine',cuisine_list)

if(cuisine):
    response=rllm.Data(cuisine)
    
st.title(response['restaurant_name'].strip())
st.write("**:blue[Menu Items:]**")
menu=response['menu_items'].strip().split(',')
for i in menu:
    st.write(f"{i}")