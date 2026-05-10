#collect a tray of numbers for a specific number of lists
#use a random generator to pick from the lists
#create a variable that subtracts both elements from the lists




import random

def random_subtraction():
        
    number = int(input("How many questions would you like to answer[10,20,25,30...etc]: "))
    
#    number_one = random.randint(1, 1000+1)
#    number_two = random.randint(0, number_one)

#    subtraction_problems = (f"What is the subtraction of the two values\n\t\t{number_one} - {number_two}")
#    return subtraction_problems
    def present_problems(number):
        correct_score = 0
        count = 1

        while(count <= number): 
            number_one = random.randint(1, 99+1)
            number_two = random.randint(0, number_one)

            print(f"------------------QUESTION {count}------------------\n")
            print(f"What is the subtraction of the two values\n\t\t{number_one} - {number_two}")

            answer = number_one - number_two

            user_attempts = int(input("Enter your answer: "))

            if (user_attempts == answer):
                print("Correct! you genius :}\n")
                correct_score+=1

            else: 
                user_attempts = int(input("Wrong.. re-enter the correct answer: "))
                if user_attempts == answer:
                    print("Bravo! you headmaster ;)\n")
                    correct_score+=1
                else:
                    print(f"Wrong still ]:\nWhat is wrong with you!\nHere... {answer} dub\n")
            count+=1
        print("----------------------- Your Result-----------------------")
        if correct_score == (count-1):
            result = f"You Einstein! ;P {correct_score}/{count-1}"
            return result
        elif correct_score >= (count-1)/2 and correct_score < (count-1):
            result = f"You passed! :] {correct_score}/{count-1}"
            return result
        elif correct_score >= 0 and correct_score < (count-1)/2:
            result = f"Fuuuailed!! :[ {correct_score}/{count-1}"
            return result
            
        #return "Error"

    student_correct_score = present_problems(number)
    return student_correct_score

#def user_attempts(number):
#    amount_of_questions = present_problems(number)

#print(random_subtraction())
