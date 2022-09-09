import streamlit as st
import streamlit_book as stb

st.title("Answers")

st.markdown("""
Both `stb.set_book_config` and `stb.set_library_config` can receive a `save_answers` argument.
* If `save_answers=False` (default value), the user answers are not saved. 
* If `save_answers=True`, the user's answers are saved into the file /tmp/answers.csv. Users will get a warning message that the answers will be saved, they have to dismiss. 

The stored answers can be accesed through the admin page, requiring authentication.
""")