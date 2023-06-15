import re

def crawl_blank(blank_path):
    with open(blank_path, 'r') as file:
        blank = file.read()
    return blank

def template_parsed(template):
    madwords = re.findall(r"\{(.*?)\}", template)
    print("these are the madwords: ", madwords)
    return madwords

def userPutWordsHere(spells):
    userInputList = []
    for word in spells:
        print("Cast your magic for {}:".format(word))
        new_word = input()
        userInputList.append(new_word)
    print("this is the userList: ", userInputList)
    return userInputList

def fulfill_template(template, wordList):
    print("this is the template: ", template)
    pattern = "\{(.*?)\}"
    # for word in spells:
    storyString = re.sub(pattern, lambda x: wordList.pop(0), template)
    return storyString


def write_to_spellbook(template, blank_path):
    with open(blank_path, "w") as f:
        f.write(template)

def main():
    # template_blank_path = input("Enter the path to the blank file: ")
    # template = crawl_blank(template_blank_path)
    template = "madlib_cli/madlib_template.txt"
    
    read_template = crawl_blank(template)
    
    parsed_madwords = template_parsed(read_template)
    
    userList = userPutWordsHere(parsed_madwords)
    
    fulfilled_template = fulfill_template(read_template, userList)
    
    print("these would be the userList: ", userList)
    
    print("this is the fulfilled template: ", fulfilled_template)
    
    complete_spellbook = write_to_spellbook(fulfilled_template, "madlib_output.txt")
    
    print("spellbook", complete_spellbook)

if __name__ == "__main__":
  main()