import pandas as pd

data = {
    "std101": {"name": "Ashish Kumar", "standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "maths": 87, "science": 89, "computer": 90, "Total": 422},
    "std102": {"name": "Abhishek Kumar", "standard": "10th", "Age": 14, "Hindi": 85, "English": 45, "maths": 48, "science": 90, "computer": 45, "Total": 313},
    "std103": {"name": "Aman", "standard": "10th", "Age": 15, "Hindi": 23, "English": 56, "maths": 78, "science": 78, "computer": 67, "Total": 302},
    "std104": {"name": "Rahul", "standard": "10th", "Age": 14, "Hindi": 45, "English": 67, "maths": 45, "science": 45, "computer": 56, "Total": 258},
    "std105": {"name": "Ruby", "standard": "10th", "Age": 13, "Hindi": 89, "English": 67, "maths": 89, "science": 93, "computer": 65, "Total": 403},
    "std106": {"name": "Suman", "standard": "10th", "Age": 13, "Hindi": 90, "English": 46, "maths": 67, "science": 67, "computer": 67, "Total": 337},
    "std107": {"name": "Saurabh", "standard": "10th", "Age": 15, "Hindi": 45, "English": 23, "maths": 34, "science": 45, "computer": 34, "Total": 181},
    "std108": {"name": "Sumit", "standard": "10th", "Age": 14, "Hindi": 23, "English": 45, "maths": 67, "science": 78, "computer": 90, "Total": 303},
    "std109": {"name": "Kamlash", "standard": "10th", "Age": 15, "Hindi": 45, "English": 56, "maths": 78, "science": 99, "computer": 67, "Total": 345},
    "std110": {"name": "Rohan", "standard": "10th", "Age": 15, "Hindi": 34, "English": 12, "maths": 24, "science": 45, "computer": 57, "Total": 172}
}

df = pd.DataFrame.from_dict(data, orient='index')

# Students who scored greater than 50 in English
students_english_gt_50 = df[df['English'] > 50]
print("Students who scored greater than 50 in English:\n", students_english_gt_50)

# Top 4 students in Maths
top_4_maths = df.nlargest(4, 'maths')
print("Top 4 students in Maths:\n", top_4_maths)

# Students with minimum 60 scores in Computer Science
students_computer_min_60 = df[df['computer'] <=60]
print("Students with minimum 60 scores in Computer Science:\n", students_computer_min_60)