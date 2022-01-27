# movie_recommendation
movie_recommendation is my project created as part of the data struture and algorithm module within the Computer Science path in codecademy. 

## Files
`imdb(MOVIES).csv` - Top 250 IMDb movies as of January 2022, downloaded from Kaggle. (https://www.kaggle.com/ramjasmaurya/top-250s-in-imdb)

`main.py` - File that runs the program. 

`user.py` - Contains the functions used to interact with the user via command line.

`catalogue.py` - Contains `load_catalogue()` function which reads the database and creates a Binary Search Tree class `catalogue_BST()` and a Trie class `Trie()`, both defined in this same file. 

## Running the code
1. Download folder and run `python main.py` on the command line. 
2. The program will ask for choice between two running modes:

    a) **Genre search**: The program will display the genres found in the data base. The user will then choose one of the genres. The films that belong to this category will be displayed. The user will then be asked to enter part of the title of one of those films and a autocomplete method will be invoked on that string.  

    b)  **General search**: The user will be asked to input the beginning of a movie title and the autocomplete method will be called on that string. 
3. If a match is found, the movie's Title, Year, Genre and Duration will be displayed alongside the option to display a description of the movie. 
4. Perform another search or exit the program. 

