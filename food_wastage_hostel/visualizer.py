import matplotlib.pyplot as plt
import pandas as pd


def plot_summary_chart(df):
    df['Date'] = pd.to_datetime(df['Date'])
    daily_summary = df.groupby('Date')[['Food_Prepared_kg', 'Food_Consumed_kg', 'Total_Food_Wasted_kg']].sum()

    plt.figure(figsize=(12, 6))
    plt.plot(daily_summary.index, daily_summary['Food_Prepared_kg'], label='Prepared')
    plt.plot(daily_summary.index, daily_summary['Food_Consumed_kg'], label='Consumed')
    plt.plot(daily_summary.index, daily_summary['Total_Food_Wasted_kg'], label='Wasted')
    plt.xlabel('Date')
    plt.ylabel('Kilograms')
    plt.title('Daily Hostel Food Data')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def show_waste_vs_consumed(df):
    total_wasted = df['Total_Food_Wasted_kg'].sum()
    total_consumed = df['Food_Consumed_kg'].sum()
    labels = ['Wasted', 'Consumed']
    values = [total_wasted, total_consumed]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green'])
    plt.title('Food Wasted vs Consumed')
    plt.axis('equal')
    plt.show()

def suggest_reduction_ideas():
    print("\n=== Ways to Reduce Food Wastage ===")
    print("- Encourage students to take only what they can eat.")
    print("- Monitor trends to adjust food preparation.")
    print("- Offer smaller serving portions with optional refills.")
    print("- Raise awareness through posters or announcements.")

def suggest_redirection_options():
    print("\n=== Where Wasted Food Can Be Redirected ===")
    print("- Partner with local NGOs for daily food redistribution.")
    print("- Set up food donation counters for leftovers.")
    print("- Create composting programs for food scraps.")
    print("- Use excess edible food in next-day meals (if safe).")
