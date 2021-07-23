import os

from summer_boot.application import SummerApplication
from summer_boot.context import ApplicationContext
from summer_boot.decorator import SummerBootApplication
from argparse import ArgumentParser


@SummerBootApplication
class MyApplication:
    pass


if __name__ == "__main__":
    args = ArgumentParser()
    SummerApplication.run(MyApplication.__class__, args=args)
