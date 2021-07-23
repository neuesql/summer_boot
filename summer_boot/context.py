from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import List, Optional, Dict, Type

from summer_boot.enviroment import ApplicationEnvironment


class LifeCycle(ABC):

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...

    @abstractmethod
    def refresh(self):
        ...

    @abstractmethod
    def is_running(self) -> bool:
        ...


class ApplicationEventPublisher(ABC):

    @abstractmethod
    def publish_event(self, event: object) -> None:
        ...

    @abstractmethod
    def publish_event_sync(self, event: object) -> None:
        self.publish_event(event)

    @abstractmethod
    def publish_event_async(self, event: object) -> None:
        ...


class AbstractBeanContext(LifeCycle, ApplicationEventPublisher):

    def __init__(self):
        self.__initializing: bool = False
        self.__running: bool = False
        self.__terminating: bool = False

        self.__singleton_objects: Dict[Type, object] = {}
        self.__providers: List[Type] = []

    @abstractmethod
    def create_bean(self, class_type: Type):
        ...

    @abstractmethod
    def destroy_bean(self, class_type: Type):
        ...

    @abstractmethod
    def refresh_bean(self, class_type: Type):
        ...

    @abstractmethod
    def get_bean(self, class_type: Type) -> Optional[object]:
        ...

    @abstractmethod
    def get_bean(self, name: str, class_type: Type) -> Optional[object]:
        ...

    @abstractmethod
    def get_beans(self, class_type: Type) -> List[object]:
        ...


class ApplicationContext(AbstractBeanContext):

    def __init__(self):
        self.__packages: List = []
        self.__args: ArgumentParser = Optional[ArgumentParser, None]
        self.environment: ApplicationEnvironment = Optional[ApplicationEnvironment, None]

    @staticmethod
    def build(classes, args):
        application_context = ApplicationContext().__set_classes(classes).__set_args(args)
        return application_context

    def __set_classes(self, classes: List):
        self.__packages = classes
        return self

    def __set_args(self, args: ArgumentParser):
        self.__args = args
        return self

    def start(self):
        self.environment = ApplicationEnvironment()
        self.environment.start()
