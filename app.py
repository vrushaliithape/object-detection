import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("YOLOv8 Cloud Object Detection")

# Use official pretrained model
model = YOLO("yolov8n.pt")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    results = model.predict(source=image)
    res_plotted = results[0].plot()

    st.image(res_plotted, caption="Detected Image")
