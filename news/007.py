import requests
from bs4 import BeautifulSoup

url = 'https://abcnews.go.com/US/extreme-weather-east-coast-multiple-storms-move-region/story?id=106220838'


def get_all_content(url):
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_elements = soup.find_all(class_="gnt_ar_b_p")
        content = '\n'.join([text.get_text() for text in text_elements])
        print(content)
        return content
    return 'No more content'


get_all_content(url)
