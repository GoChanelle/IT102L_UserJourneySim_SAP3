import random
import streamlit as st


def dive_screen():
    col1 = st.columns(1, border=True)[0]
    col1.write("The water looks thick. You almost topple over at the force of the waves crashing.")
    col1.write("You can't really back out now. So, when you are ready...")
    creatures = st.session_state.creatures

    if "current_encounter" not in st.session_state:
        st.session_state.current_encounter = None

    if st.button(":red[Dive In]", width="stretch"):
        uncollected = creatures.get_uncollected()
        if uncollected:
            st.session_state.current_encounter = random.choice(uncollected)
        else:
            st.session_state.current_encounter = None
            st.info("Is the sea finally clean..?")

    encounter = st.session_state.current_encounter
    if encounter:
        info = creatures.get_all()[encounter]
        col1 = st.columns(1, border=True)[0]
        col1.write(f"You spot a **{encounter}**.")

        if col1.button(f"Collect {encounter}"):
            msg = creatures.collect(encounter)
            st.success(msg)
            st.session_state.current_encounter = None
            st.rerun()