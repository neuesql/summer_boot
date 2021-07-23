def controller(cls):
    pass


def service(cls):
    pass


def bean(name: str = None):
    def decorator(bean_cls):
        bean_cls.__bean_name = name
        bean_cls.__bean_type = bean_cls
        return bean_cls

    return decorator
