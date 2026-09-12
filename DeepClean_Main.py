import streamlit as st

from DeepClean_Intro import show_introduction

# PAGE CONFIG -----------------------------------------------------------
st.set_page_config(
  page_title="DeepClean",
  page_icon="🌊",
  layout="wide"
)

# PAGE TITLE ------------------------------------------------------------

st.title("Deep Sea Cleaning")
st.subheader("The sea is in shambles.")
st.caption("Rough simulation for IT102L Exam")
st.divider()

# MENU OPTIONS -----------------------------------------------------------

options = ["Introduction", "Check Gear", "Dive", "Creature Index"]

if "menu" not in st.session_state:
    st.session_state.menu = options[0]  # default to "New Game"

for option in options:
    button_type = "primary" if st.session_state.menu == option else "secondary"
    if st.sidebar.button(option, use_container_width=True, type=button_type):
        st.session_state.menu = option
menu = st.session_state.menu

# STORY INTRODUCTION -----------------------------------------------------
if menu == "Introduction":
    st.caption("This is where the game would start")

    show_introduction()

    st.divider()

    if "show_mirror" not in st.session_state:
        st.session_state.show_mirror = False

    if st.button("Check Mirror", width="stretch"):
            st.session_state.show_mirror = not st.session_state.show_mirror

    if st.session_state.show_mirror:
        col4 = st.columns(1, border=True)[0]
        col4.write("Your already wearing your full diving gear. It's heavy")

elif menu == "Load Game":
    st.write("This is a simulated experience. You cannot load any previous attempts ):")
