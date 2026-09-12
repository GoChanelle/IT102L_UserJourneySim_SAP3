import streamlit as st

from DeepClean_CreatureInfo import Creature

# PAGE CONFIG -----------------------------------------------------------
st.set_page_config(
  page_title="DeepClean",
  page_icon="🏦",
  layout="wide"
)

# PAGE TITLE ------------------------------------------------------------
st.markdown("""
<style>
div[data-testid="stImage"] img {
    height: 180px;
    width: 100%;
    object-fit: cover;
    object-position: center;
}
</style>
""", unsafe_allow_html=True)
st.image(
    "https://static.wikia.nocookie.net/limbuscompany/images/e/e2/Story_boat_cloudy2.png/revision/latest/scale-to-width-down/985?cb=20231120093636",
    caption = "Great Lake (Limbus Company - Canto V)")

st.title("Deep Sea Cleaning")
st.subtitle("The sea is in shambles.")
st.caption("Rough simulation for IT102L Exam")
st.divider()

creature1 = Creature(
    "Bag", "Mistaken for sustenance", "Oxygen Depletion", 90
    )

creature1.display_info()