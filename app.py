import streamlit as st
import numpy as np
import joblib
import plotly.express as px
import pandas as pd

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Page config
st.set_page_config(page_title="💓 Heart Disease Predictor", layout="centered")
st.markdown("<h1 style='text-align: center; color: crimson;'>Heart Disease Prediction App</h1>", unsafe_allow_html=True)
st.markdown("### 🧾 Enter Patient Health Details:")

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("🎂 Age", min_value=1, max_value=100, value=45)
    sex = st.radio("⚧️ Sex", ("Male", "Female"))

    cp_display = {
        "Typical Angina (0)": 0,
        "Atypical Angina (1)": 1,
        "Non-anginal Pain (2)": 2,
        "Asymptomatic (3)": 3
    }
    cp = st.selectbox("💢 Chest Pain Type", list(cp_display.keys()))

    trestbps = st.slider("🩺 Resting BP (mm Hg)", 80, 200, 120)
    chol = st.slider("🧪 Serum Cholesterol (mg/dl)", 100, 400, 200)

    fbs = st.radio("🍬 Fasting Blood Sugar > 120 mg/dl", ("False", "True"))

with col2:
    restecg_display = {
        "Normal (0)": 0,
        "ST-T Abnormality (1)": 1,
        "LVH (2)": 2
    }
    restecg = st.selectbox("📈 Resting ECG", list(restecg_display.keys()))

    thalach = st.slider("🏃 Max Heart Rate Achieved", 70, 220, 150)
    exang = st.radio("🏋️ Exercise Induced Angina", ("No", "Yes"))
    oldpeak = st.slider("📉 ST Depression (Oldpeak)", 0.0, 6.0, 1.0)

    slope_display = {
        "Upsloping (0)": 0,
        "Flat (1)": 1,
        "Downsloping (2)": 2
    }
    slope = st.selectbox("⛰️ Slope of ST Segment", list(slope_display.keys()))

    ca = st.selectbox("🩻 Major Vessels (0–4)", [0, 1, 2, 3, 4])

    thal_display = {
        "Normal (1)": 1,
        "Fixed Defect (2)": 2,
        "Reversible Defect (3)": 3
    }
    thal = st.selectbox("🧬 Thalassemia Type", list(thal_display.keys()))

# Predict button
if st.button("🧠 Predict Heart Disease Risk"):
    sex_val = 1 if sex == "Male" else 0
    fbs_val = 1 if fbs == "True" else 0
    exang_val = 1 if exang == "Yes" else 0

    input_data = np.array([[age, sex_val, cp_display[cp], trestbps, chol, fbs_val,
                            restecg_display[restecg], thalach, exang_val, oldpeak,
                            slope_display[slope], ca, thal_display[thal]]])

    prediction = model.predict(input_data)[0]
    result = "✅ No Heart Disease" if prediction == 0 else "⚠️ Risk of Heart Disease"
    st.subheader("🔍 Prediction Result:")
    st.success(result if prediction == 0 else result)

    # Dataframe for visualization
    labels = ['Age', 'Resting BP', 'Cholesterol', 'Max HR', 'Oldpeak']
    values = [age, trestbps, chol, thalach, oldpeak]
    df_viz = pd.DataFrame({'Health Metrics': labels, 'Value': values})

    fig = px.pie(df_viz, names='Health Metrics', values='Value',
                 title="🧠 Health Metrics Overview", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

    # Radar chart
    import plotly.graph_objects as go
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        name='Patient Profile'
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True)),
                            showlegend=False,
                            title="🛡️ Health Risk Radar")
    st.plotly_chart(fig_radar, use_container_width=True)
