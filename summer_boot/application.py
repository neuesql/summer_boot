from argparse import ArgumentParser
from typing import List, Type

from summer_boot.context import ApplicationContext


class SummerApplication:

    @classmethod
    def run(cls, classes: List[Type], args: ArgumentParser) -> ApplicationContext:
        application_context = ApplicationContext().build(classes, args)
        return application_context.start()
