from datetime import datetime
import re

def analyze_heartbeat_log(input_path, output_path):
    target_key = "Key TSTFEED0300|7E3E|0400"
    filtered_entries = []

    with open(input_path, "r") as file:
        for line in file:
            if target_key in line:
                match = re.search(r"Timestamp (\d{2}:\d{2}:\d{2})", line)
                if match:
                    time_obj = datetime.strptime(match.group(1), "%H:%M:%S")
                    filtered_entries.append((time_obj, line.strip()))

    filtered_entries.sort(reverse=True)

    log_lines = []
    for i in range(len(filtered_entries) - 1):
        t1, _ = filtered_entries[i]
        t2, _ = filtered_entries[i + 1]
        delta = (t1 - t2).total_seconds()

        if 31 < delta < 33:
            log_lines.append(f"{t1.strftime('%H:%M:%S')} WARNING Heartbeat interval {int(delta)}s\n")
        elif delta >= 33:
            log_lines.append(f"{t1.strftime('%H:%M:%S')} ERROR Heartbeat interval {int(delta)}s\n")

    with open(output_path, "w") as log_file:
        log_file.writelines(log_lines)

analyze_heartbeat_log("hblog.txt", "hb_test.log")
