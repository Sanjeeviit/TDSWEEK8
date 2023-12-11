import streamlit as st

def display_substrings(input_string):
    substrings = [input_string[:i+1] for i in range(len(input_string))]
    return substrings

st.title("Display Substrings")

# Input box for the user to enter a string
input_string = st.text_input("Enter a string:")

# Display the sequence of substrings
substrings = display_substrings(input_string)

for substring in substrings:
    st.write(substring)
