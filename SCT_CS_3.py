import streamlit as st
import re

st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password", type="password")
check_button = st.button("Check")

def check_strength(password):
    criteria = {
        "At least 8 characters": len(password) >= 8,
        "Contains uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains number": bool(re.search(r"\d", password)),
        "Contains special character": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    return criteria

if check_button:
    if password.strip() == "":
        st.warning("Please enter a password first.")
    else:
        criteria = check_strength(password)
        strength = sum(criteria.values())

        st.subheader("Password Strength Analysis:")
        for requirement, met in criteria.items():
            if met:
                st.success(f"✔ {requirement}")
            else:
                st.error(f"❌ {requirement}")

        if strength == len(criteria):
            st.success("✅ Strong Password!")
        elif strength >= 3:
            st.warning("⚠ Medium Strength Password.")
        else:
            st.error("❌ Weak Password.")
