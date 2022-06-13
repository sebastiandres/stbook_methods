import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Code Input")

show_code = st.checkbox("Show code")
c1, c2 = st.columns(2)
with c1:
    with stb.echo("below", show_code):
        stb.code_input("Print 'Hello World2'", "print('Hola Mundo')", equals="2020")
