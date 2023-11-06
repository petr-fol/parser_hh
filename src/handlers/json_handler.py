from src.handlers.handler import Saver

import json


class JSONHandler(Saver):
    def __init__(self):
        pass

    @staticmethod
    def add_vacancy(vacancy):
        with open("vacancies.json", 'r+', encoding="utf-8") as f:
            try:
                # парсинг JSON из файла
                data = json.load(f)
            except json.JSONDecodeError:
                # Если файл пустой или имеет неправильный формат:
                data = []

            # новый словарь к объекту данных
            new_vacancy = {
                "profession": vacancy.profession,
                "url": vacancy.url,
                "salary_min": vacancy.salary_min,
                "salary_max": vacancy.salary_max,
                "currency": vacancy.currency,
                "requirement": vacancy.requirement
            }

            data.append(new_vacancy)

            f.seek(0)
            f.truncate()  # Очистить файл
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def get_vacancies_by_salary(salary_min=0, salary_max=185_310_000,
                                currency='RUB', reverse=False):  # макс зп взята из гугла
        with open('vacancies.json', 'r') as f:
            data = json.load(f)
            vacancies = []
            for vacancy in data:
                if vacancy["salary_min"] <= salary_min and vacancy["salary_max"] >= salary_max and vacancy["currency"] == currency:
                    vacancies.append(vacancy)
            sorted(vacancies, key=lambda x: x["salary_min"], reverse=reverse)
        return vacancies

    @staticmethod
    def delete_vacancy(url):
        with open('vacancies.json', 'r+') as f:
            data = json.load(f)
            for vacancy in data:
                if vacancy["url"] == url:
                    data.remove(vacancy)
                    break

            f.seek(0)
        print(f"успешно удалено из 'vacancies.json' -> {url}")

    @staticmethod
    def filter_vacancies(hh_vacancies, super_job_vacancies, filter_words):
        filtered_vacancies = []
        for vacancy in hh_vacancies:
            for filter_word in filter_words:
                if filter_word in vacancy.profession:
                    filtered_vacancies.append(vacancy)
                    break
        for vacancy in super_job_vacancies:
            for filter_word in filter_words:
                if filter_word in vacancy.profession:
                    filtered_vacancies.append(vacancy)
                    break
        return filtered_vacancies

    @staticmethod
    def sort_vacancies(filtered_v):
        sorted(filtered_v, key=lambda x: x["profession"])
        return filtered_v

    @staticmethod
    def get_top_vacancies(sorted_vacancies, top_n):
        while len(sorted_vacancies) > top_n:
            sorted_vacancies.pop()
        return sorted_vacancies

    @staticmethod
    def print_vacancies(sorted_vacancies):
        print(f"Всего вакансий {len(sorted_vacancies)}")
        for vacancy in sorted_vacancies:

            if vacancy["salary_min"] is None:
                vacancy["salary_min"] = ""
            else:
                vacancy["salary_min"] = f"от {vacancy['salary_min']}"
            if vacancy["salary_max"] is None:
                vacancy["salary_max"] = ""
            if vacancy["currency"] == "RUB":
                vacancy["currency"] = "в рублях"

            print(f"{vacancy['profession']} {vacancy['salary_min']} до {vacancy['salary_max']} {vacancy['currency']}"
                  f"\n{vacancy['currency']}")
