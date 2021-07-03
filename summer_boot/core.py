from argparse import ArgumentParser
from dependency_injector import containers, providers


class ApplicationContext:

    def start(self):
        pass


class SummerApplication:

    def __init__(self):
        self.container = containers.DynamicContainer()

    @classmethod
    def run(cls, instance: object, args: ArgumentParser) -> ApplicationContext:
        application_context = ApplicationContext()
        application_context.start()
        return application_context
