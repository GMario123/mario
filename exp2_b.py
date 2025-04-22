print("G Mario Shilshi Raj URK24CS1145")
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping: 
            top_element = stack.pop() if stack else '#'  
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char) 

    return not stack  # If stack is empty, it's valid

print(isValid("()"))     
print(isValid("()[]{}"))   
print(isValid("(]"))      
print(isValid("([)]"))    
print(isValid("{[]}"))   

