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
time_of_day = st.selectbox(
"Time of day",
["Morning (7–10 AM)", "Afternoon (12–4 PM)", "Evening (6–9 PM)"]
)

st.divider()

aqi_data = {
    "Delhi": 180,
    "Bangalore": 90,
    "Kochi": 70
}

# City coordinates for map visualization
city_coordinates = {
"Delhi": {"lat": 28.6139, "lon": 77.2090},
"Bangalore": {"lat": 12.9716, "lon": 77.5946},
"Kochi": {"lat": 9.9312, "lon": 76.2673}
}    


city_baseline_factor = {
    "Delhi": 11.0,
    "Bangalore": 0.85,
    "Kochi": 0.75
}    
activity_factor = {
    "Walking": 1.2,
    "Cycling": 1.5,
    "Driving": 0.8
}
time_factor = {
"Morning (7–10 AM)": 1.3,
"Afternoon (12–4 PM)": 0.9,
"Evening (6–9 PM)": 1.1
}

if st.button("Calculate Exposure"):
    aqi = aqi_data[city]
    exposure_score = (
    aqi
    * (time_spent / 60)
    * activity_factor[activity]
    * time_factor[time_of_day]
    )


    st.subheader("Exposure Result")
    st.caption(
        "Exposure varies by time of the day due to traffic density and atmospheric conditions."
    )
    st.metric("Personal Exposure Score", round(exposure_score, 2))
    city_baseline_exposure = (
        aqi
        * (time_spent / 60)
        * city_baseline_factor[city]
    )

    st.divider()
    st.subheader("City-level Pollution Map")

    map_data = []

    for city_name, coords in city_coordinates.items():
        map_data.append({
            "lat": coords["lat"],
            "lon": coords["lon"],
            "aqi": aqi_data[city_name]
    })

    st.map(map_data)

    st.subheader("Personal vs City Exposure")

    st.write("**Your Personal Exposure:**", round(exposure_score, 2))
    st.write("**City Average Exposure:**", round(city_baseline_exposure, 2))

    difference = exposure_score - city_baseline_exposure
    percent_diff = (difference / city_baseline_exposure) * 100

    if difference > 0:
        st.warning(
            f"Your exposure is approximately {round(percent_diff, 1)}% higher than the city average."
        )
    else:
        st.success(
            f"Your exposure is approximately {abs(round(percent_diff, 1))}% lower than the city average."
        )


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
