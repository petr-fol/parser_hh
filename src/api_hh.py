import requests

from src.api_interface import API


class HeadHunterAPI(API):

    def __init__(self):
        pass

    def get_vacancies(self, key_word):
        response = requests.get(f'https://api.hh.ru/vacancies?text={key_word}&per_page=1&page=1&order=salary_desc')
        return response
