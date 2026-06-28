print("Recommendation System")
print("---------------------")

print("Select a category")
print("1. Movies")
print("2. Books")
print("3. Mobile Phones")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    movies = ["3 Idiots", "Dangal", "Chhichhore"]
    print("\nRecommended Movies:")
    for movie in movies:
        print(movie)

elif choice == "2":
    books = ["Atomic Habits", "Rich Dad Poor Dad", "The Alchemist"]
    print("\nRecommended Books:")
    for book in books:
        print(book)

elif choice == "3":
    phones = ["Samsung Galaxy S24", "Nothing Phone 3", "OnePlus 13R"]
    print("\nRecommended Mobile Phones:")
    for phone in phones:
        print(phone)

else:
    print("Invalid Choice")