from functools import lru_cache

n = int(input("Enter the cache: "))
@lru_cache(n)
def random1():
    print("Hello world")
    print("""hlo
    how are you
    kasa ho 
    """)

random1()