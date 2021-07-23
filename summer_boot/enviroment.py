from abc import ABC, abstractmethod


class BaseEnvironment(ABC):

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...


class ApplicationEnvironment(BaseEnvironment):
    pass
