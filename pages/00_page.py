import streamlit as st
import streamlit_book as stb

show_code = st.checkbox("Show code", False)
with stb.echo("below", show_code):
    st.title("Single Page")

    st.header("Basic or interactive single page")
    st.markdown("""
    You use only streamlit (no need can use streamlit_book).  

    Optionally, if you want to use any of the python function for activities/questions, you can use streamlit_book. No need to initialize the library.
    """)


