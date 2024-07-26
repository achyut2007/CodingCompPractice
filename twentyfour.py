# a = 'A+B*C-D'
# # ((A+(B*C))-D) = [ABC*+]-D = ABC*+D-
# stk = []
# output = []
# p = {
#     '+':1,
#     '-':1,
#     '*':2,
#     '/':2
# }
# for i in range(len(a)):
#     if a[i] in '+-*/' and stk == []:
#         stk.append(a[i])
#     elif a[i] in '+-*/' and p[stk[-1]]<p[a[i]]:
#         stk.append(a[i])
#     elif a[i] in '+-*/' and p[stk[-1]]>=p[a[i]]:
#         while p[stk[-1]]>=p[a[i]]:
#             w=stk.pop()
#             output.append(w)
#     else:
#         output.append(a[i])
#         print(output)
#         print(stk)
# print(str(output))

### Shunting-yard algorithm implementation

# Define the operator precedence table
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Input infix expression
infix_expr = 'A+B*C-D'

# Initialize empty stacks for operators and output
operator_stack = []
output = []

# Iterate through each character in the infix expression
for char in infix_expr:
    # If the character is an operator
    if char in precedence:
        # While the operator stack is not empty and the top operator has higher or equal precedence
        while operator_stack and precedence[operator_stack[-1]] >= precedence[char]:
            # Pop the top operator from the stack and append it to the output
            output.append(operator_stack.pop())
        # Push the current operator onto the stack
        operator_stack.append(char)
    else:
        # If the character is not an operator, simply append it to the output
        output.append(char)

    # Print the current state of the output and operator stack
    print(f"Output: {output}")
    print(f"Operator Stack: {operator_stack}")

# After iterating through the entire infix expression, pop any remaining operators from the stack
while operator_stack:
    output.append(operator_stack.pop())

# Print the final postfix expression
print(f"Postfix Expression: {output}")