# classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string")
        self._name = name  # immutable

    @property
    def name(self):
        return self._name

    def articles(self):
        """Return list of Article instances written by this author"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return unique list of Magazine instances for this author's articles"""
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        """Create a new Article associated with this author and a magazine"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Return unique list of categories of magazines the author has contributed to"""
        mags = self.magazines()
        return list({mag.category for mag in mags}) if mags else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be 2-16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Magazine category must be a non-empty string")

        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be 2-16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Magazine category must be a non-empty string")
        self._category = value

    def articles(self):
        """Return list of Article instances published in this magazine"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique list of Author instances who have written for this magazine"""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        arts = self.articles()
        return [a.title for a in arts] if arts else None

    def contributing_authors(self):
        """Return authors who have written more than 2 articles for this magazine"""
        authors = [
            a for a in self.contributors()
            if len([art for art in a.articles() if art.magazine == self]) > 2
        ]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        """Return Magazine instance with most articles"""
        if not Article.all:
            return None
        magazine_counts = {
            mag: len([a for a in Article.all if a.magazine == mag])
            for mag in cls.all_magazines
        }
        return max(magazine_counts, key=magazine_counts.get)


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("title must be 5-50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title  # immutable

        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance")
        self._magazine = value

    @property
    def title(self):
        return self._title  # no setter → immutable

