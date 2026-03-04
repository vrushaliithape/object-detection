import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.title("YOLOv8 Cloud Object Detection")

@st.cache_resource
def load_model():
    return YOLO("best.pt")   # use your trained model

model = load_model()

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    results = model.predict(source=image)
    res_plotted = results[0].plot()

    st.image(res_plotted, caption="Detected Image")
