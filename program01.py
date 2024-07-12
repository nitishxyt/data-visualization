from tabulate import tabulate

stdid = ["std101", "std102", "std103", "std104", "std105", "std106", "std107", "std108", "std109", "std110"]
stdname = ["Ashish Kumar", "Abhishek Kumar", "Aman", "Rahul", "Ruby", "Suman", "Saurabh", "Sumit", "Kamlash", "Rohan"]
standard = ["10th", "10th", "10th", "10th", "10th", "10th", "10th", "10th", "10th", "10th"]
Age = [15, 14, 15, 14, 13, 13, 15, 14, 15, 15]
Hindi = [67, 85, 23, 45, 89, 90, 45, 23, 45, 34]
English = [89, 45, 56, 67, 67, 46, 23, 45, 56, 12]
maths = [87, 48, 78, 45, 89, 67, 34, 67, 78, 24]
science = [89, 90, 78, 45, 93, 67, 45, 78, 99, 45]
computer = [90, 45, 67, 56, 65, 67, 34, 90, 67, 57]
Total = [422, 313, 302, 258, 403, 337, 181, 303, 345, 172]

combined_list = []

for i in range(len(stdid)):
    combined_list.append((
        stdid[i], stdname[i], standard[i], Age[i],
        Hindi[i], English[i], maths[i], science[i],
        computer[i], Total[i]
    ))

headers = ["stdid", "stdname", "standard", "Age", "Hindi", "English", "maths", "science", "computer", "Total"]

# Print the table
print(tabulate(combined_list, headers, tablefmt="grid"))

# Students who scored greater than 50 in English
english = [stdname[i] for i in range(len(stdid)) if English[i] > 50]
print("\nStudents who scored greater than 50 in English:")
for student in english:
    print(student)

# Top 4 in Maths
math_top_4 = sorted([(maths[i], stdname[i], Age[i]) for i in range(len(maths))], reverse=True)[:4]
print("\nMath top 4:")
for score, name, age in math_top_4:
    print(f"{name} - Age: {age}, Score: {score}")

# Minimum 3 scores in Computer Science
computer_bottom = sorted([(computer[i], stdid[i], stdname[i], Age[i]) for i in range(len(computer)) ])[:3]
print("\nStudents with the lowest 3 scores in Computer Science:")
for score, std_id, name, age in computer_bottom:
    print(f"ID: {std_id}, Name: {name}, Age: {age}, Score: {score}")
