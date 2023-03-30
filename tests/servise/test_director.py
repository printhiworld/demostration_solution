import pytest
from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService



@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name='d1')
    d2 = Director(id=2, name='d2')
    d3 = Director(id=3, name='d3')

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao



class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()
        assert len(director) > 0

    def test_get_create(self):
        new_director = {'name': 'new_director'}
        director = self.director_service.create(new_director)
        assert director is not None
        assert director.id is not None

    def test_get_delete(self):
        director = self.director_service.delete(1)


    def test_get_update(self):
        up_director = {'id': 3, 'name': 'a'}
        director = self.director_service.update(up_director)
