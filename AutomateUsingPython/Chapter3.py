#a function is like a mini program within a program
def hello():
    print('howdy')
    print('Howdy!!!')
    print('Hello there.')

hello()

def hello(name):
    print('Hello {}'.format(name))

hello('Red')

#in functions you can return a value if necessary

#in pythone None is the same as Null

#in a function with no return statement, None is automatically declared - 
#similar to how in a loop there is an implicit continue statement

#on page 91 out of 505

def testing(a,b):
    p = a + b
    return p,a,b

red,t,y = testing(5,7)

#difference between local and global variables
#a,b,p are all local variable
#the function will return p,a,b
#red,t,y are a global variable
#variables are returned and defined in the above order
#note that in R, return only outputs a single thing, so you would need to
#return a list then break that list into its constituent parts.

#next they go into try except finally clauses.

#finished!