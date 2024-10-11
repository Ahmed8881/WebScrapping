import asyncio
import csv
import logging
import os
import re

import pandas as pd
from bs4 import BeautifulSoup
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox  # Import QMessageBox
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize Selenium WebDriver (using Chrome in this example)
def get_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless")  # Run in headless mode (no browser UI)
    try:
        driver = webdriver.Chrome(options=options)
        return driver
    except WebDriverException as e:
        logging.error(f"Error initializing WebDriver: {e}")
        return None


# Check if an element has no children (i.e., it's a leaf node)
def is_leaf_node(element):
    return not element.findChildren()


# Function to scrape data from a given URL
async def scrape_data(url):
    driver = get_driver()
    if not driver:
        return None

    try:
        driver.get(url)
        await asyncio.sleep(2)  # Simulate async behavior
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except WebDriverException as e:
        logging.error(f"Error fetching the URL: {e}")
        return None
    finally:
        driver.quit()  # Close the Selenium browser

    # Dictionary to store scraped data by class name
    scraped_data = {}

    # Find all elements with a class attribute that contains the word 'container'
    containers = soup.find_all(
        class_=lambda class_name: class_name and "container" in class_name
    )
    for container in containers:
        # Find all elements with a class attribute that have no child elements (leaf nodes) within the container
        for element in container.find_all(class_=True):
            if is_leaf_node(element):
                class_name = " ".join(element["class"])  # Get class name(s)
                text = element.get_text(strip=True)  # Get text content

                # Append data to the corresponding class in the dictionary
                if class_name not in scraped_data:
                    scraped_data[class_name] = [text]
                else:
                    scraped_data[class_name].append(text)

    return scraped_data


# Save scraped data to a CSV file
def save_to_csv(data, output_filename="scraped_data.csv"):
    # Filter out empty values and replace with 0 if empty
    filtered_data = {
        k: [v if v else "0" for v in values] if values else ["0"]
        for k, values in data.items()
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in filtered_data.items()]))

    # Fill any NaN values with 0
    df = df.fillna("0")

    # Save DataFrame to CSV
    df.to_csv(output_filename, index=False)
    logging.info(f"Data saved to {output_filename}")
    QMessageBox.information(None, "Data Saved", f"Data saved to {output_filename}")


# Sanitize URL to create a valid file name
def sanitize_filename(url):
    return re.sub(r"[^\w\-_\. ]", "_", url)


# Main function to scrape and save
async def scrape_and_save(url, output_filename=None):
    logging.info(f"Scraping data from {url}")
    scraped_data = await scrape_data(url)

    # Generate a valid file name from the URL if not provided
    if not output_filename:
        sanitized_filename = sanitize_filename(url)
        output_filename = f"{sanitized_filename}_scraped.csv"

    # Check if data was found
    if scraped_data:
        save_to_csv(scraped_data, output_filename)
    else:
        logging.warning("No data found.")
        # show a message box
        QMessageBox.warning(None, "No Data Found", "No data found on the page.")

        # Save an empty CSV with a single 0
        save_to_csv({"NoData": ["0"]}, "no_data_found.csv")
