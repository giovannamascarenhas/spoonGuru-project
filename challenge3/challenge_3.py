""" 
This file creates an object manager like Django manager
to create custom filter queries with Python
"""

# External packages
from collections.abc import MutableSet
import operator
import inspect


class ObjectManager(MutableSet):
    """This class creates a object manager like in Django."""
    def __init__(self):
        self._object_attributes = None
        self._data = set()
    
    def add(self, item):
        self._data.add(item)

    def discard(self, item):
        self._data.discard(item)
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, item):
        try:
            return item in self._data
        except AttributeError:
            return False

    def set_attributes(self, an_object):
        self._object_attributes = [
            a[0] for a in inspect.getmembers(
                an_object, lambda a:not(inspect.isroutine(a))
            ) if not(a[0].startswith('__') and a[0].endswith('__'))
        ]

    def filter(self, **kwargs):
        mode = kwargs.pop('mode', 'or')
        ok_objects = set()
        for kw in kwargs:
            if '__' in kw:
                _kw, op = kw.split('__')
                # Valid operators
                assert op in ('lt', 'le', 'eq', 'ne', 'ge', 'gt', 'in')
            else:
                op = 'eq'
                _kw = kw
            _oper = getattr(operator, op)
            # Allow access to valid object attributes
            assert _kw in self._object_attributes
            n_objects = (
                obj for obj in self if _oper(getattr(obj, _kw), kwargs[kw])
                )
            if mode == 'and':
                if n_objects:
                    ok_objects = ok_objects.intersection(n_objects)\
                        if ok_objects else set(n_objects)
                else:
                    return set()

            else:
                ok_objects.update(n_objects)
        return ok_objects


class MyTable:
    # initiate the object manager
    objects = ObjectManager()

    def __init__(self, id, url, date, rating):
        self.id = id
        self.url = url
        self.date = date
        self.rating = rating

        if not len(self.objects):
            self.objects.set_attributes(self)
        # add the new instance to the object manager
        self.objects.add(self)
