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