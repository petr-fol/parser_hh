from src.api_interfaces.api_interface import API
import requests
import json
import os

from src.vacancy import Vacancy


class SuperJobAPI(API):

    def __init__(self):
        pass

    def get_vacancies(self, key_word):
        api_url = "https://api.superjob.ru/2.0/vacancies/"
        api_token = os.getenv("sj_api")

        params = {"keyword": "python", "count": 1}
        headers = {"X-Api-App-Id": api_token}
        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")

        vacancies_data = response.json()["vacancies"]
        vacancies_list = []

        for v_json in vacancies_data:
            currency = v_json["salary"]["currency"]
            if currency == "RUR":
                currency = "RUB"

            vacancy = Vacancy(
                v_json["title"],
                f"https://www.superjob.ru/vakansii/{v_json['id']}.html",
                v_json["salary"]["min"],
                v_json["salary"]["max"],
                currency,
                v_json["requirement"]
            )

            # Добавляем данные в список в виде словаря
            vacancies_list.append({
                "profession": vacancy.profession,
                "url": vacancy.url,
                "salary_min": vacancy.salary_min,
                "salary_max": vacancy.salary_max,
                "currency": vacancy.currency,
                "requirement": vacancy.requirement
            })

        return vacancies_list

    def get_vacancies_by_salary(self, salary):
        pass
