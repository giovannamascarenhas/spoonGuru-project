""" 
This file creates an object manager like Django manager
to create custom filter queries with Python
"""

from collections.abc import MutableSet
import operator
import inspect


class ObjectManager(MutableSet):
    """This class creates a object manager like in Django."""
    def __init__(self):
        self._object_attributes = None
        self._theset = set()
    
    def add(self, item):
        self._theset.add(item)

    def discard(self, item):
        self._theset.discard(item)
    
    def __iter__(self):
        return iter(self._theset)
    
    def __len__(self):
        return len(self._theset)
    
    def __contains__(self, item):
        try:
            return item in self._theset
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


# table_data = [
#     {'id': 1, 'url': 'somwulr.com', 'date': '19-06-2020', 'rating': 9.5},
#     {'id': 2, 'url': 'somwulr2.com', 'date': '15-02-2019', 'rating': 8.4},
# ]
# for data in table_data:
#     MyTable(**data)

# print([md.id for md in MyTable.objects.filter(id__ge=1)])
# print([md.id for md in MyTable.objects.filter(mode='and', id__ge=1, rating__ge=5.5, date__eq='19-06-2020')])
