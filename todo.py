def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            tasks = f.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    print("📋 لیست کارهای احمد جان:")
    if not tasks:
        print("هیچ کاری ثبت نشده 😴")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("➕ یه کار جدید وارد کن: ").strip()
    if new_task:
        tasks.append(new_task)
        print("✅ کار اضافه شد:", new_task)
    else:
        print("❌ ورودی خالی بود احمد جان!")

if __name__ == "__main__":
    print("📝 AhmadToDo - لیست کارهای فرم‌کُش احمد جان 😤")
    tasks = load_tasks()
    while True:
        print("\n1. نمایش کارها\n2. اضافه کردن کار\n3. خروج")
        choice = input("🔧 انتخاب کن (1-3): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            print("👋 خداحافظ احمد جان!")
            break
        else:
            print("❌ انتخاب نامعتبره!")
