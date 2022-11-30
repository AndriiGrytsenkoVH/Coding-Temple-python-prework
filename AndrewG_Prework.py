#question 1
def hello_name(user_name):
    print("hello_" + user_name  + "!")

# user = "USER"
# hello_name(user)

#question 2
def first_odds():
    for i in range(1,100,2):
        print(i)

#first_odds()

#question 3
def max_num_in_list(a_list):
    return max(a_list)

#test_list = [1,2,300,4,5,]
#print(max_num_in_list(test_list))

#question 4
def is_leap_year(a_year):
    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)

#years = [1800,1900,2000,2001,2004]
#must be F F T F T
#print(list(map(is_leap_year, years)))

#question 5
#implied that len(a_list) >= 2
def is_consecutive(a_list):
    for i in range(1,len(a_list)):
        if (a_list[i] - a_list[i-1]) != 1:
            return False
    return True

# num_list = [1,2,3,4,6]
# print(is_consecutive(num_list))

