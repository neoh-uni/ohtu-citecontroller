"""
Author: Niklas
See more types from: wikipedia https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management
e.g. booklet, inbook, incollection, manual, mastersthesis/phdhesis,...
"""
from typing import Optional
from datetime import datetime
from attrs import define, field


def check_year(instance_unused, attribute_unused, given_year):
    """
    Checks that publishment year is in a reasonable range;
    e.g [500, current year + 5]
    """
    year_now = datetime.now().year
    if given_year is None:
        raise ValueError("All fields must have a value")
    if (given_year > year_now + 5) or (given_year < 500):
        raise ValueError(f"Given year is not in range [500, {year_now+5}]")


def check_name(instance_unused, attribute_unused, given_name):
    """
    Check that name is in proper format:
    - Firstname + ... + Surname
    - str made of [Aa-Zz]
    """
    given_name = given_name.replace(".", "").replace(",", "")
    split_name = given_name.split()
    len_n = len(split_name)
    if len_n < 2:
        raise ValueError("First name and surname is required")
    for name in split_name:
        if not name.isalpha():
            raise ValueError("Name has to consists only of alphabet letters")


def check_len(instance_unused, attribute_unused, given_str):
    """
    BibTeX has a 5000 character limit for each field?
    e.g. https://clemson.libguides.com/LaTeX
    """
    if given_str is not None and len(given_str) > 5000:
        raise ValueError("Str length exceeds BibTeX field character limit of 5000")


def check_str(instance_unused, attribute_unused, given_str):
    if len(given_str) is None:
        raise ValueError("All fields must have a value")
    if given_str is not None and not isinstance(given_str, str):
        raise ValueError("Given value is not a string")


def convert_year(given_str):
    try:
        return int(given_str)
    except ValueError as exc:
        raise ValueError("Year was not given as an integer") from exc


def convert_volume(given_str):
    if given_str is None:
        return None
    try:
        return int(given_str)
    except ValueError as exc:
        raise ValueError("Volume was not given as an integer") from exc


@define
class Book:
    """
    @book{Martin09,
        author = {Martin, Robert},
        title = {Clean Code: A Handbook of Agile Software Craftsmanship},
        year = {2008},
        publisher = {Prentice Hall},
    }
    """

    author: str = field(validator=[check_str, check_name, check_len])
    title: str = field(validator=[check_str, check_len])
    year: int = field(converter=convert_year, validator=[check_year])
    publisher: str = field(validator=[check_str, check_len])

    address: Optional[str] = field(default=None, validator=[check_str, check_len])
    edition: Optional[str] = field(default=None, validator=[check_str, check_len])
    editor: Optional[str] = field(default=None, validator=[check_str, check_len])
    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])
    series: Optional[str] = field(default=None, validator=[check_str, check_len])
    volume: Optional[str] = field(default=None, converter=convert_volume)


@define
class Article:
    """
    @article{CBH91,
        author = {Allan Collins and John Seely Brown and Ann Holum},
        title = {Cognitive apprenticeship: making thinking visible},
        journal = {American Educator},
        year = {1991},
        volume = {6},
        pages = {38--46}
    }
    """

    author: str = field(validator=[check_str, check_name, check_len])
    journal: str = field(validator=[check_str, check_len])
    title: str = field(validator=[check_str, check_len])
    year: int = field(converter=convert_year, validator=[check_year])
    volume: int = field(converter=convert_volume)
    pages: str = field(default=None, validator=[check_str, check_len])

    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])


@define
class Inproceedings:
    """
    @inproceedings{VPL11,
        author = {Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti},
        title = {Extreme Apprenticeship Method in Teaching Programming for Beginners.},
        year = {2011},
        booktitle = {SIGCSE '11: Proceedings of the 42nd SIGCSE technical symposium
        on Computer science education},
    }
    """

    author: str = field(validator=[check_str, check_name, check_len])
    title: str = field(validator=[check_str, check_len])
    year: int = field(converter=convert_year, validator=[check_year])
    booktitle: str = field(validator=[check_str, check_len])

    address: Optional[str] = field(default=None, validator=[check_str, check_len])
    editor: Optional[str] = field(default=None, validator=[check_str, check_len])
    month: Optional[str] = field(default=None, validator=[check_str, check_len])
    note: Optional[str] = field(default=None, validator=[check_str, check_len])
    number: Optional[str] = field(default=None, validator=[check_str, check_len])
    organization: Optional[str] = field(default=None, validator=[check_str, check_len])
    pages: Optional[str] = field(default=None, validator=[check_str, check_len])
    publisher: Optional[str] = field(default=None, validator=[check_str, check_len])
    series: Optional[str] = field(default=None, validator=[check_str, check_len])
    volume: Optional[str] = field(default=None, converter=convert_volume)
