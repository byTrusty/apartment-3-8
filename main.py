def apt_search1(city, max_rent, min_beds, pets_allowed):
    pets_text = "Pets allowed" if pets_allowed else "No pets allowed"
    return f"Searching for an apartment in {city} with a maximum rent of {max_rent} dollars per month, at least {min_beds} bedrooms, and {pets_text}."

# Example usage:
print(apt_search1("San Francisco", 3000, 2, True)) # Output: Searching for an apartment in San Francisco with a maximum rent of 3000 dollars per month, at least 2 bedrooms, and Pets allowed.
print(apt_search1("New York", 2500, 1, False)) # Output: Searching for an apartment in New York with a maximum rent of 2500 dollars per month, at least 1 bedroom, and No pets allowed.


def apt_search2(city, max_rent, min_beds=1, pets_allowed=False):
    pets_text = "Pets allowed" if pets_allowed else "No pets allowed"
    return f"Searching for an apartment in {city} with a maximum rent of {max_rent} dollars per month, at least {min_beds} bedrooms, and {pets_text}."

# Example usage:
print(apt_search2("San Francisco", 3000)) # Output: Searching for an apartment in San Francisco with a maximum rent of 3000 dollars per month, at least 1 bedrooms, and No pets allowed.
print(apt_search2("New York", 2500, 2)) # Output: Searching for an apartment in New York with a maximum rent of 2500 dollars per month, at least 2 bedrooms, and No pets allowed.
print(apt_search2("Los Angeles", 2000, pets_allowed=True)) # Output: Searching for an apartment in Los Angeles with a maximum rent of 2000 dollars per month, at least 1 bedrooms, and Pets allowed.



plus_one_hundred = lambda x: x + 100
square_num = lambda x: x**2
concatenate = lambda s: "- " + s
divide_by_three = lambda x: x / 3

# Example usage:
print(plus_one_hundred(50)) # Output: 150
print(square_num(7)) # Output: 49
print(concatenate("hello")) # Output: "- hello"
print(divide_by_three(12)) # Output: 4.0

# tests should look like this:
print(plus_one_hundred(30))  # 130
print(square_num(4))  # 16
print(concatenate('hello'))  # - hello
print(divide_by_three(9))  # 3.0