import time

def countdown(seconds):
    while seconds > 0:
        print(f"⏳ باقی‌مانده: {seconds} ثانیه")
        time.sleep(1)
        seconds -= 1
    print("🚀 تایمر تموم شد احمد جان!")

if __name__ == "__main__":
    print("⏱️ AhmadTimer - تایمر فرم‌کُش احمد جان 😤")
    try:
        user_input = int(input("🧠 چند ثانیه تایمر باشه؟ "))
        countdown(user_input)
    except ValueError:
        print("❌ لطفاً فقط عدد وارد کن احمد جان!")
