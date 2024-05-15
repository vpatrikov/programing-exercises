cat_breeds = {
    "British Shorthair" : 13,
    "Siamese" : 15,
    "Persian" : 14,
    "Ragdoll" : 16,
    "American Shorthair" : 12,
    "Siberian" : 11
}

breedValid = False

while True:
    if not breedValid:
        breed = input()

        if breed in cat_breeds:
            breedValid = True
            continue
        else:
            print(f"{breed} is invalid cat!\n")
    else:
        gender = input()
        
        if gender == 'm' or gender == 'f':
            break
        else:
            print("Invalid gender (should be entered with 'm' or 'f')\n")
    

if gender == 'f':
    cat_breeds[breed] += 1

cat_years_to_months = int((cat_breeds[breed] * 12) / 6)

print(f"{cat_years_to_months} cat months")