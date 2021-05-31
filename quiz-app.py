class Question:     # Question object to iterate over questions and perform required actions
    
    def __init__(self, text, choices, answer):      # constructor function, gets text of the question, choices and answer
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):      # instance method to check whether the answer is correct
        return ((self.answer.lower() == answer.lower()) or (self.answer.upper() == answer.upper()) or (self.answer == answer))

class Quiz:     # Quiz object
    def __init__(self, questions):      # constructor function, gets quesitons as a list and initialises score and index params
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
        self.points = 100 / len(self.questions)        # calculate points to be assigned to a question
    
    def getQuestion(self):      # get question by index number
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):      # display question, choices and prompt for user input
        question = self.getQuestion()       # store the returned question 
        print(f"Question {self.questionIndex + 1}: {question.text}")
        
        for c in question.choices:
            print(f"- {c}")
        
        answer = input("\nAnswer: ")        # get user input (answer)
        self.getAnswer(answer)      # call getAnswer function for checking answer with answer parameter
    
    def getAnswer(self, answer):        # method declaration for answer checking
        question = self.getQuestion()       # get current question
        
        if question.checkAnswer(answer):        # check if the given method returns true or false according to the provided answer
            self.score += self.points        # if answer is true, add points to the total score
        
        self.questionIndex += 1     # increment question index by 1 to advance to the next question
        self.loadQuestion()     # call loadQuestion method
    
    def loadQuestion(self):     # loadQuestion method declaration to decide how to continue
        if self.questionIndex == len(self.questions):       # if question index is reached the last value,
            self.showProgress()     # show progress
            self.showScore()        # show final score
        else:       # if there are still questions to be loaded,
            self.showProgress()     # show progress
            self.displayQuestion()      # display the next question
    
    def showScore(self):        # if all questions are answered, show the final score and rate of correct answers
        print(f"Your Score: {self.score:.2f} / 100\nYou have correctly answered {int(self.score / self.points)} questions out of {len(self.questions)}.")
    
    def showProgress(self):     # show current progress, in which question you are
        if self.questionIndex == len(self.questions):
            print("\nQuiz is over!")
            print(" R E S U L T S ".center(100, "-"))
        else:
            print(f" Question {self.questionIndex + 1} of {len(self.questions)} ".center(100, "-"))


'''
THE PART BELOW COMPLETELY DEPENDS ON WHAT QUESTIONS TO ASK, WHAT CHOICES TO DISPLAY AND WHAT IS THE ANSWER!

Feel free to change number of questions and questions details!
'''

# Creating Question objects 
q1 = Question("Which programming language is mostly used in embedded programming?", ["Java", "C", "Python", "Swift"], "C")      # Change this line
q2 = Question("Which city serves as a bridge between Asia and Europe?", ["Istanbul", "Cairo", "Moscow", "Athens"], "Istanbul")      # Change this line
q3 = Question("Which one is a client-side vulnerability?", ["Broken Authentication", "Lack of Obfuscation", "Cross-Site Scripting", "Mass Assignment"], "Cross-Site Scripting")     # Change this line
q4 = Question("Which programming language does Django framework belong to?", ["Java", "C", "Python", "Swift"], "Python")        # Change this line

questions = [q1, q2, q3, q4]        # assigning questions to a list     -> Change this line

quiz = Quiz(questions)      # creating a quiz object by providing questions as a list 

quiz.loadQuestion()   # call loadQuestion method of quiz object and start the quiz
