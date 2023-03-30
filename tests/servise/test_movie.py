from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    m1 = Movie(id=1, title='a', description='qwerty')
    m2 = Movie(id=2, title='b', description='trewq')
    m3 = Movie(id=3, title='c', description='qwert')

    movie_dao.get_one = MagicMock(return_value=m1)
    movie_dao.get_all = MagicMock(return_value=[m1, m2, m3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
    return movie_dao




class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()
        assert len(movie) > 0

    def test_get_create(self):
        new_movie = {'title': 'new_director', 'description': 'qwerty'}
        movie = self.movie_service.create(new_movie)
        assert movie is not None
        assert movie.id is not None

    def test_get_delete(self):
        movie = self.movie_service.delete(1)

    def test_get_update(self):
        up_movie = {'id': 3, 'title': 'new_director', 'description': 'qwerty'}
        movie = self.movie_service.update(up_movie)
