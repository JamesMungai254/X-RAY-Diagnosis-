import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import os

# ---------------------------
# 🧠 MODEL LOADING (Replace this part with your own)
# ---------------------------
def load_model():
    model_path = "model/best_model.pth"
    model = torch.load(model_path, map_location=torch.device('cpu'))
    model.eval()
    return model

def predict(image_path):
    model = load_model()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
    
    # Assuming class 1 = Tuberculosis, 0 = Normal
    return 'Tuberculosis' if predicted.item() == 1 else 'Normal'


# ---------------------------
# 🧭 STREAMLIT PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI-Powered TB Detection",
    page_icon="🩻",
    layout="wide",
)

# ---------------------------
# 💎 SIDEBAR NAVIGATION
# ---------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🔬 Predict TB"])

# ---------------------------
# 🏠 HOME PAGE
# ---------------------------
if page == "🏠 Home":
    st.title("🩺 AI-Powered Tuberculosis Detection")
    st.markdown("""
    Welcome to the **AI-Powered TB Detection System** — a deep learning application designed to assist medical professionals in detecting **tuberculosis (TB)** from **chest X-ray images**.

    ### 🌍 Purpose
    Early and accurate detection of TB can save lives.  
    This system leverages **Artificial Intelligence (AI)** and **Computer Vision** to:
    - Classify chest X-rays as either **Normal** or **Tuberculosis**.
    - Help improve diagnostic speed and consistency.
    - Support healthcare accessibility, especially in **resource-limited areas**.

    ---
    ### 💡 How it works
    1. Go to the **Prediction page** from the sidebar.  
    2. Upload a **chest X-ray image** (JPG, PNG).  
    3. The AI model analyzes and gives a prediction instantly.
    ---
    """)

    st.image("images/tb_banner.jpg", use_container_width=True, caption="AI for Healthcare – Tuberculosis Detection")

    st.markdown("""
    ### 👨‍⚕️ Ethical Note
    This tool is for **research and educational purposes** and should not replace professional medical diagnosis.
    """)

# ---------------------------
# 🔬 PREDICTION PAGE
# ---------------------------
elif page == "🔬 Predict TB":
    st.title("🔬 Chest X-ray Tuberculosis Prediction")
    st.markdown("Upload a chest X-ray image below and let the AI model predict if it indicates **Tuberculosis** or **Normal** lungs.")

    uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save temporarily
        save_dir = "uploads"
        os.makedirs(save_dir, exist_ok=True)
        image_path = os.path.join(save_dir, uploaded_file.name)

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display the uploaded image
        st.image(image_path, caption="Uploaded Chest X-ray", use_container_width=True)

        # Predict Button
        if st.button("🧠 Predict TB"):
            with st.spinner("Analyzing X-ray image..."):
                result = predict(image_path)
            
            st.success(f"✅ Prediction Result: **{result}**")

            if result == "Tuberculosis":
                st.error("⚠️ The image shows signs of **Tuberculosis**. Please consult a healthcare provider.")
            else:
                st.info("✅ The image appears **Normal**. No TB detected.")
    else:
        st.info("Please upload a chest X-ray image to proceed.")

# ---------------------------
# ✉️ FOOTER
# ---------------------------
st.markdown("""
---
📘 **Developed by:** *James Mungai*  
💻 *AI-Powered Diagnostic Tool for Tuberculosis Detection in Kenya*  
""")
