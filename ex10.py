# use the tab escape character
tabby_cat = "\tI'm tabbed in."
# use the new line escape character
persian_cat = "I'm split\non a line"
# use the backslash escape character
backslash_cat = "I'm \\ a \\ cat."
# use the triple quote with tabs to create a long list of items
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
# print out each string

combination_test = '''
This is a combination_test list:
\nTeams I like:
\t+ Man Utd
\t+ Stevenage
\t+ Hull FC

Teams I don't like:
\t- Arsenal
\t- Liverpool
\t- Leeds
'''

formatter = "{}{}{}{}"


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(combination_test)
print(formatter.format("\t\n#1", "\t\n#2","\t\n#3","\t\n#4"))
