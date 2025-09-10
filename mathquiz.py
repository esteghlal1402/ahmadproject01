import random

def ask_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(['+', '-', '*'])
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    else:
        answer = a * b
    user_input = input(f"❓ {a} {op} {b} = ")
    try:
        return int(user_input) == answer
    except ValueError:
        return False

if __name__ == "__main__":
    print("🧮 AhmadMathQuiz - آزمون ریاضی احمد جان 😤")
    score = 0
    for i in range(5):
        if ask_question():
            print("✅ درست بود!")
            score += 1
        else:
            print("❌ اشتباه بود!")
    print(f"🎯 امتیاز نهایی: {score} از 5")
