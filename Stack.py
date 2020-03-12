
def isfull():
    if top == capacity-1: #index of last element is capacity-1,becasuse index start at zero
        return True
    else:
        return False
def isempty():
    if top == -1:
        return True
    else:
        return False

def display():
    if(isempty()):
        print('Stack is empty')
    else:
        print('Stack :')
        print(stack[:top+1])

def pop():
    global top
    if(isempty()):
        print('Stack is empty')
    else:
        top -= 1
        display()
def push(num):
    global top
    if(isfull()):
        print('stack is full')
    else:
        top+=1
        stack[top]=num
        display()

#set capacity of the stack
capacity = int(input('Enter size of stack\n'))

#initialize stack with capacity
stack = [None] * capacity

#stack is empty ,top is set to -1
top = -1


choice=0
while(choice<=2):
    choice=int(input('1:push\n2:pop\n'))
    if(choice == 1):
        num = int(input('Enter element to push :\n'))
        push(num)
    elif(choice == 2):
        pop()
    else:
        break
