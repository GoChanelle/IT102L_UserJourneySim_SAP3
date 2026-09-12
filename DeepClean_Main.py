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

    col1 = st.columns(1, border=True)[0]
    col1.write("It's the year 20xx. Less of the world is becoming inhabitable."
               " The air around the coastline is thick and the waters are dangerous.")

    col2 = st.columns(1, border=True)[0]
    col2.write("The coastline is prohibited to anyone who isn't a Diver."
               " Unfortunately, you are a :red[Diver].")

    col3 = st.columns(1, border=True)[0]
    col3.write("Your job is to maintain the Trash Beasts for a hopefully better future."
                   " Goodluck, :red[Don't Drown].")

elif menu == "Load Game":
    st.write("This is a simulated experience. You cannot load any previous attempts ):")
