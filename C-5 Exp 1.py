print("Name : Jeev therese v mathew ")
print("Admission No: A24MCA034")
print("Experiment No: 15")


with open("file.txt", "r") as file:
    lines = [line.strip() for line in file]
    print("lines are:", lines)
