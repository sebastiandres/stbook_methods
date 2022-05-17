import streamlit as st
import streamlit_book as stb
import time
import random

st.title("To Do List")

# Default
st.header("Question with minimal arguments")
c1, c2 = st.columns([5,5])
with c1:
    st.code("""
    stb.to_do_list( 
                tasks={"a":True, "b":False, "c":False} # required argument
                )
        """)
with c2:
    stb.to_do_list( 
                tasks={"a":True, "b":False, "c":False} # required argument
                )

# Default
st.header("Question with all optional arguments")
c1, c2 = st.columns([5,4])
with c1:
    st.code("""
    stb.to_do_list( 
                tasks={"a":True, "B":False, "c":False}, # mandatory
                header="Description", # optional argument
                success="Pelota increíble - Incredibol - Incrediball - Incredible!" # optional argument
                )
    """)
with c2:
    stb.to_do_list( 
                tasks={"a":True, "B":False, "c":False}, # mandatory
                header="Description", # optional argument
                success="Pelota increíble - Incredibol - Incrediball - Incredible!" # optional argument
                )

# Custom question
st.header("Question with custom behavior")
c1, c2 = st.columns([4,3])
with c1:
    st.code("""
    all_task_completed = stb.to_do_list(
                                        tasks={"A":True, "B":False, "C":False}, # mandatory
                                        header="Description 02", # optional argument
                                        success="Bravo!" # optional argument
                                        )
    if all_task_completed:
        st.info("Bravo!")            
    else:
        st.info("Yes, you can!")            
    """)
with c2:
    all_task_completed = stb.to_do_list(
                                        tasks={"A":True, "B":False, "C":False}, # mandatory
                                        header="", # optional argument
                                        success="" # optional argument
                                        )
    if all_task_completed:
        st.info("Bravo!")            
    else:
        st.info("Yes, you can!")            
