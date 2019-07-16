import argparse
import os
from japana.word_count import word_count
from japana.kanji_count import list_kanji


description = 'CLI to perform various NLP on japanese text stored files'
parser = argparse.ArgumentParser(description= description)
parser.add_argument('-asc', '--ascending', action='store_true',
                    help='sort by frequency in ascending order (default descending)')
parser.add_argument('-dic', '--dictionary', action='store_true',
                    help='add dictionary definitions')
parser.add_argument('-k', '--kana', action='store_true',
                    help='count kana words')

parser.add_argument('-i', '--include', action='store_true',
                    help='include words with no definitions')


parser.add_argument('-o', '--output', default="output/output.txt",
                    help='the full file path where the output will be saved, default is output/output.txt')
parser.add_argument('FILEPATH', type=str, help='file path to text file')


args = parser.parse_args()

output = args.output
if output is "output/output.txt":
    output = os.path.dirname(args.FILEPATH) + output

directory = os.path.dirname(output)

original_umask = os.umask(0)
try:
    if not os.path.exists(directory):
        os.makedirs(directory, 0o777)
finally:
    os.umask(original_umask)

print("input file path: ", args.FILEPATH)
print("file will be written at: ", output)
list_kanji(args.FILEPATH)

with open(args.FILEPATH, 'r') as f:
    text = f.read()

words = word_count(text, args.kana, args.ascending, args.dictionary, args.include)
print("writing to file ..")
with open(output, "a") as o:
    o.truncate(0)
    for word in words:
        line = word['word'] + "\t"
        line += (word['meaning'] if word.get("meaning") else "-") + "\t"
        line += (word['pronunciation'] if word.get("pronunciation") else "-") + "\t"
        line += (word['jlpt'] if word.get("jlpt") else "-") + "\t"
        line += str(word['frequency']) + "\n"

        o.write(line)
print("done")