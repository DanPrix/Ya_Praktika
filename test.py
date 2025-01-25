import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Геном:Танцы на снегу')
        collector.add_new_book('Геном:Танцы на снегу')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_without_name_is_failed(self):
        collector = BooksCollector()
        collector.add_new_book('')

        assert '' not in collector.get_books_genre()

    def test_add_new_book_name_longer_than_40(self):
        collector = BooksCollector()
        long_name = ('A' * 41)
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()
        # assert len(long_name) == 40   Нужно исправить: закомментирован исполняемый код

    def test_set_book_genre_not_in_list_gender(self): # Нужно исправить: написан негативный тест на метод, но нет позитивных
        collector = BooksCollector()
        book_name = "Линии грез:Линия грез"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, " ")

        not_at_list_genre = collector.get_book_genre(book_name)

        assert book_name not in not_at_list_genre

    @pytest.mark.parametrize(
        "name, genre",
        [
            ("Лорд с планеты земля:Планета, которой нет", "Ужасы"),
            ("Диптаун:Лабиринт Отражений", "Детективы"),
            ("Лорд с планеты земля:Стеклянное море", "Ужасы")
        ]
    )
    def test_books_for_children_excludes_age_restricted_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        children_books = collector.get_books_for_children()

        assert 'name' not in children_books # Нужно исправить: происходит проверка текста 'name', а не переменной name

    @pytest.mark.parametrize(
        "name, genre",
        [
            ("Книга гор:Мальчик с планеты земля", "Мультфильмы"),
            ("Геном:Танцы на снегу", "Комедии"),
        ]
    )
    def test_books_for_children_includes_children_books(self, name, genre): # Нужно исправить: нарушен порядок, позитивные тесты должны проходить в первую очередь
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        children_books = collector.get_books_for_children()

        assert name in children_books

    @pytest.mark.parametrize( # Нужно исправить: т.к. в тесте используется parametrize, проверка значений происходит отдельно и тест не проверяет, то что метод должен выдавать список значений
        "name, genre",
        [
            ("Книга гор:Мальчик с планеты земля", "Мультфильмы"),
            ("Диптаун:Лабиринт Отражений", "Детективы"),
            ("Лорд с планеты земля:Стеклянное море", "Ужасы")
        ]
    )
    def test_get_books_with_specific_genre(self, name, genre): # Нужно исправить: нарушен поярдок выполнения методов
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        specific_genre = collector.get_books_with_specific_genre(genre)
        assert name in specific_genre

    def test_add_book_in_favorites_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Рыцари Сорока Островов')
        collector.set_book_genre('Рыцари Сорока Островов', 'Фантастика') # Можно улучшить: жанр книги не отображается в списке Избранное, следовательное производится лишнее действие
        book_collection = collector.get_books_genre()
        assert 'Рыцари Сорока Островов' in book_collection # Нужно исправить: текущий тест направлен на проверку метода добавляющего книгу в список Избранное, следовательно проверка get_books_genre лишняя
        collector.add_book_in_favorites('Рыцари Сорока Островов')
        favorite_books = collector.get_list_of_favorites_books()
        assert 'Рыцари Сорока Островов' in favorite_books

    def test_delete_book_from_favorites_not_from_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Звездный лабиринт:Черновик')
        collector.set_book_genre('Звездный лабиринт:Черновик', 'Фантастика') # Можно улучшить: жанр книги не отображается в списке Избранное, следовательное производится лишнее действие
        book_collection = collector.get_books_genre() # Нужно исправить: в коде есть переменная не используемая в тесте
        collector.add_book_in_favorites('Звездный лабиринт:Черновик')
        favorite_books = collector.get_list_of_favorites_books()
        assert 'Звездный лабиринт:Черновик' in favorite_books # Нужно исправить: текущий тест направлен на проверку метода удаления книги из списока Избранное, следовательно проверка наличия книги в списке лишняя

        collector.delete_book_from_favorites('Звездный лабиринт:Черновик')

        assert 'Звездный лабиринт:Черновик' not in favorite_books

    def test_get_book_genre(self): # Нужно исправить: нарушен поярдок выполнения методов
        collector = BooksCollector()
        book_name = "Звездный лабиринт:Черновик"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Фантастика")

        book_genre = collector.get_book_genre(book_name)

        assert book_genre == "Фантастика"

    def test_get_books_genre_two_added(self): # Нужно исправить: нарушен поярдок выполнения методов
        collector = BooksCollector()
        collector.add_new_book("Звездный лабиринт:Черновик")
        collector.set_book_genre("Звездный лабиринт:Черновик", "Фантастика")
        collector.add_new_book("Звездный лабиринт:Чистовик")
        collector.set_book_genre("Звездный лабиринт:Чистовик", "Ужасы")

        books_genre = collector.get_books_genre()

        expected_books_genre = {
            "Звездный лабиринт:Черновик": "Фантастика",
            "Звездный лабиринт:Чистовик": "Ужасы"
        }

        assert books_genre == expected_books_genre

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book_name = 'Рыцари Сорока Островов'
        second_book_name = 'Звёзды - холодные игрушки'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre) # Можно улучшить: жанр книги не отображается в списке Избранное, следовательное производится лишнее действие
        collector.add_new_book(second_book_name)
        collector.set_book_genre(second_book_name, genre) # Можно улучшить: жанр книги не отображается в списке Избранное, следовательное производится лишнее действие

        collector.add_book_in_favorites(second_book_name)

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Звёзды - холодные игрушки']

'''
Итоги
Основные погрешности замеченные в работе относятся неправильному порядку выполнения тестов и лишним проверкам assert,
не относящимся к задаче теста.
Из улучшений на которые стоит обратить: создание объекта класса в фикстуре и более подробное изучение методов программы
с целью определить выходные данные и не производить лишние действия при выполнении теста.
'''