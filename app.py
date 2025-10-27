import streamlit as st
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# ---------------------------
# 🧠 MODEL LOADING
# ---------------------------
@st.cache_resource  # Cache the model so it doesn’t reload every time
def load_model():
    model_path = "model/best_model.pth"

    # Define model architecture
    model = models.resnet18(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 2)  # 2 classes: Normal, Tuberculosis

    # Load weights
    state_dict = torch.load(model_path, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    model.eval()
    return model


# ---------------------------
# 🔍 PREDICTION FUNCTION
# ---------------------------
def predict(image):
    model = load_model()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    image = image.convert('RGB')
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)

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
    Welcome to the **AI-Powered TB Detection System** — a deep learning web app that assists medical professionals in detecting **Tuberculosis (TB)** from **chest X-ray images**.

    ### 🌍 Purpose
    Early and accurate detection of TB can save lives.  
    This system leverages **Artificial Intelligence (AI)** and **Computer Vision** to:
    - Classify chest X-rays as either **Normal** or **Tuberculosis**.
    - Improve diagnostic speed and consistency.
    - Enhance accessibility, especially in **resource-limited areas**.

    ---
    ### 💡 How It Works
    1. Go to the **Prediction page** using the sidebar.  
    2. Upload a **chest X-ray image** (JPG, PNG).  
    3. The AI model analyzes the image in real-time and provides an instant result.
    ---
    """)

    banner_path = "images/tb_banner.webp"
    try:
        st.image(banner_path, use_container_width=True, caption="AI for Healthcare – Tuberculosis Detection")
    except Exception:
        st.warning("⚠️ Banner image not found. Please ensure 'images/tb_banner.webp' exists.")

    st.markdown("""
    ### 👨‍⚕️ Ethical Note
    This tool is intended for **research and educational purposes** and should not replace professional medical diagnosis.
    """)

# ---------------------------
# 🔬 PREDICTION PAGE
# ---------------------------
elif page == "🔬 Predict TB":
    st.title("🔬 Chest X-ray Tuberculosis Prediction")
    st.markdown("Upload a chest X-ray image below to let the AI model predict whether it indicates **Tuberculosis** or **Normal** lungs.")

    uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png","webp"])

    if uploaded_file is not None:
        # Read image directly from memory (no saving)
        image = Image.open(uploaded_file)

        # Display uploaded image
        st.image(image, caption="Uploaded Chest X-ray", use_container_width=True)

        # Predict Button
        if st.button("🧠 Predict TB"):
            with st.spinner("Analyzing X-ray image..."):
                result = predict(image)

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
💻 *AI-Powered Diagnostic Tool for Tuberculosis Detection*  
📧 **Contact:** [jamesmungai6303@gmail.com](mailto:jamesmungai6303@gmail.com)
""")