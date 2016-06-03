class NameGiverType(type):
    def __new__(cls, name, bases, namespace):
        namespace['name'] = name.lower()
        return type.__new__(cls, name, bases, namespace)


class Foo(metaclass=NameGiverType):
    pass

Foo.name
