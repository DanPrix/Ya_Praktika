from src.bun import Bun


class TestBun:

    def test_init_bun_with_correct_data(self):
        name = "test"
        price = 42.0
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_init_bun_with_empty_data(self):
        has_error = False
        try:
            Bun()
        except TypeError:
            has_error = True
        assert has_error

    def test_getters(self):
        name = "test"
        price = 42.0
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
