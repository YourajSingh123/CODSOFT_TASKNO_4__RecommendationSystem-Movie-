from recommender import recommend

print("=" * 50)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

while True:

    movie = input("\nEnter Movie Name (or exit): ")

    if movie.lower() == "exit":
        break

    result = recommend(movie)

    if result is None:
        print("\nMovie not found.")
    else:
        print("\nRecommended Movies:\n")

        for i, movie in enumerate(result, 1):
            print(f"{i}. {movie}")