import streamlit as st
import requests
import time

API = "http://localhost:8000"  # change to Render URL later

st.set_page_config(page_title="Sentinel Alpha", layout="centered")
st.title("📈 Sentinel Alpha — Crypto Signal Dashboard")

# Live price
price_data = requests.get(f"{API}/market/price").json()
st.metric(
    f"Live Price ({price_data['symbol']})",
    f"${price_data['price']:.2f}"
)

st.divider()

# Run model
if st.button("▶ Run Model"):
    requests.post(f"{API}/agent/step")

decision = requests.get(f"{API}/agent/decision").json()

st.subheader("🧠 Model Decision")

if decision["side"] == "BUY":
    st.success(f"🟢 BUY @ {decision['price']:.2f}")
elif decision["side"] == "SELL":
    st.error(f"🔴 SELL @ {decision['price']:.2f}")
else:
    st.info("⚪ HOLD")



st.divider()
st.caption("Demo mode • No real trading")

time.sleep(5)
st.rerun()
