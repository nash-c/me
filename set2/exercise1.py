"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# This is a list
some_words = ["what", "does", "this", "line", "do", "?"]

# I think this will print every string that is within the list
for word in some_words:
    print(word) # It prints every word in the list

# Honestly no clue what will happen here, I think it migh print the strings within the list by calling the print function
for x in some_words:
    print(x) # It prints every word in the list

# I think this will print the list, like "['what', 'does', 'this', 'line' 'do', '?']"
print(some_words) # It prints the list as I thought

# If the list has more than 3 words in it, it will print "some_words contains more than 3 words" by calling the print function
if len(some_words) > 3:
    print("some_words contains more than 3 words") # It does what I thought it would


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think it will return a tuple containing my laptop's system, node, release, version, machine and processor by calling the print function
    print(platform.uname()) # It did what I expected, however didn't print the processor part


usefulFunction()
