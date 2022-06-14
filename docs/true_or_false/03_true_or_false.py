import streamlit as st
import streamlit_book as stb

st.title("True or False Question")
st.header("An example")

# To control the width of the text outputs
show_code = st.checkbox("Show code?")
with stb.echo("below", show_code):
    stb.true_or_false('Is "Indiana Jones and the Last Crusade" the best movie of the trilogy?', 
                        True, 
                        success="You have chosen wisely", 
                        error="You have chosen poorly", 
                        button="You must choose")
