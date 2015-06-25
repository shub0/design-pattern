#! /usr/bin/python

class Event:
  def __init__( self, name ):
    self.name = name

# This is the Handler interface and base implementation
class Handler:
  # pass in the successor. if you do not pass something in
  # it would be assumed to be the end of the Chain
  def __init__( self, successor = None ):
    self.__successor = successor

  def handle( self, event ):
    handler = 'handle_' + event.name

    # if the handler has the event attribute, it can handle the object, so do so
    if hasattr( self, handler ):
      method = getattr( self, handler )
      return method( event )

    # if it does not have the attribute, it means this handler is not appropriate so pass
    # it to the next handler in the chain
    elif self.__successor:
      return self.__successor.handle( event )

    # this is an implementation detail and not strictly required
    # adds a default support to all handlers (i.e. catch all for non supported events)
    elif hasattr( self, 'handle_default' ):
      return self.handle_default( event )

# Concrete Handler
class EndOfChain( Handler ):
  def handle_close( self, event ):
    return 'EndOfChain: ' + event.name
  def handle_default( self, event ):
    return 'Default: ' + event.name

# Concrete Handler
class MiddleOfChain( Handler ):
  def handle_do( self, event ):
    return 'MiddleOfChain: ' + event.name

# Concrete Handler
class FirstOfChain( Handler ):
  def handle_action( self, event ):
    return 'FirstChain: ' + event.name

def main():
    # Client code following for constructing the chain
    # and sample executions of the chain

    # build chain of responsibility
    end = EndOfChain()
    middle = MiddleOfChain(end)
    first = FirstOfChain(middle)

    doEvent = Event('do')
    actionEvent = Event('action')
    closeEvent = Event('close')
    nilEvent = Event('nil')

    assert first.handle(actionEvent) == "FirstChain: action"
    assert first.handle(doEvent) == "MiddleOfChain: do"
    assert first.handle(closeEvent) == "EndOfChain: close"
    assert first.handle(nilEvent) == "Default: nil"
    print "Testing passed"

if __name__ == "__main__":
    main()
