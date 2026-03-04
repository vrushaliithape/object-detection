import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.title("YOLOv8 Cloud Object Detection")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    results = model(image)
    st.image(results[0].plot(), caption="Detected Image")
