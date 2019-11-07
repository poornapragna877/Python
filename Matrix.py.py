import random

matrix=[]

for i in range (6):               #generating a random 6x6 Matrix 
    a=[]
    for j in range (6):
        a.append(random.randint(-10,100)) #can alter the domain accordingly
    matrix.append(a)
for i in range (6):
    
    for j in range (6):

        print(matrix[i][j],end=" ")  
    print(" ")
entry_row=-61                     #min possible case as defined domain considered
for i in range (6):               #starting with the row having maximim sum
    row_sum=0
    for j in range (6):
        row_sum=row_sum+matrix[i][j]
    #print(row_sum)
    if entry_row < row_sum :
            entry_row=row_sum
            row_no=i
print("Entry @ row:",++row_no)
#exit_sum=col_sum=n=0
col_sum=x=0
for i in range (row_no+1,6):          #going down
    col_sum=col_sum+matrix[i][5]
#print(col_sum)
    return_sum=0
    for j in range (5,-1,-1):
        return_sum=return_sum+matrix[i][j]
   # print(return_sum)
    if x<col_sum+return_sum :
            x=col_sum+return_sum
            exit_row=i
#print(exit_row,row_no)

col_sum=y=0
for i in range (row_no-1,-1,-1):          #going up
    col_sum=col_sum+matrix[i][5]
#print(col_sum)
    return_sum=0
    for j in range (5,-1,-1):
        return_sum=return_sum+matrix[i][j]
    #print(return_sum)
    if y<col_sum+return_sum :
            y=col_sum+return_sum
            exit_rowup=i

if max(x,y)==x:                     #optimizing
    if max(x,entry_row)==x:
        print("Exit @ row:",++exit_row)
    else:
        print("Exit @ row:",++row_no)
else:
    if max(y,entry_row)==y:
        print("Exit @ row:",++exit_rowup)
    else:
        print("Exit @ row:",++row_no)
    
