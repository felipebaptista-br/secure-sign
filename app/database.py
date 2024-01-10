from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

connection_string = URL.create(
    drivername='postgresql',
    username='felipe.baptista06',
    password='RCLlgP1K3Axw',
    host='ep-shrill-butterfly-47488354.us-east-2.aws.neon.tech',
    database='secure-sign',
    query={
        'sslmode': 'require',
    }
)

engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()
