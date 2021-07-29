import json
from difflib import get_close_matches

data = json.load(open("d:/Study stuff/python/1-Dictionary-project/data.json"))
def meaning(word):
    word=word.lower()
    
    if word in data:
        return data[word]

    elif word.capitalize() in data:
        return data[word.capitalize()]
    
    elif word.upper() in data:
        return data[word.upper()]
    
    elif len(get_close_matches(word,data.keys(),n=1,cutoff=0.8))>0:
        response = input("Did you mean %s instead ? Enter Y for yes and N for no : " % get_close_matches(word,data.keys(),n=1,cutoff=0.8)[0])
        
        if response=="Y" or response=="y" :  
            return data[get_close_matches(word,data.keys(),n=1,cutoff=0.8)[0]]
        
        elif response=="N" or response=="n" :
            word = input("Enter new word : ")
            output = meaning(word)
            if type(output) == list :
                for item in output:
                    print(item)
            else : 
                print(output)
            
            return None 
        
        else:
            return "Invalid input . "
    
    else :
        return "Word dose not exist. Please check the word again."

word = input("Enter word: ")
    
if word == "" :
    print("No input recived.")
    word = input("Enter word again : ")
    
output = meaning(word)

if type(output) == None:
    print()

elif type(output) == list :
    for item in output:
        print(item)

else : 
    print(output)

close = input("Press any key to exit ")