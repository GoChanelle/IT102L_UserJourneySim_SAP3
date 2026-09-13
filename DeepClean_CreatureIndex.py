import streamlit as st


def creature_index():
    st.subheader("Creature Index")
    creatures = st.session_state.creatures

    for name, info in creatures.get_all().items():
        col1, col2 = st.columns([3, 1])
        if info["collected"]:
            col1.write(f"**{name}** — {info['description']}")
            col2.write("✅ Collected")
        else:
            col1.write("❓ ??? — undiscovered")
            col2.write("🔒 Locked")