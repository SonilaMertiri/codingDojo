# 1.Create a function that, given a string, returns all of that string’s contents, but without blanks. 

def removeBlanks(string):
    return ''.join(string.split())

# Examples
print(removeBlanks(" Pl ayTha tF u nkyM usi c "))  # Output: "PlayThatFunkyMusic"
print(removeBlanks("I can not BELIEVE it's not BUTTER"))  # Output: "IcannotBELIEVEit'snotBUTTER"

