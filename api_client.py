import os
import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/todos"
OUTPUT_FILE = "frontend_feed.json"


def fetch_and_transform():
    token = os.getenv("API_TOKEN", "dev_token")
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "B1-AI-Pipeline/1.0",
    }

    try:
        response = requests.get(API_URL, headers=headers, timeout=5)
        response.raise_for_status()
        raw_data = response.json()

        if not isinstance(raw_data, list) or not raw_data:
            raise ValueError("Expected a non-empty list of tasks.")

        # Keep user 1's tasks and rename fields for the front end.
        cleaned_records = []
        for task in raw_data:
            if task["userId"] == 1:
                cleaned_records.append({
                    "task_id": task["id"],
                    "label": task["title"],
                    "is_done": task["completed"],
                })

        with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
            json.dump(cleaned_records, output, indent=2)

        print(f"Successfully exported {len(cleaned_records)} records to {OUTPUT_FILE}.")
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP ERROR: {e}")
    except Exception as e:
        print(f"UNEXPECTED ERROR: {e}")


if __name__ == "__main__":
    fetch_and_transform()
