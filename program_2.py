# Programmer: Mai Lillie
# Date: 9/17/24
# Age Categories

def categorize_age(age):
    age_category = "TBD"
    if age <= 1:
        age_category = "infant"
    elif age <13:
            age_category = "child"
    elif age <20:
        age_category = "teenager"
    elif age >= 20:
        age_category = "adult"
    return age_category

if __name__ == '__main__':
    # Local variables
    # Get age from the user.
    age = float(input("Enter the person's age: "))
    # Display the age
    ageBucket = categorize_age(age)
    print (ageBucket)
