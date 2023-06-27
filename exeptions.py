import string
from datetime import datetime


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
        return f"Email is too long"


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


class PassportLengthWrong(Exception):
    def __str__(self):
        return f"Passport should contain exactly 9 characters"


class PassportUpperCaseOrDigits(Exception):
    def __str__(self):
        return f"Passport should contain uppercase letters and digits only"


class DateNoDigits(Exception):
    def __str__(self):
        return f"Date must contain digits and '/' only "


class WrongDateFormat(Exception):
    def __str__(self):
        return f"Date format must be yyyy/mm/dd"


class DateMonthTooBig(Exception):
    def __str__(self):
        return f"Date month greater then 12"


class DateDayTooBig(Exception):
    def __str__(self):
        return f"Date day greater then 31"


class DateBeforeCurrnet(Exception):
    def __str__(self):
        return f"Date typed is before current day"


class DateAfterCurrnet(Exception):
    def __str__(self):
        return f"Date typed is after current day"


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
        elif len(email) > 30:
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


def validate_passport(passport):
    try:
        if len(passport) != 9:
            raise PassportLengthWrong
        # Check if the passport number contains only uppercase letters and digits
        if not passport.isalnum():
            raise PassportUpperCaseOrDigits

    except PassportLengthWrong as a:
        print(a)
    except PassportUpperCaseOrDigits as b:
        print(b)
    return True


def validate_date(date_str):
    # Check if all characters are numbers except for slashes
    try:
        if not date_str.replace('/', '').isdigit():
            raise DateNoDigits

        # Check if date is in the right format
        if datetime.strptime(date_str, "%Y/%m/%d"):
            raise WrongDateFormat

        # Convert the input date string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y/%m/%d").date()
        # Check if month is not greater than 12
        if date_obj.month > 12:
            raise DateMonthTooBig

        # Check if day is not greater than 31
        if date_obj.day > 31:
            return DateDayTooBig

    except DateNoDigits as a:
        print(a)
    except WrongDateFormat as b:
        print(b)
    except DateMonthTooBig as c:
        print(c)
    except DateDayTooBig as d:
        print(d)
    # All checks passed, date is valid
    return True


def validate_flight_date(date):
    if validate_date(date):
        # Get the current date
        current_date = datetime.now().date()
        date = datetime.strptime(date, "%Y/%m/%d").date()
        # Convert the input date string to a datetime object
        try:
            if date < current_date:
                raise DateBeforeCurrnet
        except DateBeforeCurrnet as a:
            print(a)
        return True


def validate_dob_date(date):
    if validate_date(date):
        # Get the current date
        current_date = datetime.now().date()
        date = datetime.strptime(date, "%Y/%m/%d").date()
        # Convert the input date string to a datetime object
        try:
            if date > current_date:
                raise DateAfterCurrnet
        except DateAfterCurrnet as a:
            print(a)
        return True
