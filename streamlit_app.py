import streamlit as st
import streamlit_book as stb
from pathlib import Path
from glob import glob
def main():
    # Streamlit webpage properties
    st.set_page_config(layout="wide", page_icon="📚", page_title="stb methods demo")

    # Control the entry point
    query_params = st.experimental_get_query_params()
    save_answers = False
    current_path = Path(__file__).parent.absolute()

    # Decide if we need to show a single file or not
    if "view" in query_params:
        view = query_params["view"][0]
        regex = str(current_path) + "/docs/*/*" + view + ".py"
        matching_files = glob(regex)
    else:
        matching_files=[]

    # Show the single page or the whole app
    if len(matching_files)>0:
        view_file = sorted(matching_files)[0]
        stb.render_file(view_file)
        # Add info on where to find the whole app
        url = "https://stbook-methods.streamlitapp.com/"
        html_link = f'[{url}]({url})'
        mkd = f"See full app at {html_link}"
        st.markdown(mkd)
    else:
        # Streamit book properties
        stb.set_book_config(menu_title="streamlit_book",
                            menu_icon="lightbulb",
                            options=[
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
                                    "Admin", 
                                    ], 
                            paths=[
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
                                    current_path / "docs/answers",
                                    current_path / "docs/admin",
                                    ],
                            save_answers=save_answers,
                            #display_page_info=False,
                            )

if __name__ == "__main__":
    main()