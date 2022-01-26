import csv

def load_catalogue(filename):
    # Returns catalogue BST and titles Tries() used for autocomplete.
    with open(filename,encoding="utf8") as csvfile:
        movies = [{key: value for key, value in row.items()}
            for row in csv.DictReader(csvfile, skipinitialspace=True)]
    catalogue = catalogue_BST(movies[0])
    genres_unique = movies[0]["genre"].split(", ")
    genres_tries = [Trie() for genre in genres_unique]
    for i in range(1,len(movies)):
        catalogue.insert(movies[i]) # Inserts each movie into BST
        
        for genre in movies[i]["genre"].split(", "):
            if genre not in genres_unique:
                genres_unique.append(genre) # Keeps track of unique genres 
                genres_tries.append(Trie()) # Creates a Trie for every unique genre
                genres_tries[genres_unique.index(genre)].insert(movies[i]["movie name "].lower()) # Inserts movie title inside trie corresponding to genre
            else:
                genres_tries[genres_unique.index(genre)].insert(movies[i]["movie name "].lower())
    return catalogue,  genres_unique, genres_tries
class Trie():
    def __init__(self) -> None:
        self.children = {}
        self.word_end = False
    
    def insert(self, word):
        for char in word:
            if char not in self.children:
                self.children[char] = Trie()
            self = self.children[char]
        self.word_end = True

    def words_with_prefix(self, prefix):
        results = []
        if self.word_end:
            # Base case is that the prefix is a word
            results.append(prefix)
        for char, node in self.children.items():
            results.extend(node.words_with_prefix(prefix+char))
        return results

    def autocomplete(self, prefix):
        node = self
        for char in prefix:
            # checks that there is a path containing that prefix
            if char not in node.children:
                return None
            node = node.children[char]
        return node.words_with_prefix(prefix)

    def list_words(self):
        all_words = []
        for start in self.children.keys():
            all_words.extend(self.autocomplete(start))
        return all_words

class catalogue_BST:
    def __init__(self, movie, depth=1):
        self.movie = movie
        self.title = movie["movie name "].lower()
        self.year = movie["Year"]
        self.time = movie["runtime"]
        self.genre = movie["genre"]
        self.description = movie["DETAIL ABOUT MOVIE"]
        self.depth = depth

        self.parent = None
        self.left = None
        self.right = None
    
    def insert(self, movie):
        """ Store method: Inserts value into tree"""
        if (movie["movie name "].lower() < self.title):
            if self.left is None:
                self.left = catalogue_BST(movie, self.depth+1)
            else:
                self.left.insert(movie) # If left child exists, then inserts value to tree with value left (re runs insert on it)
        else:
            if self.right is None:
                self.right = catalogue_BST(movie, self.depth+1)
            else:
                self.right.insert(movie)
    
    def retrieve(self, movie_name: str):
        "Retrieval method: returns tree with target value"
        if self.title == movie_name:
            return self
        elif movie_name > self.title and self.right is not None:
            return self.right.retrieve(movie_name)
        elif movie_name < self.title and self.left is not None:
            return self.left.retrieve(movie_name)
        else:
            return None

    def depth_traversal(self, movie_titles=[]):
        # first traverses all left nodes
        if self.left is not None:
            self.left.depth_traversal(movie_titles)
        #print(f"Depth = {self.depth}, Title = {self.title}")
        movie_titles.append(self.title)
        if self.right is not None:
            self.right.depth_traversal(movie_titles)
        return movie_titles
    
    def create_tries(self):
        all_titles = self.depth_traversal()
        title_tries = Trie()
        for title in all_titles:
            title_tries.insert(title)
        return title_tries


    def breadth_search(self):
        if self.left is not None:
            print(f"Depth = {self.depth}, Title = {self.left.title}")
 
    



        
            

