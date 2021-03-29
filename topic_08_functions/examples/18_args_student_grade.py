def print_scores(student, *scores):
    print(f"Student Name: {student}")
    for score in scores:
        print(score)


print_scores("Lily", 100, 95, 88, 92, 99)
"""
Student Name: Lily
100
95
88
92
99
"""