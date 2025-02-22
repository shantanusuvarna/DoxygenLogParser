import csv
import sys
import re

def parse_doxygen_log(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Line", "File", "Message"])
        
        for line in infile:
            match = re.match(r'(\d+): (\S+): (.*)', line)
            if match:
                writer.writerow(match.groups())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python log_parser.py <input_log_file> <output_csv_file>")
        sys.exit(1)
    parse_doxygen_log(sys.argv[1], sys.argv[2])