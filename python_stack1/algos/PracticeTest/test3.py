# Assignment: Type List


mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]
spl = []


def identify_list_type(lst):
    new_string = ''
    total = 0
    if len(lst) <1:
        return "Not a Valid List"

    for value in lst:
        if isinstance(value,int) or isinstance(value,float):
            total += value

        elif isinstance(value,str):
            new_string += value

    if new_string and total:

        print ("The array you entered is of mixed type")
        print ("String:", new_string)
        print (total)

    elif new_string:

        print("The array you entered is of String Type")
        print("String:", new_string)

    else:
        print("The array you entered is of Integer Type")
        print(total)



print(identify_list_type(spl))
