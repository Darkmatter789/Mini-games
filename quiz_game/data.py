# import urllib.request, urllib.parse, urllib.error
# import json
import ssl
import requests


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_data():
    question_data = []
    params = {
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
}
    response = requests.get("https://opentdb.com/api.php", params=params)
    response.raise_for_status()
    data = response.json()
    for items in data['results']:
        question_data.append(items)
    print(question_data)
    return question_data

# def get_difficulty():
#     diff_setting = input("How difficult would like the questions to be? (easy/hard/expert): ").lower()
#     if diff_setting == 'easy':
#         url = 'https://opentdb.com/api.php?amount=20&difficulty=easy&type=boolean'
#     elif diff_setting == 'hard':
#         url = 'https://opentdb.com/api.php?amount=20&difficulty=medium&type=boolean'
#     elif diff_setting == 'expert':
#         url = 'https://opentdb.com/api.php?amount=20&difficulty=hard&type=boolean'
#     return url

# url = get_difficulty()

# data = urllib.request.urlopen(url, context=ctx).read().decode()
# js = json.loads(data)

# question_data = []

# for items in js['results']:
#     question_data.append(items)

