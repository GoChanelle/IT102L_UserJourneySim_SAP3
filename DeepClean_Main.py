import streamlit as st

from DeepClean_Intro import show_introduction, check_mirror, check_outside
from DeepClean_Gear import Gear
from DeepClean_Shop import repair_station, gear_shop

# PAGE CONFIG -----------------------------------------------------------
st.set_page_config(
  page_title="DeepClean",
  page_icon="🌊",
  layout="wide"
)

if "gear" not in st.session_state:
    st.session_state.gear = Gear()

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
    check_mirror()
    check_outside()

# CHECK / REPLACE GEAR -----------------------------------------------------   

elif menu == "Check Gear":
    st.caption("This is how you would check your gear for damages and repairs.")

    repair_station()
    st.divider()
    gear_shop()
