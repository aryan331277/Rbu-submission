import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import time

# Set page configuration
st.set_page_config(
    page_title="Health Analysis Portal",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        font-weight: 700;
        color: #000000;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #000000;
        text-align: center;
        margin-bottom: 3rem;
    }
    .card {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        transition: transform 0.3s;
        color: #000000;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .card-cancer {
        background-color: #F3F4F6;
        border-left: 5px solid #374151;
    }
    .card-mental {
        background-color: #F3F4F6;
        border-left: 5px solid #374151;
    }
    .center-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        color: #000000;
    }
    .result-container {
        margin-top: 2rem;
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #F3F4F6;
        color: #000000;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        text-align: center;
        padding: 1rem;
        background-color: #F9FAFB;
        font-size: 0.8rem;
        color: #000000;
    }
    .stButton button {
        background-color: #374151;
        color: white;
    }
    .stButton button:hover {
        background-color: #111827;
    }
    /* Change all text to black */
    p, h1, h2, h3, h4, h5, h6, div, span, label {
        color: #000000;
    }
    .stSlider label, .stFileUploader label {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 class='main-header'>Health Analysis Portal</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Early detection saves lives. Choose an analysis option below.</p>", unsafe_allow_html=True)

# Function for lung cancer detection
def process_lung_image(image):
    # This would contain the actual image processing and model prediction code
    # For demonstration, we'll simulate processing time and return a result
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    for i in range(100):
        progress_bar.progress(i + 1)
        status_text.text(f"Processing image: {i+1}%")
        time.sleep(0.02)
    
    status_text.text("Analysis complete!")
    time.sleep(1)
    status_text.empty()
    progress_bar.empty()
    
    # Simulated result
    result = {
        "prediction": "Suspicious nodule detected",
        "confidence": 0.87,
        "nodule_size": "8mm",
        "location": "Right upper lobe",
        "recommendations": "Follow-up CT scan recommended in 3 months. Consult with pulmonologist."
    }
    return result

# Function for mental health analysis
def process_mental_health(answers):
    # This would contain the actual processing of mental health questionnaire
    # For demonstration, we'll calculate a simple score
    score = sum(answers.values())
    max_score = len(answers) * 4  # Assuming each question has max score of 4
    percentage = (score / max_score) * 100
    
    if percentage < 30:
        result = {
            "status": "Low concern",
            "score": score,
            "interpretation": "Your responses suggest minimal mental health concerns at this time.",
            "recommendations": "Practice regular self-care and mindfulness. Reassess if symptoms change."
        }
    elif percentage < 60:
        result = {
            "status": "Moderate concern",
            "score": score,
            "interpretation": "Your responses indicate some mental health challenges that may benefit from attention.",
            "recommendations": "Consider speaking with a mental health professional for further assessment."
        }
    else:
        result = {
            "status": "High concern",
            "score": score,
            "interpretation": "Your responses suggest significant mental health challenges.",
            "recommendations": "We strongly recommend consulting with a mental health professional soon."
        }
    return result

# Main function to create the dual-button interface
def main():
    # Create two columns for the buttons
    col1, col2 = st.columns(2)
    
    # Lung Cancer Detection Card
    with col1:
        st.markdown("""
        <div class="card card-cancer">
            <div class="center-content">
                <h2>Lung Cancer Detection</h2>
                <p>Upload a chest CT scan or X-ray image for analysis using our AI-powered detection system.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Upload lung scan image", type=["jpg", "jpeg", "png", "dcm"], key="cancer_uploader")
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Analyze Image", key="cancer_button"):
                with st.spinner("Processing image..."):
                    result = process_lung_image(image)
                
                st.markdown("<div class='result-container'>", unsafe_allow_html=True)
                st.subheader("Analysis Results")
                st.write(f"**Classification:** {result['prediction']}")
                st.write(f"**Confidence Score:** {result['confidence']*100:.1f}%")
                st.write(f"**Nodule Size:** {result['nodule_size']}")
                st.write(f"**Location:** {result['location']}")
                st.write("**Recommendations:**")
                st.write(result['recommendations'])
                st.markdown("</div>", unsafe_allow_html=True)
                
                st.warning("⚠️ This is a demonstration only. Always consult with healthcare professionals for medical diagnoses.")
    
    # Mental Health Analysis Card
    with col2:
        st.markdown("""
        <div class="card card-mental">
            <div class="center-content">
                <h2>Mental Health Analysis</h2>
                <p>Complete a confidential questionnaire to receive insights about your mental wellbeing.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("Start Mental Health Assessment"):
            st.write("Please answer the following questions honestly. Rate each item on a scale of 0-4:")
            st.write("0 = Not at all, 1 = Several days, 2 = More than half the days, 3 = Nearly every day, 4 = Every day")
            
            questions = {
                "q1": "Little interest or pleasure in doing things",
                "q2": "Feeling down, depressed, or hopeless",
                "q3": "Trouble falling or staying asleep, or sleeping too much",
                "q4": "Feeling tired or having little energy",
                "q5": "Poor appetite or overeating",
                "q6": "Feeling bad about yourself or that you are a failure",
                "q7": "Trouble concentrating on things",
                "q8": "Moving or speaking slowly, or being fidgety/restless",
                "q9": "Thoughts that you would be better off dead or of hurting yourself"
            }
            
            answers = {}
            for key, question in questions.items():
                answers[key] = st.slider(question, 0, 4, 0, key=key)
            
            if st.button("Submit Assessment", key="mental_button"):
                with st.spinner("Processing responses..."):
                    result = process_mental_health(answers)
                
                st.markdown("<div class='result-container'>", unsafe_allow_html=True)
                st.subheader("Assessment Results")
                
                # Visual indicator of status (with black text)
                if result["status"] == "Low concern":
                    st.success(f"Status: {result['status']}")
                elif result["status"] == "Moderate concern":
                    st.warning(f"Status: {result['status']}")
                else:
                    st.error(f"Status: {result['status']}")
                
                st.write(f"**Interpretation:** {result['interpretation']}")
                st.write("**Recommendations:**")
                st.write(result['recommendations'])
                st.markdown("</div>", unsafe_allow_html=True)
                


if __name__ == "__main__":
    main()
