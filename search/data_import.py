# search/data_import.py
import csv
import os
from django.conf import settings
from search.models import Restaurant
import json


def get_aggregate_rating(json_text):
    try:
        data = json.loads(json_text)
        user_rating = data.get('user_rating', {})
        aggregate_rating = user_rating.get('aggregate_rating', '-1')
        return float(aggregate_rating)  # Convert to float if needed
    except (json.JSONDecodeError, TypeError):
        return -1

def populate_data():
    file_path = os.path.join(settings.BASE_DIR, 'restaurants_small.csv')
    print(f"Looking for file at: {file_path}")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating = get_aggregate_rating(row['full_details'])
            print(f"Aggregate Rating: {rating}")
            Restaurant.objects.create(
                name=row['name'],
                location=row['location'],
                items=row['items'],
                lat_long=row['lat_long'],
                full_details=row['full_details'],
                aggregate_rating=rating
            )
