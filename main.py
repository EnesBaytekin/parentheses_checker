

class Stack:
    def __init__(self):
        self.items = []
        self.top = 0
    def push(self, item):
        self.top += 1
        self.items.append(item)
    def pull(self):
        self.top -= 1
        return self.items.pop()
    def peek(self):
        return self.items[-1]

def get_text():
    file = open("text.txt")
    text = file.read().strip()
    file.close()
    return text

def check(text):
    stack = Stack()
    for c in text:
        if c in ("(", "["):
            stack.push(c)
        elif c in (")", "]"):
            if stack.top == 0:
                return False
            o = stack.pull()
            if   o == "(" and c == ")": pass
            elif o == "[" and c == "]": pass
            else:
                return False
        # print(stack.items, stack.top)
    if stack.top > 0:
        return False
    return True

def main():
    text = get_text()
    if check(text):
        print("brackets are matched correctly")
    else:
        print("brackets are not matched")

if __name__ == "__main__":
    main()
