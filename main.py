# Project 4 - Movie Review Sentiment Analysis App
# Adithya Prasad
# Project 4 - Movie Review Sentiment
# 10/22 CS 111 (CRN:40304)

# This app will allow users to submit text files with the reviews
# of any movie of their choice, and will output the overall score
# and general audience opinion regarding if the reviews are positive or negative .


# This void function prints out the menu.
# INPUT:
# isFirstTime - if True, print welcome message.  if False, do not print welcome message.  Here is what prints if True:
#Welcome to the Movie Review Sentiment Analysis App!
#1. Load word list file.
#2. Load movie review file.
#3. Get average score of a word.
#4. Get average scores for a list of words.
#5. Plot average scores for a list of words.
# OUTPUT:
# no return
def display_menu(isFirstTime):
  if isFirstTime:
    print("Welcome to the Movie Review Sentiment Analysis App!")
    print("1. Load word list file.")
    print("2. Load movie review file.")
    print("3. Get average score of a word.")
    print("4. Get average scores for a list of words.")
    print("5. Plot average scores for a list of words.")


# This function reads in a file of words.  Each word in the file gets stored as an item in a list, which is returned.
# INPUTS:
# file_name - a string of which file to read, e.g. "wordList.txt".
# OUTPUTS:
# return the list of words (NOTE: make sure each item in the list contains no extra spaces or newline characters.)
def make_list(file_name):
  file = open(file_name) 
  list = file.readlines()
  newlist = []
  i = 0 
  string = ''
  while i < len(list):
    word = list[i].split()
    newlist += word
    i+=1    
  file.close()
  return newlist


# convert file to a list (each line is an element in the list)
  list = file.readlines()
  file.close()
  pass


# This function reads in a file of movie reviews.  Each review and associated score are stored as a key/value pair (respectively) in a dictionary, which is returned.
# INPUTS:
# file_name - a string of which file to read, e.g. "movieReviews.txt".
# OUTPUTS:
# return the dictionary of reviews (key, string), scores (value, integer) (NOTE: keys that store each movie review do not need to be cleaned to remove spaces, newline characters, or anything else.  See instructions for more details.)
def make_dict(file_name):
    file = open(file_name)
    list = file.readlines()
    file.close()
    i = 0
    dictionary = {}
    while i < len(list):
      line = str(list[i])
      score = int(line[0])
      review = line[2:]
      dictionary[review] = score
      i+=1
    return dictionary


# This function searches the dictionary for wordToFind, counts instances of wordToFind, and calculates the average score.  The word search is case insensitive, however, search is looking for full match not partial match.  For example, if wordToFind is "terrific", movie reviews with "terrific" and "Terrific" are both a match.  However, movie reviews with "terrifically" would not be a match.
# INPUTS:
# dict - a dictionary of reviews (key), scores (value), e.g. dict = {"A series of escapades...":1, "This quiet , ":4, ...}
# wordToFind - a string to search for in the movie reviews, e.g. wordToFind = "terrific"
# OUTPUTS:
# return count, score
# count is number of instances that wordToFind appears in all reviews in dict
# score is the average score for that wordToFind
def search_word(dict, wordToFind):
  count = 0
  score = 0
  avg_score = 0
  for word in dict:
    list = word.split()
    for ch in list:
      if ch.lower() == wordToFind.lower():
        count += 1
        score += dict[word]
  if count == 0:
    avg_score = 0
  else:
    avg_score = score / count
  return count, avg_score


# This function is similar to search_word, except instead of searching for a single word, it searches for a list of words stored in list.
# INPUTS:
# list - a list of words to search for, e.g. list = ["worst", "best", "boring"]
# dict - a dictionary of reviews (key), scores (value), e.g. dict = {"A series of escapades...":1, "This quiet , ":4, ...}
# OUTPUTS:
# return list_scores, avg_score
# where list_scores is a list of the average score for each word in the input parameter list, e.g. list_scores = [0.7272, 2.925, 1.2432]
# where avg_score is the average score of all words in list, e.g. avg_score = (0.7272 + 2.925 + 1.2432)/3 = 1.6318
def search_all_words(list, dict):
    new_list = []
    for word in list:
      count, average = search_word(dict,word)
      new_list.append(average)
    avg_for_all = sum(new_list) / len(new_list)
    return new_list, avg_for_all


# This void function displays the words (stored in list) and their associated scores (stored in list_scores) to screen
# INPUTS:
# list - a list of words
# list_scores - a list of scores (that correspond with the words in list)
# OUPUTS:
# print to screen in the following format:
# worst: 0.7272
# best: 2.925
# etc.
def print_lists(list, list_scores):
    for i in range(len(list)):
      print(list[i]+":",list_scores[i])
    pass

# This is the main code.  It calls all the functions above. It sets up the interaction with the user.
if __name__ == '__main__':
  isFirstTime = True
  display_menu(isFirstTime)
  start = int(input("Enter a number (0 to exit): "))
  while start != 0:
    if start == 1:
      name = input("Enter word list filename: " )
      list = make_list(name)
      print("Word list is loaded.")
    elif start == 2:
      name = input("Enter movie review filename: ")
      dict = make_dict(name)
      print("Movie reviews are loaded.") 
    elif start == 3:
      wordToFind = input("Enter word to search: " )
      count, avg_score = search_word(dict, wordToFind)
      print(wordToFind, "appears",count,"times")
      print("The average score for the reviews containing the word",wordToFind,"is:",avg_score)
    elif start == 4:
      list_scores, avg_score = search_all_words(list, dict)
      print_lists(list, list_scores)
      print("Average score all of words: " + str(avg_score) + " which means this text is ", end="")
      if avg_score >= 2:
        print("positive")
      else:
        print("negative")
    elif start == 5:
      pass
    display_menu(isFirstTime)
    start = int(input("Enter a number (0 to exit): "))


          
