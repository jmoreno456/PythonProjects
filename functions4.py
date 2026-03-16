# passing a list
# you will find it useful to pass a list to a function. when you pass
# a list to a function, the function gets direct access to the contents
# of the list.
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ["hannah", "ty", "margot"]
greet_users(usernames)


# modifying a list in a function
# when you pass a list to a function, the function can modify the list
# any changes made to the list inside the function's body are permanent
# allowing you to work efficiently even when you're dealing with large
# amounts of data.
# consider a company that creates 3D printed models of designs that
# users submit. designs that need to be printed are stored in a list,
# and after being printed they're moved to a separate list


# start with designs that need to be printed
# this code does not use a function
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# simulate printing each design, until none are left
# move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# we can reorganize this code using two functions. each does a specific
# job. we are structuring the code more carefully. the first function
# will handle printing the design, and the second will summarize the
# prints that have been made
# every function should have one specific job. the first function prints
# each design, the second function displays the completed models.
# if you're writing a function and notice the function is doing too
# many different tasks, try to split the code into two functions
# remember that you can always call a function from another function
def print_models(unprinted_designs, completed_models):
    """simulate printing each design, until none are left,
    move each design to completed models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendent", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# preventing a function from modifying a list
# sometimes you'll want to prevent a function from modifying a list
# for example, say that you start with a list of unprinted designs
# and write a function to move them to a list of completed models
# even though you printed all the designs, you want to keep the original
# list of unprinted designs for your records. you can keep the list by
# passing the function a copy of the list, not the original. any changes
# the function makes to the list will affect only the copy, leaving the
# original list intact


# you can send a copy of a list to a function like this:
## function_name(list_name[:])
# the slice notation[:] makes a copy of the list to send to the function
# if we didn't want to empty the list of unprinted designs. we could
# call print_models() like this:
## print_models(unprinted_designs[:], completed_models)


# 8-9 messages: make a list containing a series of short text messages
# pass the list to a function called show_messages(), which prints
# each message
def show_messages(texts):
    """print each message"""
    for text in texts:
        print(text.title())


messages = ["hi", "how are you", "goodnight"]
show_messages(messages)


# 8-10 sending messages: write a function called send_messages() that
# prints each text message and moves each message to a new list called
# sent_messages as it's printed. after calling the function, print both
# of your lists to make sure the message were moved correctly
messages = ["hi", "how are you", "goodnight"]
sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_text = messages.pop(0)
        print(f"\nCurrent Text: {current_text.title()}")
        sent_messages.append(current_text)


# call the function
send_messages(messages, sent_messages)
# print both lists after calling function
print("\nRemaining messages: ", messages)
print("Sent messages: ", sent_messages)


# 8-11 archived messages: start with your work from exercise 8-10. call
# the function send_messages() with a copy of the list of messages. after
# calling the function, print both of your lists to show that the
# original list has retained its messages
messages = ["hi", "how are you", "goodnight"]
sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_text = messages.pop(0)
        print(f"\nCurrent Text: {current_text.title()}")
        sent_messages.append(current_text)


# call the function
send_messages(messages[:], sent_messages)
# print both lists after calling function
print("\nRemaining messages: ", messages)
print("Sent messages: ", sent_messages)
