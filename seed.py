"""Seed file to make sample data for db."""

from unicodedata import name
from models import db, Pet
from app import app

# Create all tables
# db.drop_all()
# db.create_all()

# d1 = Department(dept_code="mktg", dept_name="Marketing", phone="987-9999")
# d2 = Department(dept_code="acct", dept_name="Accounting", phone="111-2222")
# d3 = Department(dept_code="r&d", dept_name="Research and Development", phone="908-7753")
# d4 = Department(dept_code="sales", dept_name="Sales", phone="532-9785")
# d5 = Department(dept_code="it", dept_name="Information Technology", phone="187-5432")
# river = Employee(name="River Bottom", state="NY", dept_code="mktg")
# joaquin = Employee(name="Joaquin Phoenix", dept_code="acct")
# summer = Employee(name="Summer Winter", state="OR", dept_code="mktg")
# octavia = Employee(name="Octavia Spencer", dept_code="r&d")
# larry = Employee(name="Larry David", state="NY", dept_code="r&d")
# kurt = Employee(name="Kurt Cobain", state="WA", dept_code="it")
# rain = Employee(name="Rain Phoenix", dept_code="it")

# db.session.add_all([d1, d2, d3, d4, d5])
# db.session.commit()

# db.session.add_all([river, joaquin, summer, octavia, larry, kurt, rain])
# db.session.commit()
db.drop_all()
db.create_all()

Pet.query.delete()

# Add sample employees and departments
fred = Pet(name="Fred", species="fish", photo_url="https://www.randomlists.com/img/animals/starfish.webp",
           age=1, notes="A smelly starfish", available=True)
zoe = Pet(name="Zoe", species="gopher",
          photo_url="https://www.randomlists.com/img/animals/gopher.webp")
kazoo = Pet(name="Kazoo", species="canary",
            photo_url="https://www.randomlists.com/img/animals/canary.webp", age=2, notes="A talkative bird")
carl = Pet(name="Carl", species="dog", notes="A friendly dog")
larry = Pet(name="Larry", species="bunny",
            photo_url="https://www.randomlists.com/img/animals/bunny.webp", age=3, available=False)

db.session.add_all([fred, zoe, kazoo, carl, larry])
db.session.commit()
