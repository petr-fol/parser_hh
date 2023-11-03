import requests

from src.api_interface import API
from src.vacancy import Vacancy


class HeadHunterAPI(API):

    def __init__(self):
        pass

    def get_vacancies(self, key_word):
        response = requests.get(f'https://api.hh.ru/vacancies?text={key_word}&per_page=2000&page=1&order=salary_desc')
        vacancies = []
        for v_json in response.json()['items']:
            name = v_json[0]["name"]
            url = v_json[0]["alternate_url"]
            currency = v_json[0]["salary"]["currency"]
            requirement = v_json[0]["snippet"]["requirement"]

            if v_json[0]["salary"]["to"] != None:
                s_max = v_json[0]["salary"]["to"]
            else:
                s_max = None

            if v_json[0]["salary"]["from"] != None:
                s_min = v_json[0]["salary"]["from"]
            else:
                s_min = None

            vacancy = Vacancy(name, url, s_min, s_max, currency, requirement)
            vacancies.append(vacancy)
        return vacancies
