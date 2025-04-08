# File Name : main.py
# Student Name: Ray Happel, Andrew Rozsits, Nate Hoang, Liam Vasey
# email:  happelrc@mail.uc.edu,
# Assignment Number: Assignment 10
# Due Date:   04/10/2025
# Course #/Section:   IS 4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  In this assignment, we are exeuting an API call using a specfic URL that we selected.

# Brief Description of what this module does. We are learning about how to incorporate API files to aggreagate data from JSON files.
# Citations: https://realpython.com/python-json/ , https://requests.readthedocs.io/ , https://www.w3schools.com/python/pandas/pandas_csv.asp , https://opendata.cityofnewyork.us/


import json
import requests

from JSONPackage.JSON import NYCDataFetcher

    
def main():
    url = 'https://data.cityofnewyork.us/api/views/xeg4-ic28/rows.json?accessType=DOWNLOAD'
    fetcher = NYCDataFetcher(url)

   
    fetcher.fetch_data()

    
    extracted = fetcher.extract_rows()
    print(f"Number of records extracted: {len(extracted)}")

    
    def pretty_print_record(record: dict):
        print(f"{record.get('Park Location', 'Unknown')} ({record.get('Borough Location', 'N/A')})")
        print(f"Week of {record.get('Week Start Date', 'N/A')} to {record.get('Week End Date', 'N/A')}")
        print(f"Sports: {record.get('Sports Played', 'None listed')}")
        print(f"Total Attendance: {record.get('Attendance Sum', '0')}")
        print(f"    - Sun: {record.get('Sunday\'s Attendance', '0')} | Mon: {record.get('Monday\'s Attendance', '0')} "
              f"| Tue: {record.get('Tuesday\'s Attendance', '0')} | Wed: {record.get('Wednesday\'s Attendance', '0')} "
              f"| Thu: {record.get('Thursday\'s Attendance', '0')} | Fri: {record.get('Friday\'s Attendance', '0')} "
              f"| Sat: {record.get('Saturday\'s Attendance', '0')}")
        print("-" * 50)


    for record in extracted[:5]:  
        pretty_print_record(record)

    print("Writing to CSV")
    fetcher.save_to_csv(extracted)

if __name__ == "__main__":
    main()