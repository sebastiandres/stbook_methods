import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Multiple Choice Question")

# Default
st.header("Question with minimal arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
stb.multiple_choice("I typically ask recruiters to point out which of these are pokemon",
                    {"ditto":True,
                     "jupyter":False,
                     "pyspark":False,
                     "scikit":False,
                     "metapod":True,
                     "vulpix":True}
                   )
    """)
with c2:
    stb.multiple_choice("I typically ask recruiters to point out which of these area pokemon",
                        {"ditto":True,
                         "jupyter":False,
                         "pyspark":False,
                         "scikit":False,
                         "metapod":True,
                         "vulpix":True}
                       )
                       
# Custom
st.header("Question with all optional arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
stb.multiple_choice("I typically ask recruiters to point out which of these are pokemons",
                    {"ditto":True,
                     "jupyter":False,
                     "pyspark":False,
                     "scikit":False,
                     "metapod":True,
                     "vulpix":True},
                    success='Indeed!', 
                    error="Gotta catch them all!", 
                    button='Check MY answer'
                   )
        """)
with c2:
    stb.multiple_choice("I typically ask recruiters to point out which of these are pokemons",
                        {"ditto":True,
                         "jupyter":False,
                         "pyspark":False,
                         "scikit":False,
                         "metapod":True,
                         "vulpix":True},
                        success='Indeed!', 
                        error="Gotta catch them all!", 
                        button='Check MY answer'
                       )

# Custom question
st.header("Question with custom behavior")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
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
    """)
with c2:
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