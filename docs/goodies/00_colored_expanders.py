import streamlit as st
import streamlit_book as stb

st.title("Colored Expanders")

show_code = st.checkbox("Show code?", False, key="ce1")
with stb.echo("below", show_code):
    with st.expander("INFO"):
        st.markdown("Lorem")
        st.markdown("Ipsum")

show_code = st.checkbox("Show code?", False, key="ce2")
with stb.echo("below", show_code):
    with st.expander("Success"):
        st.markdown("Lorem")
        st.markdown("Ipsum")

show_code = st.checkbox("Show code?", False, key="ce3")
with stb.echo("below", show_code):
    with st.expander("OK"):
        st.markdown("Lorem")
        st.markdown("Ipsum")

show_code = st.checkbox("Show code?", False, key="ce4")
with stb.echo("below", show_code):
    with st.expander("Warning"):
        st.markdown("Lorem")
        st.markdown("Ipsum")

show_code = st.checkbox("Show code?", False, key="ce5")
with stb.echo("below", show_code):
    with st.expander("Error"):
        st.markdown("Lorem")
        st.markdown("Ipsum")

show_code = st.checkbox("Show code?", False, key="ce6")
with stb.echo("below", show_code):
    with st.expander("A regular expander"):
        st.markdown("Lorem")
        st.markdown("Ipsum")
