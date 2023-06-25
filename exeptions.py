import string


class NameContainsIllegalCharacter(Exception):
    def __init__(self, letter, index):
        self._letter = letter
        self._index = index

    def __str__(self):
        return f"The name contains an illegal character {self._letter} at index {self._index}"


class NameTooShort(Exception):
    def __str__(self):
        return f"Name is too short"


class NameTooLong(Exception):
    def __str__(self):
        return f"Name is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return f"Password is missing a Character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    def __str__(self):
        return f"password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return f"password is too long"


class EmailTooShort(Exception):
    def __str__(self):
        return f"email is too short"


class EmailTooLong(Exception):
    def __str__(self):
        return f"Email is too short"


class EmailMissingCharacter(Exception):
    def __str__(self):
        return f"Email is missing a vital char"


class EmailIsNotValid(Exception):
    def __str__(self):
        return f"This Email address is not valid"


class PhoneNumTooShort(Exception):
    def __str__(self):
        return f"Phone number is too short"


class PhoneNumTooLong(Exception):
    def __str__(self):
        return f"Phone number is too long"


class PhoneNumNotDigits(Exception):
    def __str__(self):
        return f"Phone number must contain digits only"


def validate_name(name):
    try:
        for i in range(len(name)):
            if not name[i].isalpha() and not name[i].isdigit() and name[i] != '_':
                raise NameContainsIllegalCharacter(name[i], i)
        if len(name) < 2:
            raise NameTooShort
        elif len(name) > 16:
            raise NameTooLong
        return True

    except NameContainsIllegalCharacter as a:
        print(a)

    except NameTooShort as b:
        print(b)

    except NameTooLong as c:
        print(c)


def validate_phone_num(phone_num):
    try:
        if not all(char.isdigit() for char in phone_num):
            raise PhoneNumNotDigits
        elif len(phone_num) < 8:
            raise PhoneNumTooShort
        elif len(phone_num) > 14:
            raise PhoneNumTooLong

        return True
    except PhoneNumTooShort as a:
        print(a)
    except PhoneNumTooLong as b:
        print(b)
    except PhoneNumNotDigits as c:
        print(c)


def validate_password(password):
    try:
        if len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 20:
            raise PasswordTooLong
        elif not any(char.isupper() for char in password):
            raise PasswordMissingUppercase
        elif not any(char.islower() for char in password):
            raise PasswordMissingLowercase
        elif not any(char.isdigit() for char in password):
            raise PasswordMissingDigit
        elif not any(char in string.punctuation for char in password):
            raise PasswordMissingSpecial
        return True

    except PasswordMissingUppercase as d:
        print(d)

    except PasswordMissingLowercase as e:
        print(e)

    except PasswordMissingDigit as f:
        print(f)

    except PasswordMissingSpecial as g:
        print(g)

    except PasswordTooLong as h:
        print(h)

    except PasswordTooShort as i:
        print(i)


def validate_email(email):
    try:
        if len(email) < 4:
            raise EmailTooShort
        elif len(email) > 20:
            raise EmailTooLong
        elif '@' not in email or '.' not in email:
            raise EmailMissingCharacter
        elif email.startswith('@') or email.endswith('@') or ' ' in email:
            raise EmailIsNotValid
        return True

    except EmailTooShort as a:
        print(a)
    except EmailTooLong as b:
        print(b)
    except EmailMissingCharacter as c:
        print(c)
    except EmailIsNotValid as d:
        print(d)
