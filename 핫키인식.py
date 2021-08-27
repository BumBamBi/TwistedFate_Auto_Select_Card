from pynput.keyboard import Listener, Key, KeyCode

store = set()
 
HOT_KEYS = {
    'print_hello': set([ Key.ctrl_l, KeyCode(char='w')] )
}
 
def print_hello():
    print('hello, World!!!')
 
def handleKeyPress( key ):
    store.add( key )
 
    for action, trigger in HOT_KEYS.items():
        CHECK = all([ True if triggerKey in store else False for triggerKey in trigger ])
 
        if CHECK:
            try:
                func = eval( action )
                if callable( func ):
                   func()
            except NameError as err:
                print(err)

def handleKeyRelease( key ):
    if key in store:
        store.remove( key )
        
    # 종료
    if key == Key.esc:
        return False
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()

