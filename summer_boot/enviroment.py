import glob
import os
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

import yaml
from dotenv import dotenv_values


class BaseEnvironment(ABC):

    def __init__(self):
        self.DEFAULT_APPLICATION_NAME = 'application'
        self.DEFAULT_ENV_NAME = 'env'
        self.reading: bool = False
        self.running: bool = False
        self.properties: Dict[str, object] = {}

    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...


class ApplicationEnvironment(BaseEnvironment):

    def __init__(self, configure_locations: Optional[List[str]] = None):
        super().__init__()
        self.configure_locations = []
        if configure_locations is None:
            self.configure_locations.append(os.getcwd())
        else:
            self.configure_locations.extend(configure_locations)

    def read_application_properties(self):
        for location in self.configure_locations:
            file_pattern = f"{location}/{self.DEFAULT_APPLICATION_NAME}*.yml"
            files = glob.glob(file_pattern)
            for file_name in files:
                with open(file_name) as file_handle:
                    """
                    TODO, several env file
                    """
                    self.properties[self.DEFAULT_APPLICATION_NAME] = yaml.safe_load(file_handle)

    def read_env_properties(self):
        for location in self.configure_locations:
            file_pattern = f"{location}/.{self.DEFAULT_ENV_NAME}"
            configuration = {**os.environ, **dotenv_values(file_pattern)}
            self.properties[self.DEFAULT_ENV_NAME] = configuration

    def start(self):
        self.read_application_properties()
        self.read_env_properties()

    def stop(self):
        pass
