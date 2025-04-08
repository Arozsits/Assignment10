# File Name : JSON.py
# Student Name: Ray Happel, Andrew Rozsits, Nate Hoang, Liam Vasey
# email:  happelrc@mail.uc.edu,
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, we are exeuting an API call using a specfic URL that we selected.

# Brief Description of what this module does. We are learning about how to incorporate API files to aggreagate data from JSON files.
# Citations:  https://realpython.com/python-json/ , https://requests.readthedocs.io/ , https://www.w3schools.com/python/pandas/pandas_csv.asp , https://opendata.cityofnewyork.us/


import requests
import json
import csv

class NYCDataFetcher:
    def __init__(self, url: str):  # The constructor
        """
        Initialize with the API URL
        @param url: The API endpoint where we will fetch the data from
        """
        self.url = url
        self.data = {}

    def fetch_data(self) -> dict: # Now we have a data dictionary
        """
        Fetches the data from the API and stores the JSON response
        @return: Parsed JSON data as a Python dictionary
        """
        response = requests.get(self.url) 
        response.raise_for_status() 
        self.data = response.json() 
        return self.data
    def extract_rows(self) -> list:
            """
            Extracts rows using column names from meta
            @return: List of dictionaries with selected column data
            """
            if not self.data:
                print("None")
                return []

            columns = self.data.get("meta", {}).get("view", {}).get("columns", [])
            rows = self.data.get("data", [])

            if not columns or not rows:
                print("None")
                return []

        
            column_names = [col["name"] for col in columns]
            print(f"Detected columns: {column_names[:5]}...")  

            extracted = []
            for row in rows:
            
                row_data = dict(zip(column_names, row))
                extracted.append(row_data)

            return extracted

    def save_to_csv(self, records: list, filename: str = "nyc_data.csv") -> None:
            """
            Saving the extracted records to a CSV file
            """
            if not records:
                print("None")
                return

            keys = records[0].keys()
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(records)

            print(f"Data successfully written to {filename}")



