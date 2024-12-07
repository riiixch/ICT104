std_id = input("Std ID : ")
std_name = input("Std Name : ")
score_1 = input("Score 1 : ")
score_2 = input("Score 2 : ")

total_score = int(score_1) + int(score_2)

grade = ""

if total_score >= 80:
    grade = "A"
elif total_score >= 75:
    grade = "B+"
elif total_score >= 70:
    grade = "B"
elif total_score >= 65:
    grade = "C+"
elif total_score >= 60:
    grade = "C"
elif total_score >= 55:
    grade = "D+"
elif total_score >= 50:
    grade = "D"
else:
    grade = "F"

print("********************")
print("Std ID :", str(std_id))
print("Std Name :", str(std_name))
print("Score 1 :", int(score_1))
print("Score 2 :", int(score_2))
print("Total Score :", int(total_score))
print("Grade :", str(grade))
print("********************")