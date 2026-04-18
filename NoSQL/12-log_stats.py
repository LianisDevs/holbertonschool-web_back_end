#!/usr/bin/env python3
"""log_status module"""

from pymongo import MongoClient


def log_details():
    """
    provides stats about Nginx logs
    """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    total_logs = collection.count_documents({})
    print(total_logs, "logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print(status_count, "status check")


if __name__ == "__main__":
    log_details()
