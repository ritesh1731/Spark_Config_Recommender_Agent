import openai
from utils import get_openai_api_key

openai.api_key = get_openai_api_key()

SYSTEM_PROMPT = (
    "You are an AI assistant that recommends optimal Spark configuration parameters "
    "(driver/executor memory, executor cores, shuffle partitions, dynamic allocation settings) "
    "based on provided job metrics."
)

def generate_prompt(metrics: dict) -> str:
    lines = [SYSTEM_PROMPT, "", "Job Metrics:"]
    for k, v in metrics.items():
        lines.append(f"- {k}: {v}")
    lines.append("\nProvide a concise spark-submit parameter recommendation.")
    return "\n".join(lines)


def get_recommendation(metrics: dict) -> str:
    prompt = generate_prompt(metrics)
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return resp.choices[0].message.content.strip()
