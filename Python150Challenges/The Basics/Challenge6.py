# 006  Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left and display the answer in a userfriendly format.

total_slices = int(input("Enter total no.of slices before eating: "))
slices_eaten = int(input("Enter no. of slices eaten: "))
slices_remaining = total_slices - slices_eaten
print("Slices left to eat:", slices_remaining)
