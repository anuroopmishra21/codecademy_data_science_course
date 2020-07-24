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
