class QuizBrain:
  def __init__(self,questions_list):
    self.question_number = 0
    self.questions_list = questions_list
    self.score = 0
  def still_has_questions(self):
    if self.question_number < len(self.questions_list):
      return True
    else:
      return False
  def next_question(self):
    current_question = self.questions_list[self.question_number].text
    user_answer = input(f"Q.{self.question_number+1}: {current_question} True/False: ")
    current_answer = self.questions_list[self.question_number].answer
    self.question_number +=1
    self.check_answer(user_answer,current_answer)
  def check_answer(self,user_answer,current_answer):
    if user_answer.lower() == current_answer.lower():
      print("You got it right! ")
      self.score +=1
    else:
      print("It's wrong.")
    print(f"The correct answer is: {current_answer} ")
    print(f"Your current score is: {self.score} /{self.question_number} ")
