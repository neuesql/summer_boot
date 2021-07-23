from argparse import ArgumentParser
from typing import List, Optional, Dict
import glob
import os
import yaml

from summer_boot.context import ApplicationContext


class SummerApplication:

    def __init__(self):
        pass

    @classmethod
    def run(cls, classes: List[type], args: ArgumentParser) -> ApplicationContext:
        application_context = ApplicationContext.build(classes, args)
        return application_context.start()
