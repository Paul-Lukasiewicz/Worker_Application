import os 
from dotenv import load_dotenv
import requests 

load_dotenv()

airtable_api_key = os.getenv("AIRTABLE_API_KEY")
airtable_base_id = os.getenv("AIRTABLE_BASE_ID")
airtable_intervention_table_id = os.getenv("AIRTABLE_INTERVENTION_TABLE_ID")



class Table:
    def __init__(self, base_id, table_id, api_key):
        self.base_id = base_id
        self.table_id = table_id
        self.api_key = api_key
        self.url = f"https://api.airtable.com/v0/{self.base_id}/{self.table_id}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_records(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.json()["records"]
        else:
            print(f"Error: {response.status_code}")
            return None

    def create_record(self, data):
        response = requests.post(self.url, headers=self.headers, json={"fields": data})
        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error: {response.status_code}")
            return None


# Example usage:
table = Table(airtable_base_id, airtable_intervention_table_id, airtable_api_key)


table.create_record({"Transcript":"intervention du XXX"})
# Get all records
records = table.get_records()
if records:
    for record in records:
        print(record["id"], record["fields"])
        

        


