import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Text Input")

show_code = st.checkbox("Show code")
with stb.echo("below", show_code):
    stb.text_input("In what year was streamlit released?", "20xx", equals="2020")
