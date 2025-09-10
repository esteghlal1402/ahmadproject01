import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 AhmadPasswordGen - سازنده رمز فرم‌کُش احمد جان 😤")
    try:
        user_input = int(input("🧠 طول رمز عبور رو وارد کن: "))
        password = generate_password(user_input)
        print("🔑 رمز عبور تولید شده:", password)
    except ValueError:
        print("❌ لطفاً فقط عدد وارد کن احمد جان!")
