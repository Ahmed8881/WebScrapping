import csv
import re
import threading
import time

from bs4 import BeautifulSoup
from PyQt6.QtCore import QObject, pyqtSignal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Scraper(QObject):
    progress = pyqtSignal(int)

    def __init__(self, pause_event, stop_event):
        super().__init__()
        self.pause_event = pause_event
        self.stop_event = stop_event

    def ScrapData(self):
        # service = Service(executable_path=r"H:\Setups\chromedriver-win64\chromedriver.exe")
        service = Service(
            executable_path=r"C:\Users\butta\chromedriver-win64\chromedriver-win64\chromedriver.exe"
        )

        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        driver = webdriver.Chrome(service=service, options=chrome_options)

        i = 1
        # make columns in data.csv file
        with open("data_ptr.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(
                [
                    "Organization Type",
                    "Title",
                    "Review",
                    "Organization",
                    "Description",
                    "Resource",
                    "Data Set",
                ]
            )

        while i <= 14360:
            if self.stop_event.is_set():
                print("Stopping the scraping process.")
                break

            if not self.pause_event.is_set():
                driver.implicitly_wait(10)
                if i % 100 == 0:
                    time.sleep(60)
                driver.get(f"https://catalog.data.gov/dataset/?page={i}")
                organization_types = []
                titles = []
                reviews = []
                organizations = []
                descriptions = []
                resources = []
                data_sets = []
                time.sleep(2)
                page = driver.page_source
                soup = BeautifulSoup(page, "html.parser")
                for element in soup.find_all("div", class_="dataset-content"):
                    organization_type_element = element.find(
                        "span", class_="organization-type"
                    )
                    organization_type = (
                        organization_type_element.text.strip()
                        if organization_type_element
                        else "district"
                    )
                    heading = element.find("h3", class_="dataset-heading")
                    title = heading.find("a").text.strip().replace("\n", " ")
                    title = re.sub(
                        " +", " ", title
                    )  # Replace multiple spaces with a single space
                    review_element = heading.find("span", class_="recent-views")
                    review = (
                        review_element.get("title").strip() if review_element else "0"
                    )

                    notes = element.find("div", class_="notes")
                    organization_element = notes.find(
                        "p", class_="dataset-organization"
                    )
                    organization = (
                        organization_element.text.strip()
                        if organization_element
                        else "no organization"
                    )

                    description_element = notes.find("div")
                    description = (
                        description_element.text.strip().replace("\n", " ")
                        if description_element
                        else "no description"
                    )
                    description = re.sub(
                        " +", " ", description
                    )  # Replace multiple spaces with a single space
                    dataset_resources_element = element.find(
                        "ul", class_="dataset-resources"
                    )

                    # Initialize variables to store the first resource and data set value
                    resource_text = "no resource"
                    data_set_text = "no data set"

                    # Find the first resource
                    if dataset_resources_element:
                        first_resource = dataset_resources_element.find(
                            "a", class_="label"
                        )
                        if first_resource:
                            resource_text = first_resource.text.strip()

                    # Find the data set value
                    first_data_set = element.find("a", class_="more")
                    if first_data_set:
                        data_set_text = first_data_set.text.strip()

                    resources.append(resource_text)
                    data_sets.append(data_set_text)

                    organization_types.append(organization_type)
                    titles.append(title)
                    reviews.append(review)
                    organizations.append(organization)
                    descriptions.append(description)
                    print(f"Page {i}: Collected data for title: {title}")

                with open(
                    "data_ptr.csv", mode="a", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                    for org_type, title, review, org, desc, res, ds in zip(
                        organization_types,
                        titles,
                        reviews,
                        organizations,
                        descriptions,
                        resources,
                        data_sets,
                    ):
                        writer.writerow([org_type, title, review, org, desc, res, ds])
                        print(f"Page {i}: Written data for title: {title}")

                self.progress.emit(int((i / 1350) * 100))  # Emit progress
                i += 1
            else:
                print("Paused")
                time.sleep(1)


def start_scraping():
    global pause_event, stop_event, scraping_thread, scraper
    pause_event = threading.Event()
    stop_event = threading.Event()
    scraper = Scraper(pause_event, stop_event)
    scraping_thread = threading.Thread(target=scraper.ScrapData)
    scraping_thread.start()


def pause_scraping():
    pause_event.set()
    print("Scraping paused.")


def resume_scraping():
    pause_event.clear()
    print("Scraping resumed.")


def stop_scraping():
    stop_event.set()
    scraping_thread.join()
    print("Scraping stopped.")
