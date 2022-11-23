def retry():
    def _decorator(func):
        def wrapper(*args,**kwargs):
            for attempt in range(1, 7):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(str(attempt)+"раз(а)",e)
            print("*******S*******T*******O*******P*******")
            print("Количество попыток превышено, Остановочка )")
        return wrapper
    return _decorator


@retry()
def func():
    raise ValueError("Наша функция в действии")

func()