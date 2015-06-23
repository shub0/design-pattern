#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GreekGetter:
    """
    Concrete Product
    """
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter:
    """
    Concrete Product
    """
    def get(self, msgid):
        return str(msgid)

class Creator:
    @staticmethod
    def get_localizer(language="English"):
        """
        The factory method
        """
        languages = dict(English=EnglishGetter, Greek=GreekGetter)
        return languages[language]()

if __name__ == "__main__":
    # Create our localizers
    e, g = Creator.get_localizer(language="English"), Creator.get_localizer(language="Greek")
    # Localize some text
    for msgid in "dog parrot cat bear".split():
        print(e.get(msgid), g.get(msgid))
