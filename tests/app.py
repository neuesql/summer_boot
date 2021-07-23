from summer_boot.application import SummerApplication
from argparse import ArgumentParser


class MyApplication:
    pass


if __name__ == "__main__":
    args = ArgumentParser()
    SummerApplication.run([MyApplication], args=args)
