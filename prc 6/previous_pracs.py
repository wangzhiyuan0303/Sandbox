#1.Error checking
def main():
    while True:
        worker_level = int(input("Worker level: "))
        if 1 <= worker_level <= 10:
            salary = worker_level * 5000
            print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
            break
        else:
            print("Invalid worker level")
if __name__ == "__main__":
    main()

#Nested loops
def main():
    rows = int(input("Rows: "))
    columns = int(input("Columns: "))
    for _ in range(rows):
        for column_number in range(columns):
            print(column_number, end=' ')
        print()
if __name__ == "__main__":
    main()

