# Spark_Config_Recommender_Agent
An AI-driven agent that analyzes Spark event log files and provides optimized spark-submit configuration parameters (executor memory, cores, dynamic allocation settings, shuffle partitions, etc.) by leveraging an LLM.

## Prerequisites
- Python 3.8 or higher
- Java 8 or higher (for PySpark)
- Docker (optional, for containerized runs)
- An OpenAI API key

## Project Structure
      project_root/
      ├── main.py
      ├── spark_log_parser.py
      ├── recommender.py
      ├── utils.py
      ├── requirements.txt
      ├── Dockerfile
      ├── .env
      └── README.md
## Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spark-config-recommender.git
   cd spark-config-recommender
2. **Configure your API key**
   Create a .env file at the project root:
    ```bash
    OPENAI_API_KEY=your_openai_api_key_here

3. Install dependencies
    ```bash
    pip install --no-cache-dir -r requirements.txt


4. Local Execution

Prepare a directory of Spark event logs (JSON format).

5. Run the agent:

python main.py --log-dir /path/to/your/spark/logs

The agent will display metrics and print recommended spark-submit flags.

6. Docker Execution

6.1. Build the image

docker build -t spark-recommender .

6.2. Run the container

docker run --env-file .env -v /path/to/logs:/logs spark-recommender

/logs in the container maps to your local log directory.
