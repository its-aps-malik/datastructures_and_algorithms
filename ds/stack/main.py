class my_stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = []*self.size

    def get_size(self):
        return(self.size)

    def push(self, val) -> int:
        if self.top < self.size-1:
            self.top += 1
            self.arr.append(val)
            print(f'{val} pushed into stack !')
        else:
            print(f'stack overflow !!! Can\'t push {val}')

    def pop(self):
        if self.top > -1:
            print(f'{self.arr[self.top]} popped from stack !')
            self.top -= 1
            return(self.arr.pop())
        else:
            print(f'stack empty !!! Can\'t pop anything !')
    
    def peek(self):
        if self.top == -1:
            print('Stack empty !!!')
        else:
            print(f'current top value = {self.arr[self.top]}')

if __name__ == "__main__":

    print(f'please enter the size of the array : ', end='')
    flag = True
    size = None
    while flag:
        try:
            size = int(input())
            flag = False
        except:
            print(f'please enter a valid integer : ', end='')

    obj = my_stack(size)

    flag = True
    while(flag):
        print('Select an option : \n1. Push into stack\n2. Pop from stack\n3. peek top element\n4. Exit')
        flag2 = True
        val = None
        while flag2:
            try:
                val = int(input())
                flag2 = False
            except:
                print('please select a correct option : ')
        if val == 1:
            print('Please enter the value to be pushed : ',end='')
            data = input()
            obj.push(data)
        elif val == 2:
            obj.pop()
        elif val == 3:
            obj.peek()
        elif val == 4:
            flag = False
            print('Exiting execution !!')
        else:
            print('please select a correct option : ')
