import inspect
from typing import Type


def bean(name: str = None, type: Type = None):
    def decorator(bean_cls):
        bean_cls.__bean_name = name
        if inspect.isclass(bean_cls):
            bean_cls.__bean_type = bean_cls
        elif inspect.isfunction(bean_cls):
            bean_cls.__bean_type = type
        return bean_cls

    return decorator


def factory(name: str = None):
    def decorator(factory_cls):
        factory_cls.__factory_name = name
        return factory_cls

    return decorator
