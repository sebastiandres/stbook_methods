import streamlit as st
import streamlit_book as stb

st.title("True or False Question")
st.header("Question with minimal arguments")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.true_or_false("Are you a robot?", False)
