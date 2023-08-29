import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


name_pattern = r'[\w]+'
domain_pattern = r'\.[a-z]+'

MAX_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]

email = input()

while email != 'End':

    domain_match = re.findall(domain_pattern, email)

    if len(email.split("@")[0]) < MAX_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if domain_match[0] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid!")

    email = input()
