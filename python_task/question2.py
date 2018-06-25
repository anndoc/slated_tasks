import re
import sys


def validate_password(value):
    """
    Validate password according to criteria:

    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    3. At least 1 letter between [A-Z]
    4. At least 1 character from [*#+@]
    5. Minimum length of transaction password: 4
    6. Maximum length of transaction password: 6
    7. No space is allowed
    """
    regex = re.compile(
        r'^'
        r'(?!.*?[ ])'  # no space is allowed
        r'(?=.*?[A-Z])'  # at least 1 letter between [A-Z]  
        r'(?=.*?[a-z])'  # at least 1 letter between [a-z]
        r'(?=.*?[0-9])'  # at least 1 number between [0-9]
        r'(?=.*?[*#+@])'  # at least 1 character from [*#+@]
        r'.{4,6}'  # minimum length of transaction password: 4, maximum length of transaction password: 6
        r'$'
    )
    return re.match(regex, value)


def main(passwords):
    return ','.join([password for password in passwords.split(',') if validate_password(password)])


if __name__ == "__main__":
    """
    Write a program which will accept a sequence of comma separated transaction passwords 
    and will check them according to the bank's criteria. Passwords that match the criteria 
    are to be printed, each separated by a comma.
    """
    value = input('Enter sequence of comma separated transaction passwords: \n')
    sys.stdout.write('{}\n'.format(main(value)))
