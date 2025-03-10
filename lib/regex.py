import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z]\w*[\s|'][a-zA-Z-]*"
name_regex = re.compile(name)

phone_number = r"\(?\d{3}\)?\s?\-?\d{3}\-?\d{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-Za-z][a-zA-Z0-9_\.]+\@\w+\.\w+"
email_regex = re.compile(email_address)
