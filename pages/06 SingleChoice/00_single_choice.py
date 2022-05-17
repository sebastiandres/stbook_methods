import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Single Choice Question")

# Required arguments
st.header("Question with minimal arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
stb.single_choice("What does pandas (the library) stands for?",
                  ["The cutest bear", "Panel Data", 
                   "Pure Adamantium Numeric Datasets And Stuff", "PArties & DAtaSets"],
                  1)
    """)
with c2:
    stb.single_choice("What does pandas (the library) stands for?",
                      ["The cutest bear", "Panel Data", 
                      "Pure Adamantium Numeric Datasets And Stuff", "PArties & DAtaSets"],
                      1)

# All arguments
st.header("Question with all optional arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
stb.single_choice("What does pandas (python library) stands for?",
                  ["The cutest bear", "Pure Adamantium Numeric Datasets And Stuff", 
                   "Panel Data", "PArties & DAtaSets"],
                  2,
                  success='Now you know!', 
                  error='Nopes, not this one...', 
                  button='Check MY answer'
                  )
        """)
with c2:
    stb.single_choice("What does pandas (python library) stands for?",
                      ["The cutest bear", "Pure Adamantium Numeric Datasets And Stuff", 
                       "PArties & DAtaSets", "Panel Data"],
                      3,
                      success='Now you know!', 
                      error='Nopes, not this one...', 
                      button='Check MY answer'
                     )

# Custom question
st.header("Question with custom behavior")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
checked_answer, correct_answer = stb.single_choice(
                                    "What does pandas (the python library) stands for?",
                                    ["The cutest bear", 
                                     "Pure Adamantium Numeric Datasets And Stuff", 
                                     "Panel Data", 
                                     "PArties & DAtaSets"],
                                    2,
                                    success='', 
                                    error='', 
                                    button='Check THE answer'
                                    )

if checked_answer:
    if correct_answer:
        st.info("Yes! It's Panel Data, but here's a pandas as a prize just for you!")           
        st.image('https://www.stockvault.net/data/2016/06/30/203684/preview16.jpg')
        st.balloons()
    else:
        st.warning("Sadly, that's not true")
else:
    st.write("You need to check the answer")
        """)
with c2:
    checked_answer, correct_answer = stb.single_choice(
                    "What does pandas (the python library) stands for?",
                    ["The cutest bear", "Pure Adamantium Numeric Datasets And Stuff", 
                     "Panel Data", "PArties & DAtaSets"],
                    2,
                    success='', 
                    error='', 
                    button='Check THE answer'
                    )

    if checked_answer:
        if correct_answer:
            st.info("Yes! It's Panel Data, but here's a pandas as a prize just for you!")           
            st.image('https://www.stockvault.net/data/2016/06/30/203684/preview16.jpg')
            st.balloons()
        else:
            st.warning("Sadly, that's not true")
    else:
        st.write("You need to check the answer")
