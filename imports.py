# in order to access functions in other files, you need to import them. For example
import functions

# now, you can call any function within it, so long as you prefix it with functions.
print(functions.test1(1, 2))
# alternatively, you can also get specific functions from other files which can be added into the program as if it was defined within the file
from functions import test1

print(test1(2,2))

# so, to make and use packages 
# make a file named __init__.py and put the files within there
# to import the whole package, simply:
# import somepackage
# when doing this, any of the functions must be prefixed like
# somepackage.somemodule.function()
# if you want a specific module
# import somepackage.shipping
# functions then must be prefixed like shipping.function()