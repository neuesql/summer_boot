from argparse import ArgumentParser
from typing import List, Optional, Dict

from summer_boot.enviroment import ApplicationEnvironment


class ApplicationContext:

    def __init__(self):
        self.classes: List = []
        self.args: ArgumentParser = Optional[None]
        self.environment: ApplicationEnvironment = Optional[None]

        self.initializing: bool = False
        self.running: bool = False
        self.terminating: bool = False

        self.singleton_objects: Dict[str, object] = {}
        self.providers: List[type] = []
