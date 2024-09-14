import pytest
from sqlalchemy.orm import Session
from app.models import Band, Venue, Concert
from app.database import SessionLocal, engine

# Dependency for testing
@pytest.fixture(scope="module")
def db():
    session = SessionLocal()
    yield session
    session.close()

def test_band_creation(db: Session):
    new_band = Band(name="The Rolling Stones", hometown="London")
    db.add(new_band)
    db.commit()
    assert new_band.id is not None

def test_venue_creation(db: Session):
    new_venue = Venue(title="Wembley Stadium", city="London")
    db.add(new_venue)
    db.commit()
    assert new_venue.id is not None
