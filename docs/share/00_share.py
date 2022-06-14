import streamlit as st
import streamlit_book as stb

st.title("Share on Social Media")

show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.share("This is my text", "https://streamlit-book.readthedocs.io/")