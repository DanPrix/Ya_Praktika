class TestDatabase:

    def test_init(self, database):
        assert len(database.buns) > 0
        assert len(database.ingredients) > 0

    def test_getters(self, database):
        assert len(database.available_buns()) > 0
        assert len(database.available_ingredients()) > 0
