import pytest
from app.methods import add_concert, get_band_concerts
from app.database import SessionLocal

@pytest.fixture(scope="module")
def db():
    # Set up the database session
    session = SessionLocal()
    yield session
    # Teardown: close the session after tests are done
    session.close()

def test_add_concert(db):
    band_id = 1
    venue_id = 1
    date = "2024-09-30"
    concert = add_concert(db, band_id, venue_id, date)
    assert concert.id is not None

def test_get_band_concerts(db):
    band_id = 1
    concerts = get_band_concerts(db, band_id)
    assert len(concerts) > 0
