import streamlit as st
from savings_account import savingsAccount

st.set_page_config(page_title = "BANK APP", layout = 'centered')

savings = savingsAccount(200000)

with st.form('savings_form'):
    amount = st.number_input("Enter amount")
    operations = st.selectbox('Deposit or withdraw', ("deposit", "withdraw", "transfer",))
    submit = st.form_submit_button("Submit")

if submit and operations == "withdraw":
    with st.spinner("Processing..."):
        if amount <= 10000:
            savings.withdraw(amount)
            st.write(f"your balance is {savings.balance}")

        if amount > savings.balance:
            st.write("Insufficient Balance")
            
        else:
            st.write("you have exceeded your limit")

if submit and operations == "deposit":
     with st.spinner("Processing..."):
        savings.deposit(amount)
        st.write(f"your balance is {savings.balance}")