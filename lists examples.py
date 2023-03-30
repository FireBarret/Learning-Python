def list_odds(start_num, last_num):
    ''' (int),(int) -> list(int)
    Returns the list of odd numbers in a list of integers.
    >>>list_odds(5, 20)
    5,7,9,11,13,15,17,19
    '''
    num_list = []
    for num in range(start_num, last_num + 1):
        if num % 2 != 0 :
            num_list.append(num)
    print(num_list)
    
def sum_odds(start_num,last_num):
    ''' [(int),(int)] -> (int)
    Returns the sum of the odd numbers in a range going from start_num to last_num.
    >>>sum_odds(5,20)
    96
    '''
    total_sum = 0
    for num in range(start_num, last_num + 1):
            if num % 2 != 0 :
                total_sum = total_sum + num
    print(total_sum)
    
    
