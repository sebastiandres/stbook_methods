import streamlit as st
import streamlit_book as stb

def my_private_function_1():
    st.title("True or False Question")
    st.header("An example")

def my_private_function_2():
    show_code = st.checkbox("Show code?")
    with stb.echo("below", show_code):
        stb.true_or_false('Is "Indiana Jones and the Last Crusade" the best movie of the trilogy?', 
                            True, 
                            success="You have chosen wisely", 
                            error="You have chosen poorly", 
                            button="You must choose")

my_private_function_1()
my_private_function_2()