def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def my_sort(lst):
    try:

        for num in lst:
            if num <= 0:
                raise ValueError("Faqat musbat sonlar kiritilishi kerak.")
        
        sorted_lst = sorted(lst, key=digit_sum)
        return sorted_lst
    
    except ValueError as e:
        print(e)
        return []

def get_user_input():
    lst = []
    n = int(input("lsit uzunligini kiriting: "))
    try:
        for i in range(n):
            elm = int(input(">>> "))
            lst.append(elm)
        return lst
    
    except ValueError:
        print("Noto'g'ri kiritish! Iltimos, faqat butun sonlarni kiriting.")
        return []

input_list = get_user_input()
sorted_list = my_sort(input_list)
print(sorted_list)