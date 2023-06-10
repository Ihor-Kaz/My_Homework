# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string
# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# try to run code from pycharm/command line

name1 = 'ø'
name2 = 'å'
name3 = 'Æ'
norway_text = 'Automatisering akselererer %syeblikket da roboter vil erobre planeten v%sr. (%s)'% ('ø', 'å', 'Æ')
norway_text1 = 'Automatisering akselererer {0}yeblikket da roboter vil erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ')
norway_text2 = f'Automatisering akselererer {name1}yeblikket da roboter vil erobre planeten v{name2}r. ({name3})'
print(norway_text)
print(norway_text1)
print(norway_text2)
