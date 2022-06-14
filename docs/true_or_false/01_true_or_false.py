import streamlit as st
import streamlit_book as stb

st.title("True or False Question")
st.header("Question with all optional arguments")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.true_or_false("Are you a cyborg?", False, 
                        success='Pfiuuuuu!!!', 
                        error='RoBoTs NoT WeLcOmE to tHiS aPp', 
                        button='Check MY answer')
