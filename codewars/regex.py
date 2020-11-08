# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number

regex = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$"

# broken down, slightly different but more readable
regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)
