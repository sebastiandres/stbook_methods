import streamlit as st
import streamlit_book as stb

st.title("Python examples from/for readthedocs")

stb.single_choice("Question description", 
                  ["False alternative", "Another false alternative", 
                   "The true alternative", "Yet another false alternative"],
                  2, 
                  success="custom success message", 
                  error="custom error message", 
                  button="custom button text")


# To control the width of the text outputs
c1, c2 = st.columns([5,5])
with c1:
    stb.single_choice("What does pandas (python library) stands for?",
                      ["The cutest bear", "Pure Adamantium Numeric Datasets And Stuff", 
                       "PArties & DAtaSets", "Panel Data"],
                      3,
                      success='Now you know!', 
                      error='Nopes, not this one...', 
                      button='Check'
                     )