import re
# characters are defined
character_1 = "Dorothy"
character_2 = "Henry"
# compile your regular expression here
regular_expression = re.compile("[A-Za-z]{7}")
# check for a match to character_1 here
result_1 = regular_expression.match(character_1)
# store and print the matched text here
match_1 = result_1.group(0)
print(match_1)
# compile a regular expression to match a 7 character string of word characters and check for a match to character_2 here
result_2 = re.match("[A-Za-z]{7}", character_2)
print(result_2)

import re
# import L. Frank Baum's The Wonderful Wizard of Oz
oz_text = open("the_wizard_of_oz_text.txt",encoding='utf-8').read().lower()
# search oz_text for an occurrence of 'wizard' here
found_wizard = re.search('wizard', oz_text)
print(found_wizard)
# find all the occurrences of 'lion' in oz_text here
all_lions = re.findall('lion', oz_text)
print(all_lions)
# store and print the length of all_lions here
number_lions = len(all_lions)
print(number_lions)

import nltk
from nltk import pos_tag
from word_tokenized_oz import word_tokenized_oz
# save and print the sentence stored at index 100 in word_tokenized_oz here
witches_fate = word_tokenized_oz[100]
print(witches_fate)
# create a list to hold part-of-speech tagged sentences here
pos_tagged_oz = []
# create a for loop through each word tokenized sentence in word_tokenized_oz here
for sentence in word_tokenized_oz:
  pos_tagged_oz.append(pos_tag(sentence))
# store and print the 101st part-of-speech tagged sentence here
witches_fate_pos = pos_tagged_oz[100]
print(witches_fate_pos)

from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz
# define adjective-noun chunk grammar here
chunk_grammar = "AN: {<JJ><NN>}"
# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)
# chunk the pos-tagged sentence at index 282 in pos_tagged_oz here
scaredy_cat = chunk_parser.parse(pos_tagged_oz[282])
print(scaredy_cat)
# pretty_print the chunked sentence here
Tree.fromstring(str(scaredy_cat)).pretty_print()

from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from np_chunk_counter import np_chunk_counter
# define noun-phrase chunk grammar here
chunk_grammar = 'NP: {<DT>?<JJ>*<NN>}'
# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)
# create a list to hold noun-phrase chunked sentences
np_chunked_oz = list()
# create a for loop through each pos-tagged sentence in pos_tagged_oz here
for sentence in pos_tagged_oz:
  np_chunked_oz.append(chunk_parser.parse(sentence))
# store and print the most common np-chunks here
most_common_np_chunks = np_chunk_counter(np_chunked_oz)
print(most_common_np_chunks)

from nltk import RegexpParser
from pos_tagged_oz import pos_tagged_oz
from vp_chunk_counter import vp_chunk_counter
# define verb phrase chunk grammar here
chunk_grammar = 'VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}'
# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)
# create a list to hold verb-phrase chunked sentences
vp_chunked_oz = list()
# create for loop through each pos-tagged sentence in pos_tagged_oz here
for sentence in pos_tagged_oz:
  # chunk each sentence and append to vp_chunked_oz here
  vp_chunked_oz.append(chunk_parser.parse(sentence))
# store and print the most common vp-chunks here
most_common_vp_chunks = vp_chunk_counter(vp_chunked_oz)
print(most_common_vp_chunks)

from nltk import RegexpParser, Tree
from pos_tagged_oz import pos_tagged_oz
# define chunk grammar to chunk an entire sentence together
grammar = "Chunk: {<.*>+}"
# create RegexpParser object
parser = RegexpParser(grammar)
# chunk the pos-tagged sentence at index 230 in pos_tagged_oz
chunked_dancers = parser.parse(pos_tagged_oz[230])
print(chunked_dancers)
# define noun phrase chunk grammar using chunk filtering here
chunk_grammar = """NP: {<.*>+}
                       }<VB.?|IN>+{"""
# create RegexpParser object here
chunk_parser = RegexpParser(chunk_grammar)
# chunk and filter the pos-tagged sentence at index 230 in pos_tagged_oz here
filtered_dancers = chunk_parser.parse(pos_tagged_oz[230])
print(filtered_dancers)
# pretty_print the chunked and filtered sentence here
Tree.fromstring(str(filtered_dancers)).pretty_print()
