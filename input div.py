#THIS SCRIPT TAKES INPUT OF NUMBERS and DIVIDE THEM


# Store input numbers
A = input('')
D = input('')
print('YOU JUST ENTERED THE VALUE OF A={0} and D={1}'.format(A, D))
# multiply two numbers
quotient = float(A) / float(D)
remainder= float(A) % float(D)

# Display the product
print('The QUOTIENT OF A/D is {2}'.format(A, D, quotient, remainder))
print('& REMAINDER is {3}. '.format(A, D, quotient, remainder))
