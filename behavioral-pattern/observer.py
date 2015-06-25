#! /usr/bin/python

class AbstractSubject:
    def register(self, observer, event):
        raise NotImplemented()

    def unregister(self, observer, event):
        raise NotImplemented()

    def notify(event):
        raise NotImplemented()

class Subject(AbstractSubject):
    def __init__(self):
        self.events = dict()

    def register(self, observer, event):
        # Init the event with an empty list
        if not self.events.has_key(event):
            self.events[event] = list()
        # Adding the observer for the event
        self.events[event].append(observer)

    def unregister(self, observer, event):
        if self.events.has_key(event):
            # Remove the observer for the event
            if observer in self.events[event]:
                self.events[event].remove(observer)
            # Remove the event if its empty
            if len(self.events[event]) == 0:
                self.events.pop(event)

    def notify(self, event):
        if self.events.has_key(event):
            for observer in self.events[event]:
                observer.notify(event)


class AbstractObserver:
    def notify(self, event):
        raise NotImplemented()

class Observer(AbstractObserver):

    def __init__(self, name):
        self.name = name

    def notify(self, event):
        print '{name} executing {event}'.format(name=self.name, event=event)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
