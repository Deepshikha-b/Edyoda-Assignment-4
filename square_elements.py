# Write a Python program to square the elements of a list using map() function.

def sq():

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
    
    def square(num):
        return num ** 2

    lst_square = list(map(square,lst))
    print("Square of elements of the list : ", lst_square)
    
    return lst_square

if __name__ == "__main__":
    data = sq()