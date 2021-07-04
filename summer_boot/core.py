from argparse import ArgumentParser
from typing import List, Optional, Dict


class Environment:

    def __init__(self, env_name: str = 'default') -> None:
        self.env_name = env_name

    def start(self):
        #     load yaml
        return self

    def stop(self):
        return self


class ApplicationContext:

    def __init__(self):
        self.classes: List = []
        self.args: ArgumentParser = Optional[None]
        self.environment: Environment = Optional[None]

        self.initializing: bool = False
        self.running: bool = False
        self.terminating: bool = False

        self.singleton_objects: Dict[str, object] = {}
        self.singleton_creating_objects: Dict[str, object] = {}
        self.providers: List[type] = []

    @staticmethod
    def build(classes, args):
        application_context = ApplicationContext().set_classes(classes).set_args(args)
        application_context.environment = application_context.initialize_environment()
        application_context.providers = application_context.find_providers()
        return application_context

    def set_classes(self, classes: List):
        self.classes = classes
        return self

    def set_args(self, args: ArgumentParser):
        self.args = args
        return self

    def start(self):
        self.running = True
        self.initialize_context(self.providers)
        self.initializing = False
        return self

    def stop(self):
        self.initializing = False
        self.terminating = True
        return self

    def initialize_environment(self):
        environment = Environment()
        environment.start()
        self.register_singleton(Environment.__class__, environment)
        return environment

    def initialize_context(self, ps: List[type]):
        pass

    def create_bean(self, type, object):
        return self

    def get_bean(self, type, name):
        return None

    def find_providers(self):
        return []

    def register_singleton(self, __class__, environment):
        pass


class SummerApplication:

    def __init__(self):
        pass

    @classmethod
    def run(cls, classes: List[type], args: ArgumentParser) -> ApplicationContext:
        application_context = ApplicationContext.build(classes, args)
        return application_context.start()
