entered_text = str(input('please enter a word: ')) #user prompted to enter a phrase/word
lower_text = entered_text.lower() #all cases are lowered
no_space = str(lower_text.replace(" ","")) #all the spaces are removed
print('the string without spaces is: ',no_space) 
reversed_string = ''.join(reversed(no_space))
print('the reversed string is: ',reversed_string)
no_space_list = list(no_space.split(' ')) #the phrase is converted to a list for iteration purposes
print('the phrase you entered without spaces is: ', no_space_list)
reversed_string_list = list(reversed_string.split(' ')) #the phrase is converted to a list for iteration purposes
print('the reversed phrase you entered without spaces is: ',reversed_string_list)
for i in range(len(reversed_string_list)): #the for loop to compare two lists and determine whether they are identical
    if reversed_string_list[i]==no_space_list[i]:
        print('The phrase you enetered is a palindrome.')
    else:
        print('The phrase you enetered is not a palindrome.')



