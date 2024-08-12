from es_connection import client
import requests
import datetime

#######------------UNCOMMENT IF YOU WANT TO INDEX DATA--------------------#############
# print("Please enter the year you want to index papers = ")
# year = input()
# url = 'https://api.semanticscholar.org/graph/v1/paper/search/bulk?fields=title,url,authors&year=2024'

# # Directly define the API key (Reminder: Securely handle API keys in production environments)
# api_key = '9R0fPrNnJw3wfFjMYgH6q5p64QYxJnKZ7xfQ3uRE'  # Replace with the actual API key

# # Define headers with API key
# headers = {'x-api-key': api_key}

# # Send the API request
# response = requests.get(url, headers=headers)

# # Check response status
# if response.status_code == 200:
#    response_data = response.json()
#    # Process and print the response data as needed
#    data = response_data['data']
# else:
#    print(f"Request failed with status code {response.status_code}: {response.text}")
   
# def index_into_es(url, title, authors):
#     client.index(
#         index='academic',
#         document={
#             'url': url,
#             'title': title,
#             'authors' : authors,
#             'datetime' : datetime.datetime.now()
#     })
    
# for items in data:
#     index_into_es(items['url'], items['title'], [a['name'] for a in items['authors']])

print("thanks for running me")