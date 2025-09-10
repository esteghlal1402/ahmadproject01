import random
import time

def dynamic_encrypt(text):
    key = random.randint(1, 9)
    encrypted = ''.join([chr(ord(char) + key) for char in text])
    return encrypted, key

def dynamic_decrypt(text, key):
    return ''.join([chr(ord(char) - key) for char in text])

def loading_effect():
    for i in range(3):
        print("فرم‌کُش در حال اجرا" + "." * (i+1))
        time.sleep(0.5)

if __name__ == "__main__":
    print("🔥 پروژه رمزنگاری احمد جان شروع شد 🔥")
    msg = input("🧠 متن مورد نظر رو وارد کن: ")
    loading_effect()
    encrypted, key = dynamic_encrypt(msg)
    print(f"🔐 متن رمزنگاری شده: {encrypted}")
    print(f"🔑 کلید رمزنگاری: {key}")
    confirm = input("✅ رمزگشایی انجام بشه؟ (y/n): ")
    if confirm.lower() == 'y':
        decrypted = dynamic_decrypt(encrypted, key)
        print(f"🧠 متن رمزگشایی شده: {decrypted}")
    else:
        print("🚫 رمزگشایی لغو شد. فرم‌کُش متوقف شد.")
