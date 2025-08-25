import streamlit as st

st.set_page_config(page_title="Simple Streamlit App", page_icon="👋")

st.title("Welcome to My Simple Streamlit App with CI CD!")

st.write("This is a basic Streamlit application created by Cline.")
st.write("You can expand this app with more interactive elements, data visualizations, and machine learning models.")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

st.sidebar.header("About")
st.sidebar.info(
    "This app demonstrates a basic Streamlit setup."
)
