import streamlit as st

from DeepClean_CreatureInfo import Creature

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

options = ["New Game", "Load Game", "Settings"]

if "menu" not in st.session_state:
    st.session_state.menu = options[0]  # default to "New Game"

for option in options:
    button_type = "primary" if st.session_state.menu == option else "secondary"
    if st.sidebar.button(option, use_container_width=True, type=button_type):
        st.session_state.menu = option
menu = st.session_state.menu

if menu == "New Game":
    st.image("blob:https://www.messenger.com/c25bae2c-236e-404c-a2d4-2ec46a1bab60")
    st.caption("This is where the game would start")

elif menu == "Load Game":
    st.write("This is a simulated experience. You cannot load any previous attempts ):")
