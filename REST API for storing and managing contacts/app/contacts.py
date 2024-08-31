from datetime import date, timedelta

@router.get("/contacts/search/", response_model=List[schemas.Contact])
def search_contacts(query: str, db: Session = Depends(get_db)):
    return db.query(models.Contact).filter(
        models.Contact.first_name.contains(query) | 
        models.Contact.last_name.contains(query) | 
        models.Contact.email.contains(query)
    ).all()

@router.get("/contacts/upcoming_birthdays/", response_model=List[schemas.Contact])
def upcoming_birthdays(db: Session = Depends(get_db)):
    today = date.today()
    next_week = today + timedelta(days=7)
    return db.query(models.Contact).filter(
        models.Contact.birthday.between(today, next_week)
    ).all()
