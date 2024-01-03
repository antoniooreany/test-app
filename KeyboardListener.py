def logging_decorator(cls):
    class NewClass(cls):
        def on_press(self, key):
            print(f'Key {key} pressed')
            super().on_press(key)

        def on_release(self, key):
            print(f'Key {key} released')
            super().on_release(key)

    return NewClass

@logging_decorator
class KeyboardListener:
    pass
