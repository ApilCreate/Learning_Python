#Tuple


# def main():
#     student = get_student()
#     if student[0] == "Soni":
#         student[1] = "Bharatpur"
    
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     n = input("Name: ")
#     h = input("House: ")
#     # return (n, h) This makes the key values unchangeable later if called.
#     # This makes the key's value change if called later ->
#     return [n, h] 

# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()


def main():

    stu = get_students(3)

    for i in stu:
        if i['name'] == 'Soni':
            i['address'] = '10 for now but 12 in future'
        print(f"{i['name']} is from {i['address']} with a id {i['id']}")


def get_students(n):
    students = []

    for i in range(n):
        student = {}
        student["id"] = i + 1
        student["name"] = input("Enter your name: ")
        student["address"] = input("Enter your address: ")
        students.append(student)

    return students

if __name__ == "__main__":
    main()