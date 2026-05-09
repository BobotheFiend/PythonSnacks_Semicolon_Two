#TO get the number of students who passed or failed
#collect input 15 times
#set the count to loop 15 times for that and while doing that, store each scores based on the pass mark
#if it is 45 and above it should store as a pass
#and fail for less than 45
#THEN PRINT THE THE RESULT

pass_score = 0
fail_score = 0
for count in range(15):
    students_score = int(input("Enter students score: "))
    if (students_score >= 45):
        pass_score +=1
        #print(pass_score)
        
    else:
        fail_score +=1
        #print(fail_score)
        
print(f"The number of pass scores is {pass_score}\nThe number of failed scores is {fail_score}")
