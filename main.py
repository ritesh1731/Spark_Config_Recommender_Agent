import argparse
from spark_log_parser import parse_event_logs
from recommender import get_recommendation


def main():
    parser = argparse.ArgumentParser(description="Spark Config Recommender Agent")
    parser.add_argument("--log-dir", required=True, help="Path to Spark event log JSON files")
    args = parser.parse_args()

    metrics_list = parse_event_logs(args.log_dir)
    for idx, metrics in enumerate(metrics_list, start=1):
        print(f"\n=== Job {idx} Metrics ===")
        for k, v in metrics.items(): print(f"{k}: {v}")
        print("\nRecommended spark-submit parameters:")
        print(get_recommendation(metrics))
        print("\n" + "-"*40)

if __name__ == "__main__":
    main()
