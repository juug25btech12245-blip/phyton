import json
from collections import Counter

logs = [
    {"time": "10:00:01", "level": "INFO", "service": "auth", "message": "Login success"},
    {"time": "10:05:12", "level": "ERROR", "service": "db", "message": "Connection failed"},
    {"time": "10:10:45", "level": "WARNING", "service": "api", "message": "Slow response"},
    {"time": "10:15:30", "level": "ERROR", "service": "db", "message": "Timeout"},
    {"time": "10:20:11", "level": "INFO", "service": "api", "message": "Request served"},
]
with open("logs.json", "w") as f:
    json.dump(logs, f, indent=4)

try:
    with open("logs.json") as f:
        data = json.load(f)

    level_count = Counter(entry["level"] for entry in data)
    service_errors = Counter(e["service"] for e in data if e["level"] == "ERROR")

    print("Total entries:", len(data))
    print("Count by level:", dict(level_count))
    print("Errors by service:", dict(service_errors))

    print("\nError details:")
    for e in data:
        if e["level"] == "ERROR":
            print(f"  [{e['time']}] {e['service']}: {e['message']}")

    report = {
        "total": len(data),
        "by_level": dict(level_count),
        "errors_by_service": dict(service_errors),
    }
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)
    print("\nReport saved to report.json")

except FileNotFoundError:
    print("logs.json not found.")
except json.JSONDecodeError:
    print("Invalid JSON format.")
