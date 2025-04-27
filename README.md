# Spark_Config_Recommender_Agent
An AI-driven agent that analyzes Spark event log files and provides optimized spark-submit configuration parameters (executor memory, cores, dynamic allocation settings, shuffle partitions, etc.) by leveraging an LLM.

## Prerequisites
- Python 3.8 or higher
- Java 8 or higher (for PySpark)
- Docker (optional, for containerized runs)
- An OpenAI API key

## Project Structure
project_root/
├── main.py              # Entry point: parses logs and prints recommendations
├── spark_log_parser.py  # Extracts metrics from Spark event JSON logs
├── recommender.py       # Queries the LLM for config suggestions
├── utils.py             # Loads environment variables (API key)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Container setup
├── .env                 # Holds OPENAI_API_KEY
└── README.md            # This file

## Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spark-config-recommender.git
   cd spark-config-recommender
