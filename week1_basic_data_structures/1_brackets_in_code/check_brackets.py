# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            elif are_matching(opening_brackets_stack[-1].char, next): # if find matching brackets
                opening_brackets_stack.pop()
            else:
                return i + 1

    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[-1].position + 1
    return -1

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == -1:
        print("Success")
    else:
        print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()