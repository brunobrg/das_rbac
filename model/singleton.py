class SingletonMeta(type):
    def __new__(cls, name, bases, namespace):
        singleton_bases = [base for base in bases if isinstance(base, SingletonMeta)]
        if singleton_bases and singleton_bases != [Singleton]:
            raise TypeError('Cannot create subclass of singleton')

        return type.__new__(cls,name, bases, namespace)

    def __call__(self, *args, **kwargs):
        try:
            return self._singleton_instance
        except AttributeError:
            obj = super().__call__(*args, **kwargs)
            self._singleton_instance = obj
            return obj

class Singleton(metaclass=SingletonMeta):
    pass

