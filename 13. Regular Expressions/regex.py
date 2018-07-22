# import re
#
# p=re.compile('ab*',re.IGNORECASE)
# print(p.match('ABcdab'))

# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
# print(matchObj.groups())
# if matchObj:
#    print("matchObj.group() : ", matchObj.group())
#    print("matchObj.group(1) : ", matchObj.group(1))
#    print("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print("No match!!")

#Matching vs searching

# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'Cats', line, re.M|re.I)
# if matchObj:
#    print("match --> matchObj.group() : ", matchObj.group())
# else:
#    print("No match!!")
#
# searchObj = re.search( r'smarter', line, re.M|re.I)
# if searchObj:
#    print("search --> searchObj.group() : ", searchObj.group())
# else:
#    print("Nothing found!!")

# A Python program to demonstrate working of re.match().
# import re
#
# # Lets use a regular expression to match a date string
# # in the form of Month name followed by day number
# regex = r"([a-zA-Z]+) (\d+)"
#
# match = re.search(regex, "I was born on June 24")
#
# if match != None:
#
#     # We reach here when the expression "([a-zA-Z]+) (\d+)"
#     # matches the date string.
#
#     # This will print [14, 21), since it matches at index 14
#     # and ends at 21.
#     print("Match at index %s, %s" % (match.start(), match.end()))
#
#     # We us group() method to get all the matches and
#     # captured groups. The groups contain the matched values.
#     # In particular:
#     #    match.group(0) always returns the fully matched string
#     #    match.group(1) match.group(2), ... return the capture
#     #    groups in order from left to right in the input string
#     #    match.group() is equivalent to match.group(0)
#
#
#     print("Full match: %s" % (match.group(0)))
#
#
#     print("Month: %s" % (match.group(1)))
#
#
#     print("Day: %s" % (match.group(2)))
#
# else:
#     print("The regex pattern does not match.")

#Search and replace
# import re
#
# phone = "2004-959-559 # This is Phone Number"
#
# # Delete Python-style comments
# num = re.sub(r'#.*', "", phone)
# print("Phone Num : ", num)
#
# # Remove anything other than digits
# num = re.sub(r'\D', "", phone)
# print("Phone Num : ", num)

#Let's try to reverse the order of day and month in a date string.
#Notice how the replacement string also contains metacharacters(Back references to the captured group)
# import re
# regex = r"([a-zA-Z]+) (\d+)"
#
# print(re.sub(regex,r"\2 of \1","June 24,August 9,Dec 12"))

# import re
# # Lets use a regular expression to match a few date strings.
# regex = r"[a-zA-Z]+ \d+"
# matches = re.findall(regex, "June 24, August 9, Dec 12")
# print(matches)
# for match in matches:
#     # This will print:
#     #   June 24
#     #   August 9
#     #   Dec 12
#     print("Full match: %s" % (match))
#
# # To capture the specific months of each date we can use the following pattern
# regex = r"([a-zA-Z]+) \d+"
# matches = re.findall(regex, "June 24, August 9, Dec 12")
# print(matches)
# for match in matches:
#
#     print("Match month: %s" % (match))
#
# # If we need the exact positions of each match
# regex = r"([a-zA-Z]+) \d+"
# matches = re.finditer(regex, "June 24, August 9, Dec 12")
# print(matches)
# for match in matches:
#     # which corresponds with the start and end of each match in the input string
#     print("Match at index: %s, %s" % (match.start(), match.end()))

