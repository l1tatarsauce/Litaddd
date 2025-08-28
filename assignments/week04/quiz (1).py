
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()


"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = # Your code here
    odd_numbers = # Your code here
    
    # Calculate average
    average = # Your code here
    
    # Numbers greater than average
    above_average = # Your code here
    
    # Display results
    # Your code here

if __name__ == "__main__":
    number_operations()


3.    
scores = [78, 85, 92, 67, 88, 95, 73, 84]

# 1. คะแนนสูงสุด

max_score = max(scores)

# 2. คะแนนต่ำสุด

min_score = min(scores)

# 3. คะแนนเฉลี่ย

avg_score = sum(scores) / len(scores)

# 4. จำนวนคนที่ได้คะแนน > 80

count_over_80 = sum(1 for s in scores if s > 80)

print("คะแนนสูงสุด:", max_score)

print("คะแนนต่ำสุด:", min_score)

print("คะแนนเฉลี่ย:", avg_score)

print("จำนวนคนที่ได้คะแนน > 80:", count_over_80)
 


2.
def check_grade(score):

    if score >= 80:

        return "very good"

    elif score >= 70:

        return "good"

    elif score >= 60:

        return "normal"

    else:

        return "should be improved"

# ทดสอบฟังก์ชัน

scores = [85, 75, 65, 55]

for s in scores:

    print(f"Score {s}: {check_grade(s)}")





1.
    student_name = "Alice"
midterm = 85
final = 92
homework = 88
# คำนวณเกรดรวม
total_grade = (midterm * 0.3) + (final * 0.4) + (homework * 0.3)
# แสดงผลลัพธ์
print(f"{student_name} total grade = {total_grade:.1f}")
 