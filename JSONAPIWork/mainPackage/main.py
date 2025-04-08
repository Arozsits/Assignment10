import json
import requests



from JSONPackage.JSON import NYCDataFetcher

    
def main():
    url = 'https://data.cityofnewyork.us/api/views/xeg4-ic28/rows.json?accessType=DOWNLOAD'
    fetcher = NYCDataFetcher(url)

    print("Fetching data from NYC API")
    fetcher.fetch_data()

    print("Extracting structured rows")
    extracted = fetcher.extract_rows()
    print(f"Number of records extracted: {len(extracted)}")

    # Show first few records
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