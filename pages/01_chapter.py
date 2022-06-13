import streamlit as st
import streamlit_book as stb

show_code = st.checkbox("Show code", False)
with stb.echo("below", show_code):
    st.header("Chapter: multiple connected pages")
    st.markdown("""
    You only need previous/next buttons. 

    Use `stb.set_chapter_config` to set the path and other book configurations.
    The pages can live anywhere you like, but I recommend to use "./docs/" or "./pages/subdir/".
    """)

    

