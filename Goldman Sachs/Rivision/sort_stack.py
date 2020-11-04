def sort_stack_increasing(stack,output):
    while stack:
        temp = stack.pop()

        while output and output[-1] > temp:
            stack.append(output.pop())
        
        output.append(temp)
    return output

def sort_stack_decreasing(stack,output):
    while stack:
        temp = stack.pop()

        while output and output[-1] < temp:
            stack.append(output.pop())

        output.append(temp)
    return output


def main():
    stack = [34,3,31,98,92,23]
    new_stack = stack.copy()
    increasing = []
    increasing = sort_stack_increasing(stack,increasing)
    print(increasing)

    decreasing = []
    decreasing = sort_stack_decreasing(new_stack,decreasing)
    print(decreasing)

main()