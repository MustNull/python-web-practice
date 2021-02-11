from peewee import CharField


class PasswordField(CharField):
    def python_value(self, value):
        return super().python_value(value)

    def db_value(self, value):
        # ToDo: 加密
        return super().db_value(value)
