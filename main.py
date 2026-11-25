import time

print("WELCOME TO ISLAMIC QUIZ!")

start_time = time.time()

question1 = ["Who was the first Caliph of Islam?:", "Abu Bakr", "Umar ibn al-Khattab", "Uthman ibn Affan", "Ali ibn Abi Talib"]
question2 = ["What is the name of the Prophet Muhammad's (PBUH) mother?:", "Aminah bint Wahb", "Fatimah bint Asad", "Khadijah bint Khuwaylid", "Hafsa bint Umar"]
question3 = ["In which city was the Prophet Muhammad (PBUH) born?:", "Mecca", "Medina", "Syria", "Iraq"]
question4 = ["What is the name of the Prophet Muhammad's (PBUH) first wife?:", "Khadijah bint Khuwaylid", "Aminah bint Wahb", "Fatimah bint Asad", "Hafsa bint Umar"]
question5 = ["Who was the Prophet Muhammad's (PBUH) uncle who raised him?:", "Abu Talib", "Abdul-Muttalib", "Abdullah ibn Abdul-Muttalib", "Uthman ibn Affan"]
question6 = ["What is the name of the Prophet Muhammad's (PBUH) grandfather?:", "Abdul-Muttalib", "Abdullah ibn Abdul-Muttalib", "Muhammad ibn Abdullah", "Uthman ibn Affan"]
question7 = ["Which cousin of the Prophet Muhammad (PBUH) was also a companion?:", "Abdullah ibn Umar", "Ali ibn Abi Talib", "Uthman ibn Affan", "Abu Hurairah"]
question8 = ["What was the name of the Prophet Muhammad's (PBUH) son who died in infancy?:", "Qasim", "Isa", "Yusuf", "Ishaq"]
question9 = ["Which daughter of the Prophet Muhammad (PBUH) married Ali ibn Abi Talib?:", "Zaynab", "Umm Kulthum", "Fatimah", "Ruqayyah"]
question10 = ["Which companion was particularly known for his knowledge and wisdom?:", "Abu Bakr", "Umar ibn al-Khattab", "Uthman ibn Affan", "Ali ibn Abi Talib"]

correct_answers = [
    "Abu Bakr",
    "Aminah bint Wahb",
    "Mecca",
    "Khadijah bint Khuwaylid",
    "Abu Talib",
    "Abdul-Muttalib",
    "Ali ibn Abi Talib",
    "Qasim",
    "Fatimah",
    "Ali ibn Abi Talib"
]

questions = [
    question1, question2, question3, question4, question5,
    question6, question7, question8, question9, question10
]

score = 0
wrong_answers = []

for i in range(len(questions)):

    print("\nQuestion", i + 1, ":", questions[i][0])

    for j in range(1, 5):
        print(chr(64 + j) + ".", questions[i][j])

    answer = input("Your answer: ").strip()

    if answer.lower() == correct_answers[i].lower():
        print("Correct! Well done!")
        score += 1

    else:
        print("Incorrect!")
        wrong_answers.append(
            (questions[i][0], answer, correct_answers[i])
        )

end_time = time.time()

total_time = round(end_time - start_time, 1)

print("\n===== QUIZ RESULTS =====")

print("Your score:", score, "/ 10")
print("Time taken:", total_time, "seconds")

print("\nQuestions to practise:")

if len(wrong_answers) == 0:
    print("Excellent! No mistakes!")

else:
    for mistake in wrong_answers:
        print("\n", mistake[0])
        print("Your answer:", mistake[1])
        print("Correct answer:", mistake[2])
        print("-------------------")

print("\nThank you for playing!")