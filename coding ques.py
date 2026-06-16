def missing_num(lst):
    for i in range(1,11):
        if i not in lst:
            return i
print(missing_num([1,2,3,4,6,7,8,9,10]))
def alphabet_soup(text):
    return "".join(sorted(text))
print(alphabet_soup("hello"))
print(alphabet_soup("edabit"))
def return_only_integer(lst):
    result=[]
    for item in lst:
        if type(item)== int:
            result.append(item)
    return result
print(return_only_integer([9,2,"space","car","lion",16]))

def is_in_order(text):
    return text=="".join(sorted(text))
print(is_in_order("abc"))
print(is_in_order("edabit"))
print(is_in_order("123"))

def unique(lst):
    for num in lst:
        if lst.count(num)==1:
            return num
print(unique([3,3,3,7,3,3]))
print(unique([0,0,0.77,0,0]))


      