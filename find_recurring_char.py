# find the first recurring character,return the recurring character
def find_recurring_char(arr):
    recur_list = {}
    for item in arr:
        if item in recur_list:
            return item
        else:
            recur_list[item] = True
    return False

print(find_recurring_char([2,1,1,5,6,2]))
