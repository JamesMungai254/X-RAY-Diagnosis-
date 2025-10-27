
# 🩺 AI-Powered Tuberculosis Detection Using Chest X-Ray Images

> **Empowering early diagnosis of Tuberculosis (TB) through Artificial Intelligence and Computer Vision.**

---

## 🧠 Overview

The **AI-Powered Tuberculosis Detection System** is a **Streamlit-based web application** that analyzes **chest X-ray images** to determine whether a patient shows signs of **Tuberculosis (TB)** or is **Normal**.  
It leverages **deep learning (PyTorch)** to assist medical practitioners and researchers in making faster, more reliable diagnostic decisions.

---

## 🌍 Purpose

Tuberculosis remains a significant global health concern, particularly in resource-limited areas.  
This project aims to:
- Support **AI-assisted medical screening**.
- Enhance **diagnostic accuracy**.
- Improve **accessibility** for healthcare institutions and research organizations.

---

## 🚀 Features

✅ **User-Friendly Interface** – Simple upload and prediction workflow.  
✅ **AI-Powered Analysis** – Uses a trained deep learning model built with PyTorch.  
✅ **Real-Time Prediction** – Classifies chest X-rays as **Tuberculosis** or **Normal**.  
✅ **Ethical & Secure** – Data privacy and responsible AI use emphasized.  
✅ **Professional Design** – Multi-page Streamlit UI (Home & Prediction Page).  

---

## 🏗️ Project Structure

```

tb_xray_app/
│
├── app.py                     # Main Streamlit application
├── model/
│   └── tb_model.pth           # Trained PyTorch TB detection model
├── images/
│   └── tb_banner.jpg          # Home page banner image
├── uploads/                   # Folder for temporarily storing uploaded X-rays
└── requirements.txt           # Python dependencies

````

---

## 🧩 Technologies Used

| Category | Tools |
|-----------|--------|
| **Frontend / UI** | Streamlit |
| **Modeling Framework** | PyTorch, TorchVision |
| **Image Processing** | Pillow |
| **Programming Language** | Python 3.x |
| **Environment** | Cross-platform (Windows, Linux, macOS) |

---

## ⚙️ Installation & Setup

Follow the steps below to run the app locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/tb-xray-prediction.git
cd tb-xray-prediction
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

### 4️⃣ Open in Browser

Once launched, open the link (usually `http://localhost:8501`) in your browser.

---

## 🧠 How It Works

1. Navigate to the **“Predict TB”** page.
2. Upload a **chest X-ray image** (`.jpg`, `.jpeg`, `.png`).
3. The app preprocesses the image and passes it to the **AI model**.
4. The model predicts whether the image indicates **Tuberculosis** or **Normal**.
5. The prediction result is displayed instantly.

---

## 🖼️ Interface Preview

### 🏠 Home Page

Displays project overview, purpose, and ethical disclaimer.

### 🔬 Prediction Page

Allows users to upload an image and view AI-generated predictions.

---

## 📜 Ethical Considerations

This system is intended **for research and educational purposes only**.
It is **not a substitute for professional medical diagnosis**.
All data should comply with **Kenya’s Data Protection Act (2019)** and related ethical guidelines on medical AI research.

---

## 👨‍⚕️ Contributors

| Name                           | Role                        |
| ------------------------------ | --------------------------- |
| **James Mungai**               | Lead Developer & Researcher |
| **Kaggle Community**           | Dataset Providers           |
| **OpenAI / PyTorch Tutorials** | Technical References        |

---

## 🔗 References

* [Tuberculosis Chest X-ray Dataset – Kaggle](https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset)
* [PyTorch: Build Model Tutorial](https://pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html)
* [PyTorch: Optimization Tutorial](https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
* [PyTorch: Save/Load Model Tutorial](https://pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html)

---

## 🧾 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this software with proper attribution.

---

## 💬 Acknowledgements

Special thanks to:

* **Healthcare professionals** contributing to TB research.
* **Kaggle data community** for open-access datasets.
* **AI researchers** advancing ethical medical imaging.

---

> 🩻 *"AI won’t replace doctors — but doctors who use AI will replace those who don’t."*


