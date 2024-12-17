day = input("What day is it: ")

match day:
  case 'Monday'| 'Tuesday'| 'Wednesday' :
    print("This is a weekday!") 

  case 'Saturday' |'Sunday'  :
    print("This is a weekend!")
