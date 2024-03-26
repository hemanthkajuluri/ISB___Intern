# ISB___Intern

Task 1: Requirements

# Annual Survey of Industries Data Processing

This repository contains a Python script for processing data from the Annual Survey of Industries. The script transforms an Excel file into a CSV file with three columns: `characteristic`, `year`, and `value`.

## Installation

To use this script, you'll need Python installed on your machine along with the following Python packages:

- pandas
- openpyxl

You can install these packages by running:

```
pip install -r requirements.txt
```

## Usage

1. Place your Excel file in the same directory as the script or specify the path to the file in the script.
2. Run the script using Python:

```
python process_asi.py
```

3. The script will create a CSV file named `processed_asi_data.csv` in the same directory.
