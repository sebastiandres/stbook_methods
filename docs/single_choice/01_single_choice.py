import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Single Choice Question")
st.header("Question with all optional arguments")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.single_choice("What does pandas (python library) stands for?",
                      ["The cutest bear", "Pure Adamantium Numeric Datasets And Stuff", 
                       "PArties & DAtaSets", "Panel Data"],
                      3,
                      success='Now you know!', 
                      error='Nopes, not this one...', 
                      button='Check MY answer'
                     )