import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

# Load data once for use in multiple options
df, daily_summary = load_data()


def show_menu():
    print("\n--- Food Wastage Management Menu ---")
    print("1. View Daily Food Summary Chart")
    print("2. Food Wasted vs Taken Percentage")
    print("3. Tips to Reduce Food Wastage")
    print("4. Suggestions to Redirect Wasted Food")
    print("0. Exit")


def view_daily_summary():
    plt.figure(figsize=(14, 6))
    plt.plot(daily_summary.index, daily_summary['Food_Prepared_kg'], label='Food Prepared', marker='o')
    plt.plot(daily_summary.index, daily_summary['Food_Consumed_kg'], label='Food Consumed', marker='o')
    plt.plot(daily_summary.index, daily_summary['Total_Food_Wasted_kg'], label='Food Wasted', marker='o')
    plt.title('Daily Hostel Food Prepared, Consumed, and Wasted')
    plt.xlabel('Date')
    plt.ylabel('Kilograms')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def view_wastage_percentage():
    avg_percentage = df['Wasted_Percentage'].mean()
    print(f"\nAverage Food Wasted Compared to Prepared: {avg_percentage:.2f}%")
    print("This means for every 100 kg prepared, about {:.2f} kg is wasted.".format(avg_percentage))


def tips_to_reduce_wastage():
    print("\n--- Tips to Reduce Food Wastage ---")
    tips = [
        "1. Create awareness among students to only take what they can eat.",
        "2. Use pre-ordering systems to predict actual consumption.",
        "3. Provide half-plate or trial options for uncertain students.",
        "4. Display wastage statistics in dining areas to discourage excess.",
        "5. Engage hostel committees to monitor and analyze wastage daily."
    ]
    print("\n".join(tips))


def suggestions_for_redirection():
    print("\n--- Suggestions to Redirect Wasted Food ---")
    suggestions = [
        "1. Partner with NGOs that collect leftover edible food.",
        "2. Create compost pits from food scraps to benefit hostel gardens.",
        "3. Collaborate with nearby shelters or animal care centers.",
        "4. Convert inedible waste to biogas through local waste plants.",
        "5. Store excess properly and reuse safely for the next meal if hygienic."
    ]
    print("\n".join(suggestions))


if __name__ == '__main__':
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            view_daily_summary()
        elif choice == '2':
            view_wastage_percentage()
        elif choice == '3':
            tips_to_reduce_wastage()
        elif choice == '4':
            suggestions_for_redirection()
        elif choice == '0':
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
