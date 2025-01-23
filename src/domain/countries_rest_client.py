from abc import ABC, abstractmethod


class CountriesRestClient(ABC):
    @abstractmethod
    def find_countries_by_flag(self, max: int = 3) -> dict:
        raise NotImplementedError

    @abstractmethod
    def find_countries_by_capital(self, max: int = 3) -> dict:
        raise NotImplementedError
