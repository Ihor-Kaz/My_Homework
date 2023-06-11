# we have norway text in old style formatting
# re-write the same text as:
# #1 string with format() call
# #2 f-string
# use linter(https://github.com/wemake-services/wemake-python-styleguide)
# to check your new created python module for possible linter errors
# try to run code from pycharm/command line

name1, name2, name3 = 'ø', 'å', 'Æ'
print(('Automatisering akselererer %syeblikket ' +
       'da roboter vil erobre planeten v%sr. (%s)'
       ) % (name1, name2, name3),
      )
print(('Automatisering akselererer {0}yeblikket ' +
       'da roboter vil erobre ' +
       'planeten v{1}r. ({2})'
       ).format(name1, name2, name3),
      )
print((f'Automatisering akselererer {name1}yeblikket ' +
       f'da roboter vil erobre planeten v{name2}r. ({name3})'
       ),
      )
