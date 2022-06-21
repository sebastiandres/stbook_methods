import streamlit as st
import streamlit_book as stb

st.title("Floating button")
st.markdown("The floating button floats over text and other elements.")

show_code = st.checkbox("Show code?")

with stb.echo("below", show_code):
    import random
    import string
    char_set = string.ascii_lowercase
    text = ""
    for words in range(100):
        for word_length in range(random.randint(1, 15)):
            text += " " + "".join(random.sample(char_set*word_length, word_length))
    st.markdown(text)
    c1, c2 = st.columns(2)
    c1.markdown(text[:1000])
    c2.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")
    st.markdown(text)
    stb.floating_button("https://streamlit-book.readthedocs.io/", "file-earmark-richtext-fill", "white", "red")