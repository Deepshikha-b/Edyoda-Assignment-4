# Write a Python program to triple all numbers of a given list of integers. Use Python map.

def lst_triple():

    #creating a list
    lst_size = int(input("Enter the size of your list : "))
    lst = []
    for i in range(1,lst_size+1):                                   

        if i == 1:
            print("Enter",lst_size,"integers for the list")

        print("Element",i,end = " : ")
        num_lst = int(input())
        lst.append(num_lst)

    print("List : ",lst)

    #Triple of list numbers
    def tri(num):
        return num * 3

    triple = list(map(tri,lst))
    print("Triple of list numbers : ", triple)

    return triple


if __name__ == "__main__":
    data = lst_triple()