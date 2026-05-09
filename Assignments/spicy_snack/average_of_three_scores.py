#collect score 1, score2, and score3
#find the average by dividing it by the amount of scores intake
#give the scores conditions buy attacing it to a grade


def average_score(score_one,score_two,score_three):
#    if (score_one,score_two,score_three) >= 0 and (score_one,score_two,score_three) <= 100:
     average = (score_one + score_two + score_three) // 3
     if average >= 90 and average <= 100:
        return 'A'
     elif average >= 80 and average <= 89:
        return 'B'
     elif average >= 70 and average <= 79:
        return 'C'
     elif average >= 60 and average <= 69:
        return 'D'
     elif average >= 0 and average <=59:
        return 'F'
     else:
        return "Invalid Score Grade"
            
        
#    else:
#        return "Invalid Input"

print(average_score(56,69,97))
