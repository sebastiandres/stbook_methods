import streamlit as st
import streamlit_book as stb
import time
import random

st.title("To Do List")
st.header("Question with minimal arguments")

show_code = st.checkbox("Show code?", False, key="tdl0")
with stb.echo("below", show_code):
    stb.to_do_list( 
                tasks={"a":True, "b":False, "c":False} # required argument
                )