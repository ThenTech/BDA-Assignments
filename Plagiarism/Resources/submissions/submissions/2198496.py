# write your code here
def clean_up_and_count(string):
    new_string = ""
    for char in string:
        # if the char is not in the alfabet
        if char_in_char_list(char, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            new_string += char
        elif new_string != "":
            print(new_string, len(new_string))
            new_string = ""
            
    if new_string != "":
            print(new_string, len(new_string))
            
def char_in_char_list(char, char_list):
    for item in char_list:
        if item == char:
            return True
    return False
    
clean_up_and_count( input("Give me a String:") )