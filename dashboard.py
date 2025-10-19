import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title(" MCA Insights Engine")
st.markdown("A demonstration of an automated system for tracking and analyzing corporate data.")

# --- Data Loading ---
# We define paths relative to the 'app' directory
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
MASTER_FILE = os.path.join(DATA_DIR, 'processed', 'master_day_2.csv')
CHANGES_FILE = os.path.join(DATA_DIR, 'logs', 'changes_day_2.json')
ENRICHED_FILE = os.path.join(DATA_DIR, 'enriched', 'enriched_data.csv')
SUMMARY_FILE = os.path.join(os.path.dirname(__file__), '..', 'daily_summary.txt')

try:
    master_df = pd.read_csv(MASTER_FILE)
    changes_df = pd.read_json(CHANGES_FILE)
    enriched_df = pd.read_csv(ENRICHED_FILE)
    with open(SUMMARY_FILE, 'r') as f:
        summary_text = f.read()
except FileNotFoundError as e:
    st.error(f" Critical Error: A data file was not found. Please ensure the project structure is correct. Missing file: {e.filename}")
    st.stop()


# --- AI Summary Section ---
st.header(" Daily AI-Powered Summary")
st.info("This summary is auto-generated to highlight the most important changes from the latest data update.")
st.text(summary_text)


# --- Main Data Exploration ---
st.header(" Explore Company Data")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Filters")
    # Filters
    state_filter = st.selectbox("Filter by State:", options=['All'] + sorted(list(master_df['STATE'].unique())))
    status_filter = st.selectbox("Filter by Status:", options=['All'] + sorted(list(master_df['STATUS'].unique())))

    # Apply filters
    filtered_df = master_df.copy()
    if state_filter != 'All':
        filtered_df = filtered_df[filtered_df['STATE'] == state_filter]
    if status_filter != 'All':
        filtered_df = filtered_df[filtered_df['STATUS'] == status_filter]

    st.metric("Total Companies Displayed", len(filtered_df))

with col2:
    st.subheader("Master Company Records (Day 2)")
    st.dataframe(filtered_df)


# --- Change Log & Enriched Data ---
st.header(" Daily Changes and Enriched Information")
tab1, tab2 = st.tabs(["Daily Change Log", "Enriched Company Data"])

with tab1:
    st.subheader("Log of All Detected Changes")
    st.dataframe(changes_df)

with tab2:
    st.subheader("Sample of Enriched Company Records")
    st.dataframe(enriched_df)


# --- Chatbot Simulation ---
st.header(" Chat with MCA Data (Demonstration)")
st.warning("This is a simple demo to show the concept. Only one question is programmed.", icon="⚠️")

user_question = st.text_input("Ask a question about the data:", "Show new incorporations in Tamil Nadu")

if st.button("Ask"):
    if "new incorporation" in user_question.lower() and "tamil nadu" in user_question.lower():
        st.success("Query understood! Fetching results...")
        # We are hardcoding the response based on our mock data!
        result_df = master_df[master_df['CIN'] == 'U15400TN2025PTC123456']
        st.dataframe(result_df)
    else:
        st.info("This is a demo. Please try the exact question: 'Show new incorporations in Tamil Nadu'")