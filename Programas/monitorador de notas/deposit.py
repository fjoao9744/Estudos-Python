def separar(func):
    def wrapper():
        print('=' * 20)
        func()
        print('=' * 20)
    return wrapper