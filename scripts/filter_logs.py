import re

# Define the path to your Jenkins log file
log_file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\jenkins.log"

# Define log levels to filter (INFO, WARNING, SEVERE, etc.)
log_levels_to_filter = ["SEVERE", "WARNING", "ERROR"]

def filter_logs(log_file, levels):
    """Reads the log file and filters lines containing specified log levels."""
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if any(level in line for level in levels):
                    print(line.strip())  # Print only matching lines
    except FileNotFoundError:
        print("Log file not found. Ensure Jenkins logs are available at:", log_file)

if __name__ == "__main__":
    filter_logs(log_file_path, log_levels_to_filter)
