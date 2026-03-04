🚀 YOLOv8 Object Detection Web App

A Computer Vision web application built using Streamlit and Ultralytics YOLOv8 for real-time object detection on uploaded images.

**Live Demo:** [YOLOv8 Object Detection Web App](https://object-detection-injlzjdxwmceinnr5hbuj6.streamlit.app/)
📌 Project Overview

Upload an image and detect objects using a pre-trained YOLOv8 model.
Detected objects are displayed with bounding boxes and confidence scores in a clean web interface.

🧠 Tech Stack
Python,Streamlit,Ultralytics YOLOv8,OpenCV (Headless),Pillow,Torch

⚙️ CI/CD Integration (Jenkins)
- Configured a Jenkins pipeline to automatically build and run the project whenever changes are pushed to GitHub.
- Used SCM polling to trigger builds at regular intervals (no public webhook needed).
- Ensures latest code is tested and deployed automatically to Streamlit Cloud.

⚙️ Installation (Run Locally)
git clone https://github.com/vrushaliithape/object-detection.git
cd object-detection
pip install -r requirements.txt
streamlit run app.py

Open in browser at: http://localhost:8080

🌐 Deployment on Streamlit Cloud
Push project to GitHub
Go to Streamlit Cloud
Click New App, select your repository, and deploy
Dependencies from requirements.txt will be installed automatically.

📷 Features
✔ Upload images
✔ Detect multiple objects
✔ Display bounding boxes and confidence scores
✔ Clean, responsive interface
✔ Cloud deployment ready

🚀 Future Improvements
Live webcam detection
Video object detection
Confidence threshold slider
FastAPI backend deployment

👩‍💻 Author
Developed as a Computer Vision project using YOLOv8 and Streamlit Cloud.
