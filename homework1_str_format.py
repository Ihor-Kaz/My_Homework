"""
Lesson01 Task01.

Descrition:
    we have norway text in old style formatting
    re-write the same text as:
    #1 string with format() call
    #2 f-string
    use linter(https://github.com/wemake-services/wemake-python-styleguide)
    to check your new created python module for possible linter errors
    try to run code from pycharm/command line

    norway_text = 'Automatisering akselererer %syeblikket da roboter
    vil erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
"""

norway_text = ('Automatisering akselererer %syeblikket da roboter vil'
               ' erobre planeten v%sr. (%s)' % ('ø', 'å', 'Æ')
               )
print(norway_text)

format_norway_text = ('Automatisering akselererer {0}yeblikket da roboter vil'
                      ' erobre planeten v{1}r. ({2})'.format('ø', 'å', 'Æ')
                      )
print(format_norway_text)

f_string_norway_text = (f'Automatisering akselererer {"ø"}yeblikket da roboter'
                        f' vil erobre planeten v{"å"}r. ({"Æ"})'
                        )
print(f_string_norway_text)
