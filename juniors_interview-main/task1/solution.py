def strict(func):
    def wrapper(*args):
        param = func.__annotations__
        for index in range(len(list(param.keys()))):
            if list(param.keys())[index] == 'return':
                break
            if type(args[index]) != param[list(param.keys())[index]]:
                raise TypeError("type is not correct")
        return func(*args)
    return wrapper
