from cleanPony.db.models import db, Location
from cleanPony.core.entities import Location as LocationEntity
from cleanPony.db.repositories import CrudRepository
from pony.orm import commit, db_session


repository = CrudRepository(Location, LocationEntity)


def setup_function():
    db.create_tables()
    add_data()


def teardown_function():
    db.drop_all_tables(with_all_data=True)


@db_session
def add_data():
    Location(id=1, name='test')
    commit()


def test_add_location():
    location_id = 2
    location = LocationEntity(id=location_id, name='location2')
    result = repository.save(location)

    assert result.id == location.id
    assert result.name == location.name


def test_update_location():
    location_id = 1
    location = repository.get(location_id)

    location_name = location.name
    location.name = 'updated_name'

    assert location_name != location.name
    assert location.id == location_id

    result = repository.save(location)

    assert result.id == location.id
    assert result.name == location.name
