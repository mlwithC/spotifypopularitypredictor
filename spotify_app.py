import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('random_forest_model.pkl')

# Title
st.title("🎵 Spotify Popularity Predictor")

# Option to choose input mode
input_mode = st.radio("Choose Input Mode:", ['Custom Input', 'Popular Example', 'Not Popular Example'])

# Define 14 feature names
feature_names = [
    'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'explicit'
]

# Define inputs based on the selected mode
if input_mode == 'Custom Input':
    st.subheader("🎛️ Enter Track Features")
    input_data = []
    for feature in feature_names:
        value = st.number_input(f"{feature}", value=0.0, format="%.4f")
        input_data.append(value)
elif input_mode == 'Popular Example':
    input_data = [
        0.7, 0.85, 5, -4.5, 1, 0.05, 0.1,
        0.0, 0.12, 0.9, 120.0, 210000, 4, 0
    ]  # Values typical of a popular track
    st.success("✅ Using a predefined popular song feature set.")
elif input_mode == 'Not Popular Example':
    input_data = [
        0.2, 0.3, 2, -15.0, 0, 0.4, 0.8,
        0.7, 0.5, 0.2, 85.0, 150000, 3, 0
    ]  # Values typical of a less popular song
    st.warning("⚠️ Using a predefined not-popular song feature set.")

# Prediction button
if st.button("Predict Popularity"):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        st.markdown("🎉 **Prediction: Popular Track!**")
    else:
        st.markdown("🙁 **Prediction: Not Popular Track.**")
