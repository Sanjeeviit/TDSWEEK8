import streamlit as st

def display_substrings(input_string):
    substrings = [input_string[:i+1] for i in range(len(input_string))]
    return substrings

st.title("Display Substrings")
input_string = "sanjeev"
substrings = display_substrings(input_string)

for substring in substrings:
    st.write(substring)
