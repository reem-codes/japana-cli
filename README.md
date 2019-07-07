# About 

This is Japana. a Japanese analysis Command Line Interface using Jim Breen's JMdict & KanjiDic2 & mecab


You need to provide a text file: novel, short story, song lyrics, article, sentence ..etc. 
The program will return a word list ordered by frequency. 
each dictionary in the list has at least the word and the number of occurrence (frequency)
an depending on configurations: pronunciation and meaning
# Requirements

all requirements all stored in `requirements.txt`. In addition, you need to install my forked verion of neocl [Jamdict](https://github.com/reem-codes/jamdict)



# Installation:

1. run `pip install japana` in your venv/env/virtual_env
2. run `pip install git+https://github.com/reem-codes/jamdict` 
3. go to [Jamdict](https://github.com/neocl/jamdict)  official project and follow any instructions


# Other Projects

This project has been made into:
* python library: [Japana](https://github.com/reem-codes/japana)
* Web app: [Japana](http://japana.dev)
# Usage
`python3 japana-cli.py [-h] [-asc] [-dic] [-k] [-o OUTPUT] FILEPATH`

required arguments:

Option | Description
--- | --- 
FILEPATH | file path to text file

optional arguments:

Option | Description
--- | --- 
-h, --help | show this help message and exit 
-asc, --ascending | sort by frequency in ascending order (default descending)
-dic, --dictionary | add dictionary definitions
-k, --kana | count kana words
-o OUTPUT, --output OUTPUT | the full file path where the output will be saved, default is output/output.txt

# sample output
```
input file path:  file.txt
file will be written at:  output/output.txt
unique kanji count:  80
total word count:  261
unique word count:  62
 |██████████████████████████████████████████████████| 100.0% words has been done
writing to file ..
done
```
