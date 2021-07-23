from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import List, Optional, Dict, Type
from loguru import logger
import inspect
import sys

from summer_boot.decorator import bean, factory
from summer_boot.enviroment import ApplicationEnvironment


class ApplicationLifeCycle(ABC):

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


class ApplicationBeanProvider(ABC):

    @abstractmethod
    def get_bean_provider(self, class_type: Type):
        ...

    @abstractmethod
    def get_bean_providers(self):
        ...

    @abstractmethod
    def find_all_bean_providers(self):
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


class AbstractBeanContext(ApplicationLifeCycle, ApplicationEventPublisher, ApplicationBeanProvider):

    def __init__(self):
        self.__initializing: bool = False
        self.__running: bool = False
        self.__terminating: bool = False

        self.__singleton_objects: Dict[Type, object] = {}
        self.__providers: List[Type] = []
        self.logger = logger

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

    @abstractmethod
    def initialize_event_listeners(self):
        ...

    @abstractmethod
    def initialize_context(self, beans: List):
        ...


class User:
    def __init__(self):
        self.user_name: str = "wuqunfei"
        self.password: str = "1213"


@bean(name='user')
class UserController:
    pass


@factory(name="fac")
class UserConfig:

    @bean(name="my_config", type=User)
    def get_config(self) -> User:
        return User()


class ApplicationContext(AbstractBeanContext):

    def __init__(self):
        super().__init__()
        self.__packages: List = []
        self.__args: ArgumentParser = Optional[ArgumentParser]
        self.environment: ApplicationEnvironment = Optional[ApplicationEnvironment]

    @staticmethod
    def build(classes, args):
        application_context = ApplicationContext().set_classes(classes).set_args(args)
        return application_context

    def set_classes(self, classes: List):
        self.__packages = classes
        return self

    def set_args(self, args: ArgumentParser):
        self.__args = args
        return self

    def start(self):
        self.environment = ApplicationEnvironment()
        self.environment.start()
        self.find_all_bean_providers()

    def find_all_bean_providers(self):
        module = sys.modules[__name__]
        for name, instance in inspect.getmembers(module, predicate=inspect.isclass):
            logger.info(name)
            if hasattr(instance, '__bean_type'):
                self.logger.info(name)
            if hasattr(instance, '__factory_name'):
                self.logger.info(name)

    def create_bean(self, class_type: Type):
        pass

    def destroy_bean(self, class_type: Type):
        pass

    def refresh_bean(self, class_type: Type):
        pass

    def get_bean(self, class_type: Type) -> Optional[object]:
        pass

    def get_beans(self, class_type: Type) -> List[object]:
        pass

    def initialize_event_listeners(self):
        pass

    def initialize_context(self, beans: List):
        pass

    def stop(self):
        pass

    def refresh(self):
        pass

    def is_running(self) -> bool:
        pass

    def publish_event(self, event: object) -> None:
        pass

    def publish_event_sync(self, event: object) -> None:
        pass

    def publish_event_async(self, event: object) -> None:
        pass

    def get_bean_provider(self, class_type: Type):
        pass

    def get_bean_providers(self):
        pass
