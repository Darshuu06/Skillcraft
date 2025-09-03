import streamlit as st
from PIL import Image
import numpy as np

st.title("Image Encryption Tool - Pixel Manipulation")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

operation = st.selectbox("Choose Operation", [
    "Swap Red & Blue Channels",
    "Increase Brightness",
    "Decrease Brightness",
    "Invert Colors",
    "XOR with Value"
])

value = st.slider("Value (for Brightness/XOR)", 0, 255, 50)

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(img)

    if operation == "Swap Red & Blue Channels":
        img_array = img_array[:, :, [2, 1, 0]]
    elif operation == "Increase Brightness":
        img_array = np.clip(img_array + value, 0, 255)
    elif operation == "Decrease Brightness":
        img_array = np.clip(img_array - value, 0, 255)
    elif operation == "Invert Colors":
        img_array = 255 - img_array
    elif operation == "XOR with Value":
        img_array = img_array ^ value

    encrypted_img = Image.fromarray(np.uint8(img_array))
    st.image(encrypted_img, caption="Processed Image", use_column_width=True)

    st.download_button(
        label="Download Processed Image",
        data=encrypted_img.tobytes(),
        file_name="processed_image.png",
        mime="image/png"
    )
