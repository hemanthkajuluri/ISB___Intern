import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

# Directory where you want to save the data
DATA_DIR = Path("C:\\Users\\Amarjeet\\Downloads\\Assignment-ISB\\States2")

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Set default download directory for Chrome
    prefs = {"download.default_directory": str(DATA_DIR)}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def navigate_to_report(driver, state, report_category, report_type):
    driver.get("https://micensus.gov.in/state-wise-reports")
    time.sleep(5)  # Wait for the page to load
    
    # Select the state
    select = Select(driver.find_element(By.ID, "edit-shs-term-node-tid-depth-1"))
    select.select_by_visible_text(state)
    time.sleep(2)  # Wait for the next dropdown to populate
    
    # Fix the report category to "Fifth MI Census (2013-14)"
    select = Select(driver.find_element(By.ID, "edit-shs-term-node-tid-depth-select-1"))
    select.select_by_visible_text("Fifth MI Census (2013-14)")
    time.sleep(2)  # Wait for the next dropdown to populate

    # Select the specific report type, e.g., "Dugwell"
    select = Select(driver.find_element(By.ID, "edit-shs-term-node-tid-depth-select-2"))
    select.select_by_visible_text(report_type)
    time.sleep(5)  # Wait for the reports to load
def download_pdfs(driver, state, report_category, report_type):
    # Correctly target PDF links based on the provided HTML structure
    pdf_links = driver.find_elements(By.CSS_SELECTOR, "ul.multi-list li.multi-row a")
    for link in pdf_links:
        pdf_url = link.get_attribute('href')
        pdf_name = pdf_url.split('/')[-1]
        # Print the PDF URL for verification
        print(f"Found PDF URL: {pdf_url}")
        print(f"Downloading: {pdf_name}")

        # Attempt to download the PDF file
        try:
            response = requests.get(pdf_url)
            if response.status_code == 200:
                report_path = DATA_DIR / state / report_category / report_type.replace(" ", "_")
                report_path.mkdir(parents=True, exist_ok=True)
                with open(report_path / pdf_name, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {pdf_name}")
            else:
                print(f"Failed to download {pdf_name}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error downloading {pdf_name}: {e}")
        
        # Sleep to be polite to the server
        time.sleep(1)


def main():
    driver = setup_driver()
    try:
        # All states from the provided HTML
        states = [
            "ANDAMAN & NICOBARS", "ANDHRA PRADESH", "ARUNACHAL PRADESH", "ASSAM", "BIHAR",
            "CHANDIGARH", "CHHATISGARH", "DADRA & NAGER HAVELI", "DELHI", "GOA",
            "GUJARAT", "HARYANA", "HIMACHAL PRADESH", "JAMMU & KASHMIR", "JHARKHAND",
            "KARNATAKA", "KERALA", "MADHYA PRADESH", "MAHARASHTRA", "MANIPUR",
            "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUDUCHERRY",
            "PUNJAB", "RAJASTHAN", "SIKKIM", "TAMIL NADU", "TELANGANA",
            "TRIPURA", "UTTAR PRADESH", "UTTARAKHAND", "WEST BENGAL"
        ]
        
        report_category = "Fifth MI Census (2013-14)"  # Fixed category

        # Specific report types related to Tubewells from the provided HTML
        report_types = [
            "Deep Tubewell", "Dugwell", "Medium Tubewell", "Shallow Tubewell"
        ]
        
        for state in states:
            for report_type in report_types:
                navigate_to_report(driver, state, report_category, report_type)
                download_pdfs(driver, state, report_category, report_type)
                print(f"Completed downloading {report_type} for {state} in the category {report_category}")
                time.sleep(10)  # Delay to avoid overwhelming the server
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

