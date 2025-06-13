#!/usr/bin/python
import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder API and prints their titles.

    - Sends a GET request to the API.
    - Prints the status code of the response.
    - If successful (status code 200), parses the response as JSON.
    - Iterates through the list of posts and prints the title of each one.
    """
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder API and saves them to a CSV file.

    - Sends a GET request to the API.
    - If successful (status code 200), parses the response as JSON.
    - Extracts 'id', 'title', and 'body' from each post.
    - Writes the extracted data to 'posts.csv' using the csv module.
    """
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        data_to_save = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data_to_save:
                writer.writerow(row)

