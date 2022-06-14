import streamlit as st
import streamlit_book as stb
import time
import random

# Custom question
st.title("True or False Question")
st.header("Question with custom behavior")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    checked_answer, correct_answer = stb.true_or_false("Are you a cyborg robot?", 
                                                        False, 
                                                        success="",
                                                        error="",
                                                        button='Check THIS answer')
    if checked_answer:
        if correct_answer:
            st.info("Welcome fellow human!")            
            st.balloons()
        else:
            N = 10.0
            pb = st.progress(0.0)
            ph = st.empty()
            robot_message = ""
            for i in range(1, int(N+1)):
                pb.progress(i/N)
                robot_message += random.choice(["BIP ", "bip ", "BOP ", "bop "])
                ph.code(robot_message)
                time.sleep(.5)
    else:
        st.write("You need to check the answer")