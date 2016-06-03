from collections import MutableSequence
from numbers import Number

class FooMixin:
    def bar(self):
        print('Hello foo');

class CrazyList(FooMixin, MutableSequence):
    def __init__(self):
        self._data = []

    def __getitem__(self, idx):
        return self._data[idx]

    def __len__(self):
        return len(self._data)

    def __call__(self, x):
        try:
            return self[x]
        except IndexError:
            return x**2

    def __delitem__(self, idx):
        del self._data[idx]

    def __setitem__(self, idx, value):
        self._assert_type(value)
        self._data[idx] = value**2

    def insert(self, idx, value):
        self._assert_type(value)
        self._data.insert(idx,value**2)

    def _assert_type(self, x):
        if not isinstance(x, Number):
            type_name = type(x).__name__
            raise TypeError('%s object is not a number' % type_name)



L = CrazyList()
