import os
import json

def parse_event_logs(log_dir: str) -> list:
    """Parse all Spark event JSON files in a directory."""
    metrics_list = []
    for fname in os.listdir(log_dir):
        if fname.endswith(".json"):  # adjust if your logs use .inprogress or plain text
            path = os.path.join(log_dir, fname)
            with open(path, 'r') as f:
                metrics = parse_event_log(f)
                metrics_list.append(metrics)
    return metrics_list


def parse_event_log(fh) -> dict:
    """Extract key metrics from a single Spark event log."""
    total_input_bytes = 0
    total_shuffle_read = 0
    total_shuffle_write = 0
    for line in fh:
        event = json.loads(line)
        kind = event.get("Event")
        if kind == "SparkListenerEnvironmentUpdate":
            props = event.get("Spark Properties", [])
            for key, val in props:
                if key == 'spark.app.inputBytes':
                    total_input_bytes = int(val)
        elif kind == "SparkListenerStageCompleted":
            info = event.get("Stage Info", {})
            metrics = info.get("Stage Metrics", {})
            total_shuffle_read += metrics.get("shuffleReadMetrics", {}).get("remoteBytesRead", 0)
            total_shuffle_write += metrics.get("shuffleWriteMetrics", {}).get("bytesWritten", 0)
    return {
        "input_bytes": total_input_bytes,
        "shuffle_read_bytes": total_shuffle_read,
        "shuffle_write_bytes": total_shuffle_write
    }
