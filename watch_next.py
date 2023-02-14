#import the spacey module
import spacy

def similarity_film(model_text):
    pass

    #read the text file and save the data
    with open("movies.txt") as file:
        movies = file.readlines()

    #define similarity as 0
    similarity_max = 0

    #for each film, seperate the title from the description
    for line in movies:
        film_description = line.split(" :")

        #make the description a token
        compare_film = nlp(film_description[1])

        #store the similarity between planet Hulk and the film
        similarity = compare_film.similarity(model_text)

        #if the similarity is higher than the previous, store its data
        if similarity > similarity_max:
            similarity_max = similarity
            highest_film = film_description
    
    #print the film with the highest similarity along with its description and similarity rating
    print(f"Based on your recent films, you should watch {highest_film[0]}.")
    print(f"\nDescription:\n{highest_film[1]}")
    print(f"Similarity rating: {similarity_max}")

#create an nlp
nlp = spacy.load("en_core_web_md")

#create a variable with the model text
planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

#create a token
model_text = nlp(planet_hulk)

similarity_film(model_text)