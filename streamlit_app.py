import streamlit as st
import streamlit_book as stb
from pathlib import Path
from glob import glob
def main():
       # Streamlit webpage properties
       st.set_page_config(layout="wide", page_icon="📚", page_title="stb methods demo")

       # Control the entry point
       query_params = st.experimental_get_query_params()
       view_file = "" # Default value
       if "view" in query_params:
              view = query_params["view"][0]
              current_path = Path(__file__).parent.absolute()
              regex = str(current_path) + "/docs/*/*" + view + ".py"
              matching_files = sorted(glob(regex))
              view_file = sorted(matching_files)[0]
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
                                                 "What's new?",   
                                                 "True/False Question",
                                                 "Single Choice Question",
                                                 "Multiple Choice Question",
                                                 "To Do List",
                                                 "Text Input",
                                                 "Code Input",
                                                 "Echo",
                                                 "Colored Expanders",
                                                 "Share",
                                                 "Floating Button",
                                                 "Answers", 
                                                 "Admin View", 
                                                 ], 
                                   paths=[
                                                 current_path / "docs/00_whats_new.py", 
                                                 current_path / "docs/true_or_false", 
                                                 current_path / "docs/single_choice",
                                                 current_path / "docs/multiple_choice",
                                                 current_path / "docs/to_do_list", 
                                                 current_path / "docs/text_input", 
                                                 current_path / "docs/code_input", 
                                                 current_path / "docs/goodies/00_echo.py", 
                                                 current_path / "docs/goodies/00_colored_expanders.py",
                                                 current_path / "docs/goodies/00_share.py",
                                                 current_path / "docs/goodies/00_button.py",
                                                 current_path / "docs/03_answers.py",
                                                 current_path / "docs/04_admin_view.py",
                                          ],
                                   save_answers=save_answers,
                                   display_page_info=False,
                                   )

if __name__ == "__main__":
       main()