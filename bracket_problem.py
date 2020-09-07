'''Given a string expression, check if brackets present in the expression are balanced or not. Brackets are balanced if the bracket which opens last, closes first.
You need to return true if it is balanced, false otherwise.'''




def check_balanced(string):
  l1=[]

  for i in string:
    if i in '{[(':
      l1.append(i)

    else:
      if i==')':
        if len(l1)==0 or l1[-1]!='(':
          return False
        l1.pop()

      if i=='}':
        if len(l1)==0 or l1[-1]!='{':
          return False
        l1.pop()

      if i==']':
        if len(l1)==0 or l1[-1]!='[':
          return False
        l1.pop()

  return True

    

        













string=input()
print(check_balanced(string))