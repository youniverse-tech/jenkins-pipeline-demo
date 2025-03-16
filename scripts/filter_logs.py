import re

# Define the path to your Jenkins log file
log_file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\jenkins.log"

# Define the output file where filtered logs will be stored
output_file_path = "C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Jenkins-Pipeline-Demo\\filtered_logs.txt"

# Define log levels to filter (INFO, WARNING, SEVERE, etc.)
log_levels_to_filter = ["SEVERE", "WARNING", "ERROR"]

def filter_logs(log_file, levels, output_file):
    """Reads the log file, filters lines containing specified log levels, and saves them to an output file."""
    try:
        with open(log_file, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as output:
            for line in file:
                if any(level in line for level in levels):
                    output.write(line)  # Write to file instead of print
        print("✅ Filtered logs saved in:", output_file)
    except FileNotFoundError:
        print("❌ Log file not found. Ensure Jenkins logs are available at:", log_file)

if __name__ == "__main__":
    print("🚀 Script started...")
    print("🔍 Executing filter_logs function...")
    filter_logs(log_file_path, log_levels_to_filter, output_file_path)
