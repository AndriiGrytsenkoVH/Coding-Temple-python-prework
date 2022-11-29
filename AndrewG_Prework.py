def hello_name(user_name):
    print("hello_" + user_name  + "!")
    #return


#doesn't work. freezes.

#user = input()
#hello_name(user)
#input()

def first_odds():
    for i in range(1,100,2):
        print(i)

#first_odds()

def max_num_in_list(a_list):
    return max(a_list)

#test_list = [1,2,300,4,5,]
#print(max_num_in_list(test_list))

def is_leap_year(a_year):
    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)

#years = [1800,1900,2000,2001,2004]
#must be F F T F T
#print(list(map(is_leap_year, years)))

#problem 5

#implied that len(a_list) >= 2
def is_consecutive(a_list):
    for i in range(len(a_list)-1):
        
    return True

