# Create a sample log file
with open("app.log", "w") as f:
    f.writelines([
        "2026-11-01 10:00:01 INFO Server started\n",
        "2026-11-01 10:05:12 WARNING Disk usage high\n",
        "2026-11-01 10:10:45 ERROR Database connection failed\n",
        "2026-11-01 10:15:30 INFO User login successful\n",
        "2026-11-01 10:20:11 ERROR Timeout occurred\n",
    ])

try:
    with open("app.log", "r") as f:
        print("First line:", f.readline().strip())
        print("\nRemaining lines:")
        counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
        for line in f:
            print(line.strip())
            for level in counts:
                if level in line:
                    counts[level] += 1
    print("\nSummary:", counts)

    print("\nError lines only:")
    with open("app.log") as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())
except FileNotFoundError:
    print("Log file not found.")
except Exception as e:
    print("Error:", e)
finally:
    print("Log reading finished.")
