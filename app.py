import streamlit as st

st.title("Calculator Application")

number1=st.number_input("Insert a number ",step=1,placeholder="Enter your first number")
number2=st.number_input("Insert a number ",step=1,placeholder="Enter your second number")
operation=st.selectbox("select the operation",("Addition","subtraction"))
ret=st.button("calculate")
if ret:
    if operation=="Addition":
        st.write(number1+number2)
    elif operation=="subtraction":
            st.write(number1-number2)
        