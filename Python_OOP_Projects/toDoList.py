class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def mark_completed(self, item):
        item.completed = True

    def display_items(self):
        for item in self.items:
            status = "[X]" if item.completed else "[ ]"
            print(f"{status} {item.title}: {item.description}")



my_todo_list = TodoList()


item1 = TodoItem("Finish homework", "Complete Math assignment")
item2 = TodoItem("Go grocery shopping", "Buy milk, eggs, and bread")
item3 = TodoItem("Make projects","Make OOP python projects")

my_todo_list.add_item(item1)
my_todo_list.add_item(item2)
my_todo_list.add_item(item3)


my_todo_list.mark_completed(item1)
my_todo_list.mark_completed(item2)


my_todo_list.display_items()
