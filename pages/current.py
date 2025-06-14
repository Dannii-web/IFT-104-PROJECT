import streamlit as st
from current_account import CurrentAccount

st.set_page_config(page_title = "BANK APP", layout = 'centered')

Current = CurrentAccount(200000)

with st.form('current_form'):
    amount = st.number_input("Enter amount")
    operations = st.selectbox('Deposit or withdraw', ("deposit", "withdraw", "transfer",))
    submit = st.form_submit_button("Submit")

if submit and operations == "withdraw":
    with st.spinner("Processing..."):
        if amount <= 10000:
            Current.withdraw(amount)
            st.write(f"your balance is {Current.balance}")

        if amount > Current.balance:
            st.write("Insufficient Balance")
            
        else:
            st.write("you have exceeded your limit")

if submit and operations == "deposit":
     with st.spinner("Processing..."):
        Current.deposit(amount)
        st.write(f"your balance is {Current.balance}")