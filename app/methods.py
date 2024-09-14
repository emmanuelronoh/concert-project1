from sqlalchemy.orm import Session
from .models import Band, Venue, Concert

def add_concert(db: Session, band_id: int, venue_id: int, date: str):
    db_concert = Concert(band_id=band_id, venue_id=venue_id, date=date)
    db.add(db_concert)
    db.commit()
    db.refresh(db_concert)
    return db_concert

def get_band_concerts(db: Session, band_id: int):
    return db.query(Concert).filter(Concert.band_id == band_id).all()

def get_venue_concerts(db: Session, venue_id: int):
    return db.query(Concert).filter(Concert.venue_id == venue_id).all()
