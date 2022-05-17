import streamlit as st
import streamlit_book as stb
from pathlib import Path

def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_icon="📚", page_title="Book Demo 0.7.0")

       # Streamit book properties
       save_answers = True
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
                                   ],
                            save_answers=save_answers,
                            )


if __name__ == "__main__":
       main()