
import streamlit as st
import pandas as pd

# Load dummy pincode data
data = pd.read_csv("pm25_pincode.csv")

st.title("PM2.5 Lookup by Pincode")

pincode = st.text_input("Enter your pincode", "110001")

if st.button("Check PM2.5"):
    if pincode in data["pincode"].astype(str).values:
        pm25 = data.loc[data["pincode"] == int(pincode), "pm25"].values[0]
        st.write(f"PM2.5 in your area: {pm25} µg/m³")
        
        # Safety warning
        if pm25 <= 60:
            st.success("Air Quality is GOOD ✅")
        elif pm25 <= 120:
            st.warning("Air Quality is MODERATE ⚠️")
        else:
            st.error("Air Quality is HAZARDOUS ❌")
    else:
        st.error("Pincode not found in database. Try another.")

st.markdown("---")
st.caption("Hackathon prototype by Nafisa Parveen 2025")






