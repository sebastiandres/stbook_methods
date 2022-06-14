import streamlit as st
import streamlit_book as stb

st.title("Echo")

show_code = st.checkbox("Show code?")
st.write("Hello World!")

if show_code:
    st.code("""
show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    st.write("Hello World!")
""")