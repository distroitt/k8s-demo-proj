import datetime
import time

def main():
    now = datetime.datetime.now()
    print(f"Hello from Kubernetes CronJob! Current time: {now}")

if __name__ == "__main__":
    main()