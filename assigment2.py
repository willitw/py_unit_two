# twig williams
# assignment2.py
# 10/2/23
# calculate car interest and monthly payments using a chatbot to talk to user

# function to calc monthly payment and total cost
def calculate_loan_cost(P, numberYears, annualRate):
    # convert annual interest rate to monthly rate
    r = float(annualRate) / 100 / 12
    # calulate the number of monthly payments
    n = numberYears * 12
    # Calculate the monthly payment using the formula
    monthly_payment = (r * P) / (1 - (1 + r) ** -n)
    # calculate the total cost
    total_cost = monthly_payment * n
    return monthly_payment, total_cost

# main function for the chatbot
def main():
    # Greet the user and get their name
    user_name = input("Hello there! My name is CarBot. What is your name? ")

# definitely doesn't tell how to take over the world (i got these instrustions from my friend)
    if user_name.lower() == "how do i take over the world":
        print(
            "Ah, an interesting proposition! To take over the world, you'd need a comprehensive plan involving politics, economics, and technology. Here are some steps to get you started:")
        print("1. Gain political influence: Start by becoming a respected figure in your country's politics.")
        print("2. Build a powerful network: Forge alliances and connections with influential people.")
        print("3. Control the economy: Invest in industries that can yield power and wealth.")
        print("4. Develop advanced technology: Stay ahead in technology to control information and resources.")
        print("5. Establish global dominance: Expand your influence to other countries while maintaining stability at home.")

# if you don't want to know how to take over the world this will respond normally with the selected name
    else:
        print(f"Hello {user_name}, it is great to meet you!")

# ask the user where they are from
    user_location = input(f"{user_name}, where are you from? ")
    print(f"{user_location} sounds like a pleasant place to grow up.")

# ask the user for their favorite number
    favorite_number = int(input("Hmmmmmmmmmm, what else can I ask you... oh! What is your favorite number? "))
    my_favorite_number = 4
    print(f"Your favorite number ({favorite_number}) is {favorite_number / my_favorite_number:.1f} times as big as my favorite number ({my_favorite_number}).")

# ask the user about their dream car
    dream_car = input("What is your dream car? ")
    print(f"Wow, I've always wanted a {dream_car} as well.")

# ask the user for the cost of the dream car
    car_cost = float(input(f"How much does a {dream_car} cost? "))

# comment on the cost of the car
    print("Wow, that is expensive.")

# ask the user for the number of years for the car loan
    number_years = int(input("And if you had to take out a loan to buy the car, how many years would you take the loan out for? "))

# ask the user for the annual interest rate for the car loan
    annual_rate = float(input("What is the annual interest rate for a car loan? [0-20%] "))

# calculate monthly payment and total cost
    monthly_payment, total_cost = calculate_loan_cost(car_cost, number_years, annual_rate)

# format and display the results
    formatted_monthly_payment = "${:.2f}".format(monthly_payment)
    formatted_total_cost = "${:.2f}".format(total_cost)
    print(f"If you bought the {dream_car}, you would have a monthly payment of {formatted_monthly_payment}, hopefully that is reasonable for your budget. That's a total of {formatted_total_cost}! I hope you can make the purchase!")

# say goodbye to the user
    print(f"Anyways, I gotta go. It's been nice chatting with you {user_name} :]")

if __name__ == "__main__":
    main()
