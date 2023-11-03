def filter_vacancies(hh_vacancies, filter_words):
    filtered_vacancies = []
    for vacancy in hh_vacancies:
        for filter_word in filter_words:
            if filter_word in vacancy.profession:
                filtered_vacancies.append(vacancy)
                break
    return filtered_vacancies


class Vacancy:
    def __init__(self, profession: str, url: str, salary_min: int, salary_max: int, currency: str, requirement: str
                 ) -> None:
        self.profession = profession
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.currency = currency
        self.requirement = requirement