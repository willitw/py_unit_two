#twig willaims
#currency.py
#9/28/23
#converts money to least amount of bills

amount = float(input("Enter an amount in dollars and cents:"))

print("TOO HEAVY" if input("Enter a phrase: ").lower() == "your mother" else "")


number_of_hundreds = amount // 100
change100 = amount % 100
print(round(number_of_hundreds), "hundred dollar bill(s)")


number_of_twentys = change100 // 20
change20 = change100 % 20
print(round(number_of_twentys), "twenty dollar bill(s)")


number_of_fives = change20 // 5
change5 = change20 % 5
print(round(number_of_fives), "five dollar bill(s)")


number_of_ones = change5 // 1
change1 = change5 % 1
print(round(number_of_ones), "one dollar bill(s)")


change_cents = round(change1 * 100)

quarters = change_cents // 25
change_cents %= 25
print(quarters, "quarter(s)")

dimes = change_cents // 10
change_cents %= 10
print(dimes, "dime(s)")

nickels = change_cents // 5
change_cents %= 5
print(nickels, "nickel(s)")

pennies = change_cents
print(pennies, "penny(s)")