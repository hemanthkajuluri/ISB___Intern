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
pip install pandas
pip install openpyxl
```

## Usage

1. Place your Excel file in the same directory as the script or specify the path to the file in the script.
2. Run the script using Python:

```
python process_asi.py
```

3. The script will create a CSV file named `processed_asi_data.csv` in the same directory.

#Task 2:


# Monthly Power Generation Data ETL Pipeline

This project is designed to fetch monthly power generation statistics from the Central Electricity Authority (CEA) and upload the structured data to an AWS S3 bucket.

## Prerequisites

- Python 3.x
- AWS Account
- S3 Bucket

## Setup and Installation

1. **Install Python Dependencies:**

```
pip install requests boto3 pandas
```

2. **Configure AWS Credentials:**

   It's crucial to configure your AWS credentials securely. Follow [AWS's guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) to set up your credentials file.
     'or'
It is required to install AWS CLI from its website and create a aws account.
You also need to configue aws access keys and create a s3 bucket 
After installing the aws cli.You need to add the aws cli to the environment Variables to path of your system variables.
Run aws configure on the terminal of your code.
Add the ACCESS_KEY_ID: from the access-key of your access points created in the terminal
Now you need to create a new bucket name here.
Add the bucket name into the code.

4. **Update the Script:**

   Edit `monthly_etl.py` to include your specific S3 bucket name in the `upload_to_s3` function call.

## Running the ETL Pipeline

Execute the script to run the ETL process:

```
python monthly_etl.py
```

The script will fetch the data from CEA's API, transform it into a structured format, and upload it as a CSV file to the specified S3 bucket.

#Task 3:
# 6th Minor Irrigation Census Report Downloader

This repository contains a Python script (`get_raw_data.py`) for automated downloading of reports from the 6th Minor Irrigation Census. The script navigates the official census website, selects specified states and report categories, and downloads the reports into a structured directory system based on state and report type.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system.
- Google Chrome installed on your system for Selenium to automate web navigation.
- ChromeDriver compatible with your version of Google Chrome. The `webdriver_manager` package used in the script will automatically manage this for you.

## Installation

Follow these steps to get your development environment set up:



1. **Install the required Python packages:**




    If you need to install the packages manually:

    ```bash
    pip install selenium webdriver_manager requests
    ```

## Usage

To run the script, execute the following command in your terminal:

```bash
python get_raw_data.py
```
Add changes to the location where file needs  to be saved



