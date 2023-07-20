# fucntions equivalent to a throw() in js

class MyOwnError(Exception):
    pass

# ?1 raise Exception(message)
# ?2 assert(condition), messasge

# !accepting exceptions => Exception as e


# you can do that:
try:
    pass
except TypeError:
    pass
except ZeroDivisionError:
    pass
except MyOwnError:
    pass
else:
    # ? if no expection was triggerd
    pass
finally:
    # ? if no expection was triggerd
    # ? Usa
    # ully used for cleaing up operations
    pass
