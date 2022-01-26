from catalogue import *
import user
def greetings():
    welcome = " Hello!\n Welcome to our movie repository. Search through our 250 movies to find information about your favorite film!\n"
    print(welcome)
    imdb_catalogue, genres_list, genres_tries = load_catalogue("imdb(MOVIES).csv") # list of dictionaries
    film_titles = imdb_catalogue.create_tries()

    return imdb_catalogue, genres_list, genres_tries, film_titles
def restart(imdb_catalogue, genres_list, genres_tries, film_titles):
    again = input("\nDo you wish to search for another movie? (y/n)\n ")
    if again not in ["y", "n"]:
        print("Please enter y for yes, n for no")
        return restart(imdb_catalogue, genres_list, genres_tries, film_titles)
    if again == "y":
        select_mode(imdb_catalogue, genres_list, genres_tries, film_titles)
    if again == "n":
        print("Thank you for using our service!")

def select_mode(imdb_catalogue: catalogue_BST, genres_list: list, genres_tries: Trie, film_titles: list):
    choose = input("\n Do you want to choose from a specific genre or do you want to perform a general search?\n [1] - Genre filtered\n [2] - General search\n ")
    if int(choose) not in [1, 2]:
        print("Please enter a valid choice (1 or 2)")
        return select_mode(imdb_catalogue, genres_list, genres_tries, film_titles)

    elif int(choose) == 1:
        chosen_genre = genre_search(genres_list, genres_tries)
        matches = suggest(chosen_genre)
        movie = user.get_more_information(matches,imdb_catalogue)
        user.print_movie_card(movie)
        restart(imdb_catalogue, genres_list, genres_tries, film_titles)
    elif int(choose) == 2:
        matches = user.suggest(film_titles)
        movie = user.get_more_information(matches,imdb_catalogue)
        user.print_movie_card(movie)
        restart(imdb_catalogue, genres_list, genres_tries, film_titles)

def genre_search(genres_list:list, genres_tries:list[Trie]):
    print("These are our movie genres:")
    for idx, genre in enumerate(genres_list):
        print(f"{idx+1}. {genre.title()}")
    user_choice = input("\nWhat category would you want to search? Please enter the number associated to the genre.\n")
    if int(user_choice) not in list(range(1,len(genres_list)+1)):
        print("Please enter a valid number. Try again.")
        return genre_search(genres_list, genres_tries)
    chosen_genre = genres_tries[int(user_choice)-1] # Since genre_list and genre_trie have the same order, can choose trie directly
    print(f"\n These are the film we have under {genres_list[int(user_choice)-1]}")
    movies = chosen_genre.list_words()
    for movie in movies:
        print(f"- {movie.title()}")
    return chosen_genre


def suggest(title_trie: Trie ):
    print("\nType the beginning of the title from a movie you want information about:")
    user_input = input()
    matches = title_trie.autocomplete(user_input.lower())
    if not matches: # [] is False
        print(f"Could not find any films starting with {user_input}. Please try again.\n")
        return suggest(title_trie)
    print(f"Found {len(matches)} matches!")
    for idx, movie in enumerate(matches):
        print(f"{idx+1}. {movie.title()}") # this .title() is the string() method, not the catalogue_BST instance
    return matches

def get_more_information(matches_lst: list[str], catalogue: catalogue_BST) -> str:
    user_choice = input("\nWhich movie do you want to find more about?\n")
    if int(user_choice) not in list(range(1,len(matches_lst)+1)):
        print("Please enter a valid choice.")
        return get_more_information(matches_lst, catalogue)
    chosen_title = matches_lst[int(user_choice)-1]
    return catalogue.retrieve(chosen_title)

def print_movie_card(movie: catalogue_BST):
    movie_title = movie.title
    line_1 = f"Title: {movie_title.title()}"
    line_2 = f"Year: {movie.year[1:]}"
    line_3 = f"Run Time: {movie.time}"
    line_4 = f"Genre: {movie.time}"
    width = max(len(s) for s in [line_1, line_2, line_3, line_4])
    print("┌─" + '─'*width+ "─┐")
    print("│ " + line_1 + " "*(width-len(line_1)) + " │")
    print("│ " + line_2 + " "*(width-len(line_2)) + " │")
    print("│ " + line_3 + " "*(width-len(line_3)) + " │")
    print("│ " + line_4 + " "*(width-len(line_4)) + " │")
    print('└─' + '─' * width + '─┘')

    description = True
    while description:
        user_description = input("\nDo you wish to read a brief description about the movie? (y/n)\n")
        if user_description.lower() not in ["y", "n"]:
            continue
        else:
            description = False
    if user_description == "y":
        print(f"\nIMDb description of {movie_title.title()}: ")
        print(f"{movie.description}")
    else:
        return
    
    