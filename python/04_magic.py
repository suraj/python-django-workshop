#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Human(object):
    def __init__(self, name=None):
        super(Human, self).__setattr__('_dict', {})
        self._dict['name'] = name

    def __setattr__(self, name, value):
        self._dict[name] = value

    def __getattr__(self, name):
        return self._dict.get(name, None)

    def __delattr__(self, name):
        try:
            del self._dict[name]
        except:
           pass

    def __eq__(self, obj):
        print False

    def __str__(self):
        return self.name if self.name else 'Unnamed Human'

    def __unicode__(self):
        return self.name if self.name else u'Unnamed Human'

    def __repr__(self):
        return str(self._dict)












krishna = Human("Krishna")
ram = Human("Ram")

krishna.email='krishna@gmail.com'
ram.email='ram@gmail.com'
ram.is_married = True
ram.wife = "sita"

ram == krishna

print ram.wife
del ram.wife
print ram.wife

# print unicode(ram)
# print krishna


# print krishna.name
# print ram.name

# print krishna.email
# print ram.email

# print str(krishna)
# print unicode(krishna)
# print repr(krishna)






