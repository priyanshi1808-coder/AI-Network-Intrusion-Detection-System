from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Network Traffic Dashboard",
    page_icon="🛡️",
    layout="wide",
)
st.sidebar.title("AI-NVDS")

st.sidebar.markdown("---")

st.sidebar.info("""
Project Features

✔ Deep Packet Inspection

✔ Machine Learning Detection

✔ Real-Time Monitoring

✔ Live Alerts

✔ Streamlit Dashboard
""")

st.sidebar.markdown("---")

st.sidebar.success("Status : Running")

st_autorefresh(interval=3000, key="refresh")

st.title("🛡 AI Network Intrusion Detection System")
from datetime import datetime

st.caption(f"🕒 Last Updated : {datetime.now().strftime('%H:%M:%S')}")

st.markdown(
    """
### Real-Time Deep Packet Inspection using Machine Learning
Monitor live network traffic, detect intrusions, and visualize security events in real time.
"""
)
st.markdown("---")

status1, status2, status3 = st.columns(3)

status1.success("🟢 AI Model : ACTIVE")
status2.success("📡 Packet Capture : RUNNING")
status3.success("🛡 Threat Detection : LIVE")

csv_file = "logs/alerts.csv"

if not os.path.exists(csv_file):
    st.warning("No alerts found.")
    st.stop()

df = pd.read_csv(csv_file)

if df.empty:
    st.warning("Alert file is empty.")
    st.stop()
    
total_flows = len(df)
benign = len(df[df["Prediction"] == "BENIGN"])
attacks = total_flows - benign

confidence = (
    df["Confidence"]
      .str.replace("%", "", regex=False)
      .astype(float)
      .mean()
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric("Total Flows", total_flows)
col2.metric("Benign", benign)
col3.metric("Attacks", attacks)
col4.metric("Avg Confidence", f"{confidence:.2f}%")
col5.metric("Active Devices", df["Source IP"].nunique())
col6.metric("🚨 Today's Alerts", len(df))

st.markdown("---")

st.subheader("🛡 Latest Detection")

latest = df.sort_values("Time", ascending=False).iloc[0]

c1, c2 = st.columns(2)

with c1:
    st.info(f"""
Prediction : **{latest['Prediction']}**

Protocol : **{latest['Protocol']}**

Confidence : **{latest['Confidence']}**

Severity : **{latest['Severity']}**
""")

with c2:
    st.info(f"""
Time : **{latest['Time']}**

Source : **{latest['Source IP']}**

Destination : **{latest['Destination IP']}**
""")

st.markdown("---")

st.subheader("📊 Network Statistics")

col1, col2, col3 = st.columns(3)

top_source = df["Source IP"].value_counts().idxmax()
top_destination = df["Destination IP"].value_counts().idxmax()
top_protocol = df["Protocol"].value_counts().idxmax()

col1.metric(
    "Most Active Source",
    top_source
)

col2.metric(
    "Most Contacted Server",
    top_destination
)

col3.metric(
    "Most Used Protocol",
    top_protocol
)

st.markdown("---")

st.subheader("🚨 Attack Statistics")

high = len(df[df["Severity"] == "High"])
medium = len(df[df["Severity"] == "Medium"])
low = len(df[df["Severity"] == "Low"])

c1, c2, c3 = st.columns(3)

c1.error(f"🔴 High Severity : {high}")
c2.warning(f"🟠 Medium Severity : {medium}")
c3.success(f"🟢 Low Severity : {low}")

st.markdown("---")

st.subheader("🛡 Network Health")

if attacks == 0:
    st.success("🟢 Network Status : HEALTHY")
elif attacks < 10:
    st.warning("🟡 Suspicious Activity Detected")
else:
    st.error("🔴 Network Under Attack")
    
st.info(f"📊 Total Alerts Logged : {len(df)}")

healthy = round((benign / total_flows) * 100, 2)

st.progress(healthy / 100)

st.caption(f"Overall Network Health : {healthy}%")

st.markdown("---")

st.subheader("🔎 Interactive Alert Filters")

col1, col2, col3 = st.columns(3)

protocol_filter = col1.selectbox(
    "Protocol",
    ["ALL"] + sorted(df["Protocol"].unique().tolist())
)

prediction_filter = col2.selectbox(
    "Prediction",
    ["ALL"] + sorted(df["Prediction"].unique().tolist())
)

ip_filter = col3.text_input("Search Source IP")

filtered_df = df.copy()

if protocol_filter != "ALL":
    filtered_df = filtered_df[
        filtered_df["Protocol"] == protocol_filter
    ]

if prediction_filter != "ALL":
    filtered_df = filtered_df[
        filtered_df["Prediction"] == prediction_filter
    ]

if ip_filter:
    filtered_df = filtered_df[
        filtered_df["Source IP"].str.contains(
            ip_filter,
            case=False
        )
    ]

st.subheader("🚨 Live Alert Log")

st.dataframe(
    filtered_df.sort_values("Time", ascending=False),
    width="stretch",

)

st.markdown("---")

st.subheader("📊 Prediction Distribution")

fig = px.pie(
    df,
    names="Prediction",
    title="Prediction Distribution",
    template="plotly_dark"
)

st.plotly_chart(
    fig,
    width="stretch",
    config={"displayModeBar": False}
)

st.markdown("---")

st.subheader("🌐 Top Source IP Addresses")

top_ips = (
    df["Source IP"]
    .value_counts()
    .reset_index()
)

top_ips.columns = ["Source IP", "Count"]

fig2 = px.bar(
    top_ips.head(10),
    x="Source IP",
    y="Count",
    title="Top 10 Source IPs",
    template="plotly_dark"
)

st.plotly_chart(
    fig2,
    width="stretch",
    config={"displayModeBar": False}
)

st.markdown("---")

st.subheader("📡 Protocol Distribution")

protocols = (
    df["Protocol"]
    .value_counts()
    .reset_index()
)

protocols.columns = ["Protocol", "Count"]

fig3 = px.bar(
    protocols,
    x="Protocol",
    y="Count",
    color="Protocol",
    title="Network Protocol Distribution",
    template="plotly_dark"
)

st.plotly_chart(
    fig3,
    width="stretch",
    config={"displayModeBar": False}
)

st.markdown("---")

st.subheader("🔥 Severity Distribution")

severity = (
    df["Severity"]
      .value_counts()
      .reset_index()
)

severity.columns = ["Severity", "Count"]

fig6 = px.bar(
    severity,
    x="Severity",
    y="Count",
    color="Severity",
    template="plotly_dark",
    title="Alert Severity Distribution"
)

st.plotly_chart(
    fig6,
    width="stretch",
    config={"displayModeBar": False}
)


st.markdown("---")

st.subheader("🎯 Top Destination IP Addresses")

top_dest = (
    df["Destination IP"]
      .value_counts()
      .reset_index()
)

top_dest.columns = ["Destination IP", "Count"]

fig4 = px.bar(
    top_dest.head(10),
    x="Destination IP",
    y="Count",
    color="Count",
    title="Top 10 Destination IPs",
    template="plotly_dark"
)

st.plotly_chart(
    fig4,
    width="stretch",
    config={"displayModeBar": False}
)

st.markdown("---")

st.subheader("📈 Live Traffic Timeline")

# Convert Time column to datetime
df["Time"] = pd.to_datetime(df["Time"])

# Count flows per minute
traffic = (
    df.groupby(df["Time"].dt.strftime("%H:%M"))
      .size()
      .reset_index(name="Flows")
)

fig5 = px.line(
    traffic,
    x="Time",
    y="Flows",
    markers=True,
    title="Network Traffic Over Time",
    template="plotly_dark"
)
st.plotly_chart(
    fig5,
    width="stretch",
    config={"displayModeBar": False}
)
st.markdown("---")

st.subheader("📥 Download Reports")

with open(csv_file, "rb") as file:

    st.download_button(
        label="📄 Download Alert Report (CSV)",
        data=file,
        file_name="AI_NVDS_Alerts.csv",
        mime="text/csv"
    )
    
st.markdown("---")

st.subheader("🤖 AI Security Recommendation")

if attacks == 0:

    st.success("""
✅ No malicious traffic detected.

Recommendations

• Continue monitoring network traffic.

• IDS model is functioning correctly.

• No immediate action required.
""")

else:

    st.error("""
⚠ Suspicious traffic detected.

Recommendations

• Investigate suspicious IP addresses.

• Block malicious connections if necessary.

• Review firewall and IDS logs.

• Perform packet analysis using Wireshark.
""")
    
st.markdown("---")

st.markdown("""
<center>

## 🛡 AI Network Intrusion Detection System

Developed by **Priyanshi Pandey**

B.Tech Artificial Intelligence & Machine Learning

### Tech Stack

🐍 Python • 📡 Scapy • 🤖 XGBoost

📊 Streamlit • 📈 Plotly • 🐼 Pandas

© 2026 AI-NVDS

</center>
""", unsafe_allow_html=True)
