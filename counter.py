def count_text(text):
    char_count = len(text)
    word_count = len(text.split())
    return char_count, word_count

if __name__ == "__main__":
    print("🔢 AhmadCounter - شمارش متن احمد جان 😤")
    user_input = input("🧠 یه جمله وارد کن: ")
    chars, words = count_text(user_input)
    print(f"🔠 تعداد حروف: {chars}")
    print(f"📝 تعداد کلمات: {words}")
