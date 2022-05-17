import streamlit as st
import streamlit_book as stb

st.title("Python examples from/for readthedocs")

stb.true_or_false("Question description - True answer expected", True, 
                    success="custom success message", 
                    error="custom failure message", 
                    button="custom button text")

stb.true_or_false("Question description - False answer expected", False, 
                    success="custom success message", 
                    error="custom failure message", 
                    button="custom button text")

# To control the width of the text outputs
c1, c2 = st.columns([5,5])
with c1:
    stb.true_or_false('Is "Indiana Jones and the Last Crusade" the best movie of the trilogy?', 
                        True, 
                        success="You have chosen wisely", 
                        error="You have chosen poorly", 
                        button="You must choose")
