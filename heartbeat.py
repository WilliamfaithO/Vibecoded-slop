import datetime

# This script just writes the current time to a file
now = datetime.datetime.now()
with open("pulse.txt", "a") as f:
    f.write(f"Vibe Check at: {now}\n")

    print(f"Heartbeat recorded at {now}")
    