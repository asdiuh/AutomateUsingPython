#lists
#lists vs tuples
#elements

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
spam[1:4]
spam[1:]
spam[:2]
spam[:-1]
#spam_original = spam
import copy
spam_original = copy.deepcopy(spam)
spam[1] = 'aardvark'

#just learned how to copy stuff