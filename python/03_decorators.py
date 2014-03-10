
# Decorator
def no_negative(func):
    def wrapped(number):
        if number < 0:
            print("No negative number please.")
        else:
            func(number)

    return wrapped
















@no_negative
def add_apple(number):
    #number = kwargs.get("number")
    print ("Added {} Apples in the basket.".format(number))

# print 'add_apple(5, "apple")'
# #add_apple(5, "apple")
# print 'add_apple(number=5, name="apple")'
# add_apple(number=5, name="apple")
# print 'add_apple(name="apple", number=5)'
# add_apple(name="apple", number=5)
# print 'add_apple(5, color="green", name="apple")'
# #add_apple(5, color="green", name="apple")


# add_apple(5)
# add_apple(-5)










# exit(0)





# Decorator Adv
def no_negative_generic(func):
    def wrapped(*args, **kwargs):
        count = kwargs.get('count', None)
        stuff = kwargs.get('name', None)

        if count is None:
            print "How many to add?"
            return None

        if not isinstance(count, int):
            print "Give me some int please.."
            return None
        if stuff is None:
            print "What is it?"
            return None

        if count < 0:
            print("No negative count please.")
        else:
            func(*args, **kwargs)

    return wrapped

@no_negative_generic
def add(name=None, count=None):
    print ("Added {} {}s in the basket.".format(count, name))

add(name="Apple", count=5)
add(count=5)
add(name="Orange", count=10)
