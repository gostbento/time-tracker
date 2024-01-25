#!/usr/bin/env python3

import os
import json
import argparse
from datetime import datetime

LOGS_DIR = os.path.expanduser("~/Logs/")
LOG_FILE = os.path.join(LOGS_DIR, "time_tracker_logs.json")

def ensure_logs_directory():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)

def load_logs():
    if not os.path.exists(LOG_FILE):
        return {}

    with open(LOG_FILE, 'r') as file:
        return json.load(file)

def save_logs(logs):
    ensure_logs_directory()
    with open(LOG_FILE, 'w') as file:
        json.dump(logs, file, indent=2)

def start_tracking(project_name, budget):
    logs = load_logs()
    if project_name in logs:
        logs[project_name]['intervals'].append({'start_time': str(datetime.now()), 'end_time': None})
        save_logs(logs)
        print(f"Resumed tracking project: {project_name}")
    else:
        logs[project_name] = {'intervals': [{'start_time': str(datetime.now()), 'end_time': None}], 'budget': budget}
        save_logs(logs)
        print(f"Started tracking project: {project_name} with a budget of ${budget}")

def stop_tracking(project_name):
    logs = load_logs()
    if project_name in logs and logs[project_name]['intervals'][-1]['end_time'] is None:
        logs[project_name]['intervals'][-1]['end_time'] = str(datetime.now())
        save_logs(logs)
        print(f"Stopped tracking project: {project_name}")
    else:
        print(f"Project {project_name} is not being tracked.")

def close_project(project_name):
    logs = load_logs()
    if project_name in logs:
        for interval in logs[project_name]['intervals']:
            if interval['end_time'] is None:
                interval['end_time'] = str(datetime.now())
        save_logs(logs)
        print(f"Closed project: {project_name}")
    else:
        print(f"Project {project_name} not found.")

def remove_project(project_name):
    logs = load_logs()
    if project_name in logs:
        del logs[project_name]
        save_logs(logs)
        print(f"Removed project: {project_name}")
    else:
        print(f"Project {project_name} not found.")

def list_projects():
    logs = load_logs()
    print("List of Projects:")
    for project, details in logs.items():
        status = "Open" if details['intervals'][-1]['end_time'] is None else "Closed"
        budget = details.get('budget', 'Not specified')
        print(f"{project}: {status}, Budget: ${budget}")

def project_summary():
    logs = load_logs()
    print("Project Summary:")
    for project, details in logs.items():
        total_duration = 0
        for interval in details['intervals']:
            start_time = datetime.strptime(interval['start_time'], "%Y-%m-%d %H:%M:%S.%f")
            end_time = datetime.strptime(interval['end_time'], "%Y-%m-%d %H:%M:%S.%f") if interval['end_time'] else datetime.now()
            total_duration += (end_time - start_time).total_seconds()
        total_hours_worked = total_duration / 3600
        budget = details.get('budget', 0)
        budget = budget if budget is not None else 0
        dollars_per_hour = budget / total_hours_worked if total_hours_worked > 0 else 0

        print(f"{project}: {details.get('project_name', '-----------')}")
        print(f"Budget: ${budget}")
        print(f"Total hours worked: {total_hours_worked:.2f}")
        print(f"Hourly rate: ${dollars_per_hour:.2f}\n")
    print()

# Entry point of the script
if __name__ == "__main__":
    ensure_logs_directory()

    parser = argparse.ArgumentParser(description="Project Time Tracker")
    parser.add_argument("command", choices=["track", "stop", "close", "remove", "list", "summary"], help="Command to execute")
    parser.add_argument("project_name", nargs="?", help="Name of the project")
    parser.add_argument("--budget", type=float, help="Budget for the project")

    args = parser.parse_args()

    if args.command == "track":
        start_tracking(args.project_name, args.budget)
    elif args.command == "stop":
        stop_tracking(args.project_name)
    elif args.command == "close":
        close_project(args.project_name)
    elif args.command == "remove":
        remove_project(args.project_name)
    elif args.command == "list":
        list_projects()
    elif args.command == "summary":
        project_summary()
