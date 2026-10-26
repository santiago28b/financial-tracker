from domain.category import Category
from uuid import UUID, uuid4
from datetime import date


def test_new_categories():
    first = Category(user_id= uuid4(), name= 'ensalsa', )
    second = Category(user_id= uuid4(), name= 'ensalsa')
    assert first.category_id != second.category_id
    assert first.name == second.name
