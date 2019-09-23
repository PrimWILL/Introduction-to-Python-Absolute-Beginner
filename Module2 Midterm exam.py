fish_entry = input("enter fish name: ")
price_entry = input("enter the fish price (no symbols): ")
def fishstore(fish, price):
    ans = "fish type: "+ fish + " costs $" + price
    return ans
print(fishstore(fish_entry, price_entry))