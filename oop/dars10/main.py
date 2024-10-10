from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ma'lumotlar bazasiga ulanish
engine = create_engine('sqlite:///talabalar.db')
Base = declarative_base()

# Talabalar jadvalini yaratish
class Talaba(Base):
    __tablename__ = 'talabalar'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ism = Column(String, nullable=False)
    familiya = Column(String, nullable=False)
    guruh_kodi = Column(String, nullable=False)
    tugilgan_sana = Column(Date)
    telefon_raqami = Column(String)
    email = Column(String)

# Jadvalni yaratish
Base.metadata.create_all(engine)

# Sessiyani yaratish
Session = sessionmaker(bind=engine)
session = Session()

# Kayumov Davronjonning ma'lumotlarini kiritish
yangi_talaba = Talaba(
    ism='Davronjon',
    familiya='Kayumov',
    guruh_kodi='D-404',
    tugilgan_sana='2002-03-15',
    telefon_raqami='+998901234570',
    email='davronjon@example.com'
)

# Ma'lumotlarni saqlash
session.add(yangi_talaba)
session.commit()

print("Ma'lumotlar muvaffaqiyatli kiritildi!")
