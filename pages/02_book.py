import streamlit as st
import streamlit_book as stb

show_code = st.checkbox("Show code", False)
with stb.echo("below", show_code):
    st.header("Book: A collection of chapters")
    st.markdown("""
    Requires a sidebar menu (like this demo), where each topic required a previous/next buttons. 

    Use `stb.set_book_config` to set the path and the configuration for the book.
    """)

    # Streamit book properties
    save_answers = False
    current_path = Path(__file__).parent.absolute()
    stb.set_book_config(menu_title="streamlit_book",
                        menu_icon="lightbulb",
                        options=[
                                        "What's new on v0.7.0?",   
                                        "Core Features", 
                                        "Multipages", 
                                        "Answers", 
                                        "Admin View", 
                                        "Colored Expanders",
                                        "True/False Question",
                                        "Single Choice Question",
                                        "Multiple Choice Question",
                                        "To Do List",
                                        "Text Input",
                                        "Code Input",
                                        ], 
                        paths=[
                                        current_path / "pages/00_whats_new.py", 
                                        current_path / "pages/01 Multitest", 
                                        current_path / "pages/02_multipage.py",
                                        current_path / "pages/03_answers.py",
                                        current_path / "pages/04_admin_view.py",
                                        current_path / "pages/05_colored_expanders.py",
                                        current_path / "pages/05 TrueFalse", 
                                        current_path / "pages/06 SingleChoice",
                                        current_path / "pages/07 MultipleChoice",
                                        current_path / "pages/08 ToDoList", 
                                        current_path / "pages/09_text_input.py", 
                                        current_path / "pages/10_code_input.py", 
                                ],
                        icons=[
                                        "code", 
                                        "robot", 
                                        "book", 
                                        "pin-angle", 
                                        "shield-lock",
                                        "paint-bucket",
                                        "signpost-2",
                                        "ui-radios",
                                        "ui-checks",
                                        "check2-square",
                                        "check2-square",
                                        "check2-square",
                                ],
                        save_answers=save_answers,
                        )