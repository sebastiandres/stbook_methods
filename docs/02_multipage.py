import streamlit as st
import streamlit_book as stb

st.title("Multipage")

st.markdown("There are several user cases for having multipages on streamlit. We'll explore each one of those")

st.header("Basic or interactive single page")
st.markdown("""
You use only streamlit (no need can use streamlit_book).  

Optionally, if you want to use any of the python function for activities/questions, you can use streamlit_book. No need to initialize the library.
""")

st.header("Book: A single document with multiple connected pages")
st.markdown("""
You only need previous/next buttons. 

Use `stb.set_book_config` to set the path and other book configurations.
""")

st.header("Library: several simple or multipaged books")
st.markdown("""
Requires a sidebar menu (like this demo), where each topic required a previous/next buttons. 

Use `stb.set_library_config` to set the path and the configuration for the book.
""")
