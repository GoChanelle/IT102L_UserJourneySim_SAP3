import streamlit as st

def show_introduction():
    col1 = st.columns(1, border=True)[0]
    col1.write("It's the year 20xx. Less of the world is becoming inhabitable."
               " The air around the coastline is thick and the waters are dangerous.")

    col2 = st.columns(1, border=True)[0]
    col2.write("The coastline is prohibited to anyone who isn't a Diver."
               " Unfortunately, you are a :red[Diver].")

    col3 = st.columns(1, border=True)[0]
    col3.write("Your job is to maintain the Trash Beasts for a hopefully better future."
               " Goodluck, :red[Don't Drown].")

def check_mirror():
    if "show_mirror" not in st.session_state:
            st.session_state.show_mirror = False
    
    if st.button("Check Mirror", width="stretch"):
                st.session_state.show_mirror = not st.session_state.show_mirror
    
    def check_mirror():
        if "show_mirror" not in st.session_state:
            st.session_state.show_mirror = False

        if st.button("Check Mirror", width="stretch"):
            st.session_state.show_mirror = not st.session_state.show_mirror

        if st.session_state.show_mirror:
            col4 = st.columns(1, border=True)[0]
            col4.write("You check your gear in the mirror...")

            gear = st.session_state.gear
            for item in gear.gear_inventory():
                status = gear.gear_status[item]
                color = "red" if status == "Broken" else "green"
                col4.write(f"{item}: :{color}[{status}]")

def check_outside():
    if "show_outside" not in st.session_state:
                   st.session_state.show_outside = False
           
    if st.button("Check Outside", width="stretch"):
                       st.session_state.show_outside = not st.session_state.show_outside
           
    if st.session_state.show_outside:
                   col6 = st.columns(1, border=True)[0]
                   col6.write("A heavy fogs settles on the coastline. The sea is bubbling with energy.")