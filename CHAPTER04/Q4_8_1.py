def show_begin_end(func):
    def wrapper(*args, **kwargs):
        print("== begin")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return wrapper


def example_function():
    print("This is an example function.")


example_function()
