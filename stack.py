class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,data):
        return self.items.append(data)

    def pop(self):
        return self.items.pop()

    def display(self):
        print(self.items)

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def quit(self):
        exit()

if __name__ == '__main__':
    st = stack()
    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Display")
        print("4.Top")
        print("5.Size")
        print("6.Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter value want to push: ")
            st.push(data)
        if choice == 2:
            st.pop()
        if choice == 3:
            st.display()
        if choice == 4:
            print(st.top())
        if choice == 5:
            print(st.size())
        if choice ==6:
            st.quit()
