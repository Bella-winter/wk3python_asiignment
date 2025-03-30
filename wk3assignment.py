def calculate_discount(price, discount_percent):
   # Calculate the final price after applying the discount
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Use 'price' instead of 'original_price'
  
# Prompt the user to enter the price and discount percentage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"The final price after applying a {discount_percentage}% discount is: {final_price}")
else:
    print(f"The final price is: {final_price}")


    # The code calculates the final price after applying a discount if the discount percentage is 20% or more.

# 1. sample output:
# Enter the original price: 900
# Enter the discount percentage: 16
# The final price is: 900.0
     # If the discount percentage is less than 20%, it returns the original price.
# 2. sample output:
# Enter the original price: 900
# Enter the discount percentage: 20
# The final price after applying a 20.0% discount is: 720.0