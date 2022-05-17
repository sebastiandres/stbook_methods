import streamlit as st
import streamlit_book as stb

st.title("Python examples from/for readthedocs")

stb.true_or_false("Question description", 
                    {
                    "False alternative":False, 
                    "A true alternative":True, 
                    "Another false alternative":False, 
                    "Another true alternative":True, 
                    "Yet another false alternative":False},
                    success="custom success message", 
                    error="custom error message", 
                    button="custom button text")

# To control the width of the text outputs
c1, c2 = st.columns([5,5])
with c1:
    stb.multiple_choice("I typically ask recruiters to point out which of these area pokemon",
                        {"ditto":True,
                         "jupyter":False,
                         "pyspark":False,
                         "scikit":False,
                         "metapod":True,
                         "vulpix":True},
                        success='Are you a pokemon master?', 
                        error="Gotta catch them all!", 
                        button='Check'
                       )
