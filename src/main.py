from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()

class Thing(Base):
    __tablename__ = "thing"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

engine = create_engine("postgresql://postgres:postgres@postgresql/postgres")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    with Session(engine) as session:
        # Add some things
        for ii in range(5):
            thing = Thing(name=f"Thing {ii}")
            session.add(thing)
        session.commit()

        # Get everything
        things = session.query(Thing).order_by(Thing.name).all()
        for thing in things:
            print(thing.name)

        # Change something
        print("Updating Thing 2...")
        thing = session.query(Thing).where(Thing.name == "Thing 2").first()
        thing.name = "Thing 2 (updated)"
        session.commit()

        # Get everything again
        things = session.query(Thing).order_by(Thing.name).all()
        for thing in things:
            print(thing.name)

        # Delete something
        print("Deleting Thing 3...")
        thing = session.query(Thing).where(Thing.name == "Thing 3").first()
        session.delete(thing)

        # Get everything again
        things = session.query(Thing).order_by(Thing.name).all()
        for thing in things:
            print(thing.name)

