def print_table(n: int):
    print(f"\n Multiplication Table")
    for i in range(1, 13):
        # :2d and :3d right-aligns numbers by 2 and 3 spaces
        print(f"{n:2d} x {i:2d} = {n * i:3d}")

while True:
    try:
        user_input = int(input("Enter a number (1-12) to generate a table: "))
        if 1 <= user_input <= 12:
            print_table(user_input)
            break
        else:
            print("Error: Number must be between 1 and 12. Please try again.")
    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Print ALL tables 1-12
show_all = input("\nWould you like to see all tables from 1-12? (y/n): ").lower()
if show_all == 'y':
    for num in range(1, 13):
        print_table(num)
