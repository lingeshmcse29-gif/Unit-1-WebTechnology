quiz = [
    ["What is 2 + 2?", "a) 3 b) 4 c) 5 d) 6", "b"],
    ["Which language is used to create websites?", "a) Python b) C c) HTML d) Java", "c"],
    ["What does CPU stand for?", "a) Central Process Unit b) Central Processing Unit c) Computer Personal Unit d) Central Program Unit", "b"],
    ["Which symbol is used for comments in Python?", "a) // b) <!-- --> c) # d) **", "c"],
    ["Which keyword is used to define a function in Python?", "a) function b) def c) fun d) define", "b"]
]

score = 0

print("MCQ Quiz\n")

for i in range(len(quiz)):
    print(i + 1, quiz[i][0])
    print(quiz[i][1])

    answer = input("Your answer: ").lower()

    if answer == quiz[i][2]:
        score += 1
        print("Correct!\n")
    else:
        print("Wrong!\n")

print("Quiz Completed")
print("Your Score:", score, "/", len(quiz))
