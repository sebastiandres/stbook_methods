import streamlit as st
import streamlit_book as stb
from pathlib import Path

def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_icon="📚", page_title="stb methods demo")

       # Control the entry point
       query_params = st.experimental_get_query_params()
       view_file = "" # Default value
       if "view" in query_params:
              view = query_params["view"][0]
              current_path = Path(__file__).parent.absolute()
              view_file = current_path / "docs" / view / f"00_{view}.py"
              print(view_file)
       if view_file:
              # Render file
              stb.render_file(view_file)
              # Add info on where to find the whole app
              url = "https://stb_methods.streamlitapp.com/"
              html_link = f'<a href="{url}" target="_blank">{url}</a>'
              mkd = f"See full app at {html_link}"
              st.markdown(mkd)
       else:
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
                                                 "True/False Question",
                                                 "Single Choice Question",
                                                 "Multiple Choice Question",
                                                 "To Do List",
                                                 "Text Input",
                                                 "Code Input",
                                                 "Echo",
                                                 "Colored Expanders",
                                                 "Share",
                                                 ], 
                                   paths=[
                                                 current_path / "docs/00_whats_new.py", 
                                                 current_path / "docs/01 Multitest", 
                                                 current_path / "docs/02_multipage.py",
                                                 current_path / "docs/03_answers.py",
                                                 current_path / "docs/04_admin_view.py",
                                                 current_path / "docs/true_or_false", 
                                                 current_path / "docs/single_choice",
                                                 current_path / "docs/multiple_choice",
                                                 current_path / "docs/to_do_list", 
                                                 current_path / "docs/text_input", 
                                                 current_path / "docs/code_input", 
                                                 current_path / "docs/echo", 
                                                 current_path / "docs/colored_expanders",
                                                 current_path / "docs/share",
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
                                                 "check2-square",
                                                 "check2-square",
                                          ],
                                   save_answers=save_answers,
                                   )

if __name__ == "__main__":
       main()