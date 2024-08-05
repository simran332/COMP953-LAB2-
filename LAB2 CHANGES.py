def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        "full_name": "Simranjit Kaur",
        "student_id": 10315077,
        "pizza_toppings": ['Mushrooms','Olvies','3Cheese'],
        "movies": [
            {
                "title": "The Godfather",
                "genre": "Thriller"
            },
            {
                "title": "Unstoppable",
                "genre": "Crime"
            }
        ]
    }

    # TODO: Step 3 - Add another movie to the data structure
    about_me["movies"].append({"title": "The Bank Job","genre": "Thriller"})

    #name and id
    print_student_name_and_id(about_me)

    #list of toppings before adding more
    print_pizza_toppings(about_me)

    #add toppings
    toppings=("Peppers","Onions")
    add_pizza_toppings(about_me,toppings)

    #after adding toppings
    print_pizza_toppings(about_me)

    #printing the genres
    print_movie_genres(about_me)

    #printing the comma-separated movies titles 
    print_movie_titles(about_me["movies"])


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name= about_me["full_name"]
    first_name=full_name.split()[0]
    student_id= about_me["student_id"]
    print(f"My name is {full_name}, but you can call me Mrs. {first_name}.\nMy student ID is {student_id}.")
    return

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    for i in toppings:
        about_me['pizza_toppings'].append(i)
    about_me['pizza_toppings'].sort()
    for i in about_me["pizza_toppings"]:
        i.lower()
    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print()
    print("My prefered pizza toppings are:")
    for l in about_me["pizza_toppings"]:
        print(f'- {l}')
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    print()
    L = list()
    for movie in about_me["movies"]:
        L.append(movie ["genre"])
    s = ", ".join(L)
    print(f'I love to watch {s} movies.')
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    print()
    L = []
    for movie_info_dict in movie_list:
        L.append(movie_info_dict["title"])
    s = ", ".join(L)
    print(f"Some of my prefered movies are {s}!")
    return

if __name__== '__main__':
    main()