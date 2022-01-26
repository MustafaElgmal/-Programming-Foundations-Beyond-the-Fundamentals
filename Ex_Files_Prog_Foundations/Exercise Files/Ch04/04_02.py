# assign strings to varibles 
first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'
# to convert the first char in first_name to capitalization
first_name_cap = first_name.capitalize()
# to convert the first char in last_name to capitalization
last_name_cap = last_name.capitalize()
# to cheack if a word "award:" in string or not if exit return indx of first char in a word or if not return -1
award_location = note.find('award: ')
# cut string from indx 7 to size of varible note to varible award_text
award_text = note[7:]
# display on screen 
print(first_name_cap)
print(last_name_cap)
print(award_location)
print(award_text)