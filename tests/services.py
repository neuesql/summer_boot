from summer_boot.decorator import bean, factory


class User:
    def __init__(self):
        self.user_name: str = "wuqunfei"
        self.password: str = "1213"


@bean(name='user')
class UserController:
    pass


@factory(name="fac")
class UserConfig:

    @bean(name="my_config")
    def get_config(self) -> User:
        return User()
