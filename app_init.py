from sqlalchemy.exc import OperationalError, ProgrammingError

from app import ROLE_MAP
from applog import logger
from db import Base, SessionLocal, engine
from model.user import Role, User


def init_data():
    try:
        Base.metadata.create_all(bind=engine, checkfirst=True)
        logger.info("Tables created successfully")
    except (OperationalError, ProgrammingError) as e:
        logger.info(f"An error occurred during table creation: {str(e)}")

    db = SessionLocal()
    roles = db.query(Role).all()
    ids = [role.id for role in roles]
    for role_id, role_name in ROLE_MAP.items():
        if role_id not in ids:
            new_role = Role(id=role_id, name=role_name)
            db.add(new_role)
            logger.info(f"Initialize role: {role_name}")

    admin = db.query(User).filter(User.id == 1).first()
    if not admin:
        admin = User(id=1, role_id=1, name="admin", password="123123")
        db.add(admin)
        logger.info("Initialize admin")

    db.commit()
