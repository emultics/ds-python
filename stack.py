##implementation of stack
#1. push 2. pop 3. isEmpty 4. peek(get top of stack's element without removing it)

class Stack:
    def __init__(self, stack:list=[]):
        self.stack = stack

    def push(self,item):
        self.stack.append(item)
        print(f'pushed item:  {item}')

    def __pop(self):
        if(self.isEmpty()):
            return "Stack is Empty"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack)==0

    def length(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]
    
    def removeElementFromStack(self):
        while(self.isEmpty()==False):
            command = input("Do you want to pop? [y/N]")
            if(command=='Y' or command =='y'):
                element = self.__pop()
                print(f'{element} is popped from the stack')
            else:
                break

        

if __name__ == '__main__':
    ##stack of even number
    
    listEvenNumber = [i for i in range(0,10,2)]
    print(len(listEvenNumber))
    stackOfEvenNumber = Stack(listEvenNumber)

    #stack of odd Number
    listOfOddNumber = [i for i in range(1,10,2)]
    stackOfOddNumber = Stack(listOfOddNumber)

    # for indexOfEven in range(len(listEvenNumber)):
    #     print(indexOfEven)
    #     stackOfEvenNumber.push(listEvenNumber[indexOfEven])
    # print("=====")
    # for indexOfOdd in range(len(listOfOddNumber)):
    #     stackOfOddNumber.push(listOfOddNumber[indexOfOdd])
    
    print("==pop===")
    # stackOfEvenNumber.removeElementFromStack()
    print(stackOfEvenNumber.peek())
    
          
    


    
