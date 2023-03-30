import pytest
from unittest.mock import MagicMock
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='horror')
    g2 = Genre(id=2, name='comedy')
    g3 = Genre(id=3, name='drama')

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()
    return genre_dao

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_get_create(self):
        new_genre = {'name': 'new_genre'}
        genre = self.genre_service.create(new_genre)
        assert genre is not None
        assert genre.id is not None

    def test_get_delete(self):
        genre = self.genre_service.delete(1)


    def test_get_update(self):
        up_genre = {'id': 3, 'name': 'a'}
        genre = self.genre_service.update(up_genre)
