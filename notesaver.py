def save_note(note, filename="notes.txt"):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(note + "\n")
    print("✅ یادداشت ذخیره شد.")

def show_notes(filename="notes.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            notes = f.readlines()
        print("📒 یادداشت‌های ذخیره‌شده:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("❌ هنوز هیچ یادداشتی ذخیره نشده.")

if __name__ == "__main__":
    print("📝 AhmadNoteSaver - ذخیره‌ساز یادداشت احمد جان 😤")
    while True:
        print("\n1. اضافه کردن یادداشت\n2. نمایش یادداشت‌ها\n3. خروج")
        choice = input("🔧 انتخاب کن (1-3): ").strip()
        if choice == "1":
            note = input("🧠 یادداشتت رو بنویس: ").strip()
            if note:
                save_note(note)
            else:
                print("❌ یادداشت خالی بود احمد جان!")
        elif choice == "2":
            show_notes()
        elif choice == "3":
            print("👋 خداحافظ احمد جان!")
            break
        else:
            print("❌ انتخاب نامعتبره!")
