import os

class Words:
    
    def checkWord(self,currentWord):
        count = 0
        n = []
        cWord = currentWord #tracks the current word in the array
        
        nWord = ['TEDDY','NILE','GOD','SUN']
        
        word = nWord[currentWord] #Get the word

        print(word)

        print("The word has " + str(len(word)) + " letters "
              + "and begins with " + word[0]
              + " and ends with " + word[len(word)-1]
              )
        
        while count < len(word): 
            theLetter = input("What is the " + self.countNumber(count) + " letter? ")
            if theLetter == word[count]: #if the user has gotten the current letter
                print("Correct!")
                n.append(theLetter) #show the current letter progress
                print("So far you have found: " + ''.join(n) + "\n")
                count =count+1 #go to the next letter  
            else:
                print("Wrong, buddy")
                print("So far you have found: " + ''.join(n) + "\n")
        if count==len(word):
            print("Correct! You have guessed the FULL word: " + word)
            cWord +=1 #Go to the next word
            count = 0
            self.clearConsole()
            self.checkWord(cWord) #cWord tells function the current word to use

    def countNumber(self,nCount):
        nNumber = nCount + 1

        if nNumber == 1:
            return "1st"
        elif nNumber == 2:
            return "2nd"
        elif nNumber == 3:
            return "3rd"
        elif nNumber == 4:
            return "4th"
        elif nNumber == 5:
            return "5th"
        elif nNumber == 6:
            return "6th"
        elif nNumber == 7:
            return "7th"
        
    def clearConsole(self):
        os.system('cls')
        
                
    
#main
GuessWords = Words()
GuessWords.checkWord(0)
