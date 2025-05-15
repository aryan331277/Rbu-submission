import streamlit as st

# Page configuration
st.set_page_config(
    page_title="EDF Predictor",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit menu and footer for a cleaner look
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .edf-card {
        padding: 1.5rem;
        border-radius: 1rem;
        background: #f7f9fc;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .edf-button {
        margin-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.markdown(
    "<div class='edf-card'>"
    "<h1 style='text-align: center;'>🍏 EDF File Predictor</h1>"
    "<p style='text-align: center; color: #555;'>Upload any file and see the magic happen!</p>"
    "</div>",
    unsafe_allow_html=True
)

# File uploader accepting any type
uploaded_file = st.file_uploader(
    label="Choose a file (any type)",
    type=None,  # Accept any file type
    help="Supported: EDF files and more"
)

# When a file is uploaded
if uploaded_file:
    ext = uploaded_file.name.lower().split('.')[-1]
    if ext == 'edf':
        st.success("✅ EDF file accepted!")
    else:
        st.info(f"📂 File '{uploaded_file.name}' uploaded (not EDF).")

    # Centered button for prediction
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        predict = st.button("🎯 Predict Word", key="predict", help="Click to get your prediction")

    # Display prediction
    if predict:
        # Dummy prediction logic
        predicted_word = "apple"
        st.balloons()
        st.markdown(
            f"<div class='edf-card' style='background: #e6ffed;'>"
            f"<h2 style='text-align: center; color: #2e7d32;'>Prediction: <strong>{predicted_word}</strong></h2>"
            f"</div>",
            unsafe_allow_html=True
        )
