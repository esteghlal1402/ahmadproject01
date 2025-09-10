def encrypt_file(filename, key=3):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        encrypted = ''.join([chr(ord(char) + key) for char in content])
        with open(filename + '.enc', 'w', encoding='utf-8') as f:
            f.write(encrypted)
        print("🔐 فایل رمزنگاری شد:", filename + '.enc')
    except FileNotFoundError:
        print("❌ فایل پیدا نشد احمد جان!")

def decrypt_file(filename, key=3):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        decrypted = ''.join([chr(ord(char) - key) for char in content])
        with open(filename.replace('.enc', '.dec'), 'w', encoding='utf-8') as f:
            f.write(decrypted)
        print("🔓 فایل رمزگشایی شد:", filename.replace('.enc', '.dec'))
    except FileNotFoundError:
        print("❌ فایل پیدا نشد احمد جان!")

if __name__ == "__main__":
    print
