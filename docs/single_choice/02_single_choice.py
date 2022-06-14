import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Single Choice Question")
st.header("Question with custom behavior")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
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
