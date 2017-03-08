def fizz_buzz(z):
  if(z % 3 == 0 and z % 5 == 0):
    return'FizzBuzz'
  elif(z % 3) == 0:
    return 'Fizz'
  elif(z %5) == 0:
    return 'Buzz'
  else:
    return(z)
