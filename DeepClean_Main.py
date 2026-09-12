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

creature1 = Creature(
    "Bag", "Mistaken for sustenance", "Oxygen Depletion", 90
    )

creature1.display_info()