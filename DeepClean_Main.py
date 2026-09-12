import streamlit as st

from DeepClean_CreatureInfo import Creature

# PAGE CONFIG -----------------------------------------------------------
st.set_page_config(
  page_title="DeepClean",
  page_icon="🏦",
  layout="wide"
)

# PAGE TITLE ------------------------------------------------------------
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://static.wikia.nocookie.net/limbuscompany/images/e/e2/Story_boat_cloudy2.png/revision/latest/scale-to-width-down/985?cb=20231120093636");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: local;
}
</style>
"""

st.html(background_image)

st.title("Deep Sea Cleaning")
st.subheader("The sea is in shambles.")
st.caption("Rough simulation for IT102L Exam")
st.divider()

creature1 = Creature(
    "Bag", "Mistaken for sustenance", "Oxygen Depletion", 90
    )

creature1.display_info()