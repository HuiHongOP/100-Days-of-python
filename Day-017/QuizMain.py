from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in range(0,len(question_data)):
  question_text = question_data[x]['text']
  question_answer = question_data[x]['answer']
  question_bank.append(Question(question_text,question_answer))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
  quiz.next_question()


passing_score = .70
print("You have completed the quiz.")
user_score = quiz.score / quiz.question_number
if user_score >= passing_score:
  print("*************You have passed the quiz!*********************")
else:
  print("**************You didn't pass the quiz********************")
print(f" Your final score is {quiz.score} / {quiz.question_number}")
