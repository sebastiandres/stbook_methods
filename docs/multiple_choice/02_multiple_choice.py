import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Multiple Choice Question")
st.header("Question with all optional arguments")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    checked_answer, correct_answer = stb.multiple_choice(
                        "I typically ask recruiters to say which of these are pokemon",
                        {"ditto":True,
                         "jupyter":False,
                         "pyspark":False,
                         "scikit":False,
                         "metapod":True,
                         "vulpix":True},
                        success='', 
                        error="", 
                        button='Check'
                       )
    if checked_answer:
        if correct_answer:
            st.info("Bravo!!!")         
            st.balloons()
        else:
            st.warning("Gotta pump those numbers, roockie!!!")            
    else:
        st.write("You need to check the answer")