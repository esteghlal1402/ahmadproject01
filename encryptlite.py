# AhmadEncryptLite - رمزنگاری ساده با کلید ثابت
def encrypt(text):
    key = 3
    return ''.join([chr(ord(char) + key) for char in text])

def decrypt(text):
    key = 3
    return ''.join([chr(ord(char) - key) for char in text])

if __name__ == "__main__":
    msg = "سلام"
    enc = encrypt(msg)
    dec = decrypt(enc)
    print("رمزنگاری:", enc)
    print("رمزگشایی:", dec)
