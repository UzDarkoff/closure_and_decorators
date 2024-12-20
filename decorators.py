# from time import time
# def decorator(func):
#     def timer(*args,**kwargs):
#         start=time()
#         natija=func(*args,**kwargs)
#         stop=time()
#         vaqt=stop-start
#         print(f"{func.__name__} funksiya {vaqt:4f} soniyada bajarildi")
#         return natija
#     return timer
# @decorator
# def salomlash():
#     print("salom")
#
# salomlash()


def fibonacci(n):
    a, b = 0, 1
    def fib():
        nonlocal a,b
        for _ in range(n):
            a,b=b,a+b
        return a
    return fib()
n=10
print(fibonacci(n))

