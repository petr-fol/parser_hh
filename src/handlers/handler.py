from abc import ABC, abstractmethod


class Saver(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, profession):
        pass
