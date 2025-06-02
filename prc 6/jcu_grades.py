

def determine_grade(score):
    if score < 50:
        return 'F'
    elif score < 65:
        return 'P'
    elif score < 75:
        return 'C'
    elif score < 85:
        return 'D'
    else:
        return 'HD'

def main():
    while True:
        score = float(input("Enter your score: "))
        if score < 0:
            break
        grade = determine_grade(score)
        print(f"The score {score:.1f} is {grade}")

main()

