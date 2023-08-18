# Question 1
def hello_name(user_name):
    print(f"hello_{user_name.upper()}!")

#Question 2 
def first_odds():
    for i in range(1, 100):
        if i % 2 == 1:
            print(i)

#Question 3
def max_num_in_list(a_list):
    max_num = 0
    for i in a_list:
        if i > max_num:
            max_num = i
    return max_num

#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False    
        else:
            return True
    else: 
        return False

#Question 5
def is_consecutive(a_list):
    # holds value of first element in list
    last_number = a_list[0]

    """ goes through list and checks if element is == last_number, if not then 
        checks whether element is consecutive or not """
    for element in a_list:
        if element == last_number:
            continue
        elif element == last_number + 1:
            last_number = element
        else:
            break

    """ if loop reaches end of list, checks if last element is consecutive then
        returns bool value whether list is consecutive or not """
    if element == a_list[-1]:
        # Checks if last element in list is consecutive
        if element - 1 == a_list[-2]:
            return True
        else:
            return False
    else:
        return False