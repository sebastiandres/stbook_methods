import streamlit as st
import streamlit_book as stb
import time
import random

st.title("To Do List")
st.header("Question with all optional arguments")

show_code = st.checkbox("Show code?", False, key="tdl1")
with stb.echo("below", show_code):
    stb.to_do_list( 
                tasks={"a":True, "B":False, "c":False}, # mandatory
                header="Description", # optional argument
                success="Pelota increíble - Incredibol - Incrediball - Incredible!" # optional argument
                )