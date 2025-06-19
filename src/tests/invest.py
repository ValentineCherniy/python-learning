def investment_plan(capital, monthly_contribution, annual_return_rate, months):
    monthly_return_rate = annual_return_rate / 12 / 100
    print(f"{'Месяц':>5} | {'Взнос (€)':>10} | {'Начисленная доходность (€)':>25} | {'Итоговый капитал (€)':>20}")
    print('-' * 70)
    for month in range(1, months + 1):
        capital = capital * (1 + monthly_return_rate) + monthly_contribution
        interest_earned = capital - monthly_contribution * month
        print(f"{month:5} | {monthly_contribution:10.2f} | {interest_earned:25.2f} | {capital:20.2f}")

if __name__ == "__main__":
    capital = float(input("First capital: "))
    monthly_contribution = float(input("Monthly contribution: " ))       # Евро в месяц
    annual_return_rate = float(input("Annual return rate: " )) # Годовая доходность в %
    investment_years = int(input("Years: " ))            # Срок инвестирования в годах
    total_months = investment_years * 12

    investment_plan(capital, monthly_contribution, annual_return_rate, total_months)
