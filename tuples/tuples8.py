# Write a Python program that has two sequences. First which stores some questions
# and second stores the corresponding answers.
# Use the zip() function to form a valid question-answer series.
# Sample check:
# Ques= ["Roll_No", "Name", "Course"]
# Ans= [7, "Sourav", "BSc"]
# Output:
# The zipped result is : [('Roll_No', 7), ('Name', 'Sourav'), ('Course', 'BSc')]


Ques= ["Roll_No", "Name", "Course"]
Ans= [7, "Sourav", "BSc"]

Result=list(zip(Ques,Ans))
print(Result)