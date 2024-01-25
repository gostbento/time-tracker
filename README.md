# time-tracker
absurdly simple terminal project time tracker 
Certainly! Here is a single copiable text block for your `README.md`:

```markdown
# Project Time Tracker

The Project Time Tracker is a simple command-line tool for tracking time spent on different projects. It allows you to start and stop tracking projects, close them, and provides a summary of the total hours worked, budget, and hourly rate for each project.

## Installation

1. **Download the Script:**
   Download the `time-tracker.py` script to your Ubuntu system.

2. **Ensure Python is Installed:**
   Make sure you have Python 3 installed on your system. You can install it using:
   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

3. **Make the Script Executable:**
   Make the script executable by running the following command in the script's directory:
   ```bash
   chmod +x time-tracker.py
   ```

4. **Create Logs Directory:**
   Ensure that the `Logs` directory exists in your home directory. If not, create it:
   ```bash
   mkdir ~/Logs
   ```

## Usage

The script supports the following commands:

- **Track a Project:**
  ```bash
  ./time-tracker.py track <project_name> --budget <budget_value>
  ```

- **Stop Tracking a Project:**
  ```bash
  ./time-tracker.py stop <project_name>
  ```

- **Close a Project:**
  ```bash
  ./time-tracker.py close <project_name>
  ```

- **Remove a Project:**
  ```bash
  ./time-tracker.py remove <project_name>
  ```

- **List Projects:**
  ```bash
  ./time-tracker.py list
  ```

- **Project Summary:**
  ```bash
  ./time-tracker.py summary
  ```

## Example Usage

1. Start tracking a project:
   ```bash
   ./time-tracker.py track project-1 --budget 100
   ```

2. Stop tracking the project:
   ```bash
   ./time-tracker.py stop project-1
   ```

3. Close the project:
   ```bash
   ./time-tracker.py close project-1
   ```

4. Remove the project:
   ```bash
   ./time-tracker.py remove project-1
   ```

5. List all projects:
   ```bash
   ./time-tracker.py list
   ```

6. Display project summary:
   ```bash
   ./time-tracker.py summary
   ```

Feel free to modify the script or adapt it to your specific needs.
```


