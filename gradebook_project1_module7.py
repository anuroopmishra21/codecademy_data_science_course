last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ['physics','calculus','poetry','history']
subjects.append('computer_science')
grades = [98,97,85,88]
grades.append(100)
gradebook = list(zip(subjects,grades))
gradebook.append(('visual_arts',93))
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
