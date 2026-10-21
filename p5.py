#Name: Vishvrajsinh zala
#Eno : 92600584082
# Write a program to solve Tower of Hanoi problem 

#Tower of Hanoi problem

def tower_of_hanoi(n, source, helper, destination):

    if n ==1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, helper, source, destination)

#number of disks
n = int(input("Enter number of disks: "))

# solve tower of Hanoi
tower_of_hanoi(n, "A", "B", "C")

# Total number of moves
print("Total moves:", (2 ** n) -1)
