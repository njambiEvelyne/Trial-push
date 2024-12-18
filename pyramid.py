#Define the height of the pyramid
rows = 5
#Initialize the outer loop for the number of rows
i= 0

while i < rows: 
    #Initialize the loop for creating spaces
    j = 0
    while j <rows -i -1:
         print("", end = "") #Print spaces
         j += 1
#Initialize the inner loop for printinh=g the asterick
    k=0
    while k <2 * i+ 1:
         print("*", end="")
         k +=1
#Move to the next line after each row has been printed
    print() 
    #Increment the row counter    
    i+=1


    
