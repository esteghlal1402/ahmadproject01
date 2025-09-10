def reverse_text(text):
    return text[::-1]

if __name__ == "__main__":
    print("🔁 AhmadReverser - برگردوندن متن احمد جان 😤")
    user_input = input("🧠 یه جمله وارد کن: ")
    reversed_output = reverse_text(user_input)
    print("🔄 خروجی معکوس:", reversed_output)
