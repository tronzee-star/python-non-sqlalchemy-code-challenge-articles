import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        """magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.name, str)
        assert isinstance(magazine_2.name, str)

        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # comment out invalid assignment
        # magazine_2.name = 2
        # assert magazine_2.name == "AD"

        # use Exceptions instead
        with pytest.raises(Exception):
            Magazine(2, "Numbers")

    def test_name_len(self):
        """magazine name is between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert 2 <= len(magazine_1.name) <= 16
        assert 2 <= len(magazine_2.name) <= 16

        # comment out invalid assignment
        # magazine_1.name = "New Yorker Plus X"
        # assert magazine_1.name == "Vogue"

        # magazine_2.name = "A"
        # assert magazine_2.name == "AD"

        # use Exceptions instead
        with pytest.raises(Exception):
            magazine_1.name = "New Yorker Plus X"

        with pytest.raises(Exception):
            magazine_2.name = "A"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture"

    def test_category_is_mutable_string(self):
        """magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        assert isinstance(magazine_1.category, str)
        assert isinstance(magazine_2.category, str)

        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        assert isinstance(magazine_1.category, str)

        # comment out invalid assignment
        # magazine_2.category = 2
        # assert magazine_2.category == "Architecture"
        # assert isinstance(magazine_2.category, str)

        # use Exceptions instead
        with pytest.raises(Exception):
            Magazine("GQ", 2)

    def test_category_len(self):
        """magazine category has length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")

        assert magazine_1.category != ""

        # comment out invalid assignment
        # magazine_1.category = ""
        # assert magazine_1.category == "Fashion"
        # assert magazine_1.category != ""

        # use Exceptions instead
        with pytest.raises(Exception):
            magazine_1.category = ""

    # remaining tests unchanged...
