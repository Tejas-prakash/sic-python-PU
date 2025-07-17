from data_loader import load_data
from visualizer import (
    plot_summary_chart,
    show_waste_vs_consumed,
    suggest_reduction_ideas,
    suggest_redirection_options,
)

def menu():
    print("\n===== Food Wastage Management System =====")
    print("1. Show Summary Chart")
    print("2. Show Wasted vs Consumed Comparison")
    print("3. How to Reduce Food Wastage")
    print("4. Where Wasted Food Can Be Redirected")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def main():
    df = load_data()
    while True:
        choice = menu()
        if choice == '1':
            plot_summary_chart(df)
        elif choice == '2':
            show_waste_vs_consumed(df)
        elif choice == '3':
            suggest_reduction_ideas()
        elif choice == '4':
            suggest_redirection_options()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
