import streamlit as st

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

st.title("🔐 Caesar Cipher Encryption & Decryption")
st.markdown("This app encrypts and decrypts messages using the **Caesar Cipher** algorithm.")

text = st.text_area("Enter your message:")
shift = st.number_input("Enter shift value:", min_value=1, max_value=25, value=3)
option = st.radio("Choose an operation:", ("Encrypt", "Decrypt"))

if st.button("Submit"):
    if option == "Encrypt":
        result = encrypt(text, shift)
        st.success(f"Encrypted Message: {result}")
    elif option == "Decrypt":
        result = decrypt(text, shift)
        st.success(f"Decrypted Message: {result}")
