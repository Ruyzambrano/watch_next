# Film Recommendation based on Text Similarity

This Python script uses the SpaCy library to recommend a film based on text similarity. It compares the provided model text with a list of films and their descriptions to find the film with the highest similarity rating.

## Requirements

To run this script, you need to have Python installed on your system. Additionally, you need to install the SpaCy library by running the following command:

```
pip install spacy
```

You also need to download the SpaCy English model by running the following command:

```
python -m spacy download en_core_web_md
```

## Usage

1. Make sure you have installed the required dependencies.
2. Place the text file containing film data (movies.txt) in the same directory as the script.
3. Open the script in a Python editor or IDE.
4. Run the script.
5. The script will read the film data from the movies.txt file.
6. It will compare the provided model text with each film's description.
7. The film with the highest similarity rating will be recommended.
8. The script will display the recommended film's title, description, and similarity rating.

## Example

```
Based on your recent films, you should watch The Avengers.

Description:
Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.

Similarity rating: 0.853
```

## Customization

To customize the script for your own film dataset, you can modify the following parts:

- Modify the movies.txt file to include your own films and descriptions. Each line should follow the format: `Film Title: Film Description`.
- Modify the model_text variable to contain your own text for comparison.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Please refer to the `LICENSE` file for more information.
