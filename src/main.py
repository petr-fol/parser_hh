# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.api_interfaces.api_hh import HeadHunterAPI
from src.api_interfaces.api_sj import SuperJobAPI
from src.handlers.json_handler import JSONHandler
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
super_job_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
super_job_vacancies = super_job_api.get_vacancies("Python")

# Создание экземпляра класса для работы с вакансиями
vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", 100_000, 150_000, "RUR", "Требования: опыт "
                                                                                                 "работы от 3 лет...")

# Сохранение информации о вакансиях в файл
json_handler = JSONHandler()
json_handler.add_vacancy(vacancy)
json_handler.get_vacancies_by_salary(0, 100000)
json_handler.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем


def user_interface():
    # platforms = ["HeadHunter", "SuperJob"]
    # search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = json_handler.filter_vacancies(hh_vacancies, super_job_vacancies, filter_words)  # super_job_vacancies

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = json_handler.sort_vacancies(filtered_vacancies)
    top_vacancies = json_handler.get_top_vacancies(sorted_vacancies, top_n)
    json_handler.print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interface()
