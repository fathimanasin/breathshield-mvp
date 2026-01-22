import streamlit as st

st.set_page_config(
    page_title="BreathShield MVP",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 BreathShield")
st.subheader("Personal Air Pollution Exposure – Proof of Concept")

st.markdown(
    """
    This MVP demonstrates how **personal exposure** to air pollution
    can be estimated using simple daily factors.
    """
)

st.divider()

st.header("Daily Exposure Dashboard")

city = st.selectbox(
    "Select your city",
    ["Delhi", "Bangalore", "Kochi"]
)

activity = st.selectbox(
    "Select your activity",
    ["Walking", "Cycling", "Driving"]
)

time_spent = st.slider(
    "Time spent outdoors / commuting (minutes)",
    5, 180, 30
)

st.divider()

aqi_data = {
    "Delhi": 180,
    "Bangalore": 90,
    "Kochi": 70
}

activity_factor = {
    "Walking": 1.2,
    "Cycling": 1.5,
    "Driving": 0.8
}

if st.button("Calculate Exposure"):
    aqi = aqi_data[city]
    exposure_score = aqi * (time_spent / 60) * activity_factor[activity]

    st.subheader("Exposure Result")
    st.metric("Personal Exposure Score", round(exposure_score, 2))

    if exposure_score < 100:
        st.success("Low risk – current choices are relatively safer.")
    elif exposure_score < 200:
        st.warning("Moderate risk – small changes can reduce exposure.")
    else:
        st.error("High risk – consider adjusting timing or route.")

    st.caption(
        "This is a relative exposure estimate for decision support, "
        "not a medical measurement."
    )
    # ----------------------------
    # Mock Historical Exposure Trend
    # ----------------------------
    st.subheader("Exposure Trend (Last 7 Days)")

    historical_exposure = [
    exposure_score * 0.6,
    exposure_score * 0.75,
    exposure_score * 0.8,
    exposure_score * 0.9,
    exposure_score * 1.0,
    exposure_score * 1.1,
    exposure_score * 1.05,
    ] 
    st.line_chart(historical_exposure)
