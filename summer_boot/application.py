from argparse import ArgumentParser
from typing import List

from summer_boot.context import ApplicationContext


class SummerApplication:

    @classmethod
    def run(cls, classes: List[type], args: ArgumentParser) -> ApplicationContext:
        application_context = ApplicationContext().build(classes, args)
        return application_context.start()
