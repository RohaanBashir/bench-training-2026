def grade_classifier(score: int) -> str:
    if score >= 90:
        return "Distinction"
    elif score >= 60: 
        return "Pass"
    else:
        return "Fail"

def test_grade_classifier():
    test_cases = [95, 75, 45, 60, 89]
    for test_score in test_cases:
        print(f"Testing Score: {test_score} -> Result: {grade_classifier(test_score)}")
    print()

#testing grade classifier function
test_grade_classifier()
scores = [45, 72, 91, 60, 38, 85]

for score in scores:
    print(f"Score: {score}, Grade: {grade_classifier(score)}")
