import streamlit as st

def main():
    st.title("Online Registration Form")
    st.subheader("Please fill out the form below to register.")

    # Input fields
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    age = st.number_input("Age", min_value=0, step=1)
    gender = st.radio("Gender", options=["Male", "Female", "Other"])
    agree = st.checkbox("I agree to the terms and conditions.")

    # Submit button
    if st.button("Submit"):
        if name and email and age and agree:
            st.success(f"Thank you for registering, {name}!")
        else:
            st.error("Please fill out all fields and agree to the terms.")

if __name__ == "__main__":
    main()
