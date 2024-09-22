#
# def searcher():
#     import time
#     # Some 4 seconds time consuming task
#     book = "This is a book on harry and code with harry and good"
#     time.sleep(4)
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book")
#         else:
#             print("Text is not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("Next method run")
# search.send("harry")
#
# search.close()
# search.send("harry")
# # input("press any key")
# # search.send("harry and")
# # input("press any key")
# # search.send("thi si")
# # input("press any key")
# # search.send("joker")
# # input("press any key")
# # search.send("like this video")
#
# Example:-
def seacher():
    file = "Rohan , Anant , Rajat , Prateek , Vansh Gupta , Atul , Deepesh"
    import time
    time.sleep(4)
    while True:
        text = yield
        if text in file:
            print("Name is in the file")
        else:
            print("Name is not in the file")

search = seacher()
next(search)
name = input("Enter the name: ")
search.send(name)
name = input("Enter the name: ")
search.send(name)
name = input("Enter the name: ")
search.send(name)
name = input("Enter the name: ")
search.send(name)


