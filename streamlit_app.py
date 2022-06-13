import streamlit as st
import streamlit_book as stb
from pathlib import Path

def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_icon="📚", page_title="Streamlit Book - ReadTheDocs Demo")

       # Control the entry point
       query_params = st.experimental_get_query_params()
       view_file = "" # Default value
       if "view" in query_params:
              view = query_params["view"][0]
              current_path = Path(__file__).parent.absolute()
              view_dict = {
                     "true_or_false": current_path / "pages/05 TrueFalse/00_true_or_false.py",
                     "single_choice": current_path / "pages/06 SingleChoice/00_single_choice.py",
                     "multiple_choice": current_path / "pages/07 MultipleChoice/00_multiple_choice.py",
                     "to_do_list": current_path / "pages/08 ToDoList/00_to_do_list.py",
              }
              if view in view_dict:
                     view_file = view_dict[view]

       if view_file:
              st.title("Should be rendering page: " + view)
              stb.render_file(view_file)
       else:
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

if __name__ == "__main__":
       main()