"""
Reference types given by ohtu:

@inproceedings{VPL11,
    author = {Vihavainen, Arto and Paksula, Matti and Luukkainen, Matti},
    title = {Extreme Apprenticeship Method in Teaching Programming for Beginners.},
    year = {2011},
    booktitle = {SIGCSE '11: Proceedings of the 42nd SIGCSE technical symposium on Computer science education},
}

@article{CBH91,
    author = {Allan Collins and John Seely Brown and Ann Holum},
    title = {Cognitive apprenticeship: making thinking visible},
    journal = {American Educator},
    year = {1991},
    volume = {6},
    pages = {38--46}
}

@book{Martin09,
    author = {Martin, Robert},
    title = {Clean Code: A Handbook of Agile Software Craftsmanship},
    year = {2008},
    publisher = {Prentice Hall},
}



More types: wikipedia https://en.wikibooks.org/wiki/LaTeX/Bibliography_Management
e.g. booklet, inbook, incollection, manual, mastersthesis/phdhesis, misc, proceedings, tech report, unpublished

"""
from abc import ABC, abstractmethod


def spellingChecker():
    # TODO
    ...


class Reference(ABC):
    """Default class for all reference objects"""

    def __init__(
        self,
        # cite: str # e.g. Martin09 for {Martin, Robert} ? init now or later
        author: str,
        title: str,
        year: str,  # or int?
    ):

        self.cite = cite  # ?
        self.author = author
        self.title = title
        self.year = year

    """
    @property
    def cite(self):
        return self._cite

    @cite.setter
    def cite(self, new_cite):
        # citation format e.g. Martin09 given by user
        #TODO
        self._cite = new_cite
    """

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_name):
        """Check author str format before adding"""
        # TODO
        self._author = new_name

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        """Check title str format before adding"""
        # TODO
        self._title = new_title

    @property
    def year(self):
        # TODO
        ...

    @year.setter
    def year(self, new_year):
        # TODO
        ...

    @abstractmethod
    def __str__(self):
        """return ref in latex format? or separate method"""


# new file for this?
class Book(Reference):
    """Reference object for books"""

    def __init__(self, author: str, title: str, year: str, publisher: str):

        super().__init__(author=author, title=title, year=year)

        self.publisher = publisher

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, new_publisher):
        """Check publisher format"""
        # TODO
        self._publisher = new_publisher

    def __str__(self):
        """return ref in latex format? or separate method"""
        # TODO
        return f"@book\{{MY_CITE\n  author = {self.author}..."
