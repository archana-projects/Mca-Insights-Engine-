# MCA Insights Engine: A Demonstration

This project is a working prototype of an automated system designed to track, enrich, and analyze corporate data from India's Ministry of Corporate Affairs (MCA). It demonstrates a complete data pipeline, from ingestion and change detection to a user-friendly query interface.

Given the time constraints, this repository serves as a "working proxy" that showcases the intended logic, architecture, and core functionalities using representative mock data.

## Project Architecture

The system is built on a four-stage pipeline:

1. **Data Integration & Normalization:** Consolidates state-wise MCA data into a single, clean master dataset. (Simulated in `data/processed/`)
2. **Change Detection:** Compares daily snapshots of the master data to log new incorporations, deregistrations, and field-level updates. (The output is simulated in `data/logs/`)
3. **Data Enrichment:** Augments company records with supplementary information (e.g., Sector, Directors) scraped from public sources. (The output is simulated in `data/enriched/`)
4. **Insight & Query Layer:** A Streamlit-based dashboard provides a user interface for search, visualization, and conversational queries using an AI chatbot demonstrator.

## How to Run the Demonstration

This project runs on pre-generated mock data to showcase the final user-facing application.

**Prerequisites:**

* Python 3.8+
* Git

**Setup Instructions:**

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/your-username/mca-insights-engine.git](https://github.com/your-username/mca-insights-engine.git)
   cd mca-insights-engine
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate
   ```
3. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit Dashboard:**

   ```bash
   cd app
   streamlit run dashboard.py
   ```

   The application will open in your web browser.

## Project Structure

```
mca_insights_engine/
|-- data/                 # Contains all mock data
|   |-- processed/        # Master datasets for two days
|   |-- logs/             # Generated change logs
|   |-- enriched/         # Enriched company data
|-- scripts/              # Skeleton scripts showing the backend logic
|-- app/                  # The Streamlit dashboard application
|-- README.md             # This file
|-- requirements.txt      # Python dependencies
|-- daily_summary.txt     # Sample AI-generated summary
```

## Logic and Implementation Notes

* **Change Detection Logic (`scripts/change_detection.py`):** This script contains placeholder logic that demonstrates how a comparison between two datasets (e.g., `master_day_1.csv` and `master_day_2.csv`) would be performed to generate a structured change log like `changes_day_2.json`.
* **AI Chatbot (in `app/dashboard.py`):** The chatbot is a functional demonstration. It uses simple string matching to answer a predefined question ("Show new incorporations in Tamil Nadu") to simulate how a real AI model would parse the query and filter the data.
