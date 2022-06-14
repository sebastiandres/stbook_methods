import streamlit as st
import streamlit_book as stb
import time
import random

st.title("Multiple Choice Question")
st.header("Question with minimal arguments")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.multiple_choice("I typically ask recruiters to point out which of these area pokemon",
                        {"ditto":True,
                         "jupyter":False,
                         "pyspark":False,
                         "scikit":False,
                         "metapod":True,
                         "vulpix":True}
                       )
          