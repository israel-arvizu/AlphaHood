from app.models import db, Stock


# Adds a demo user, you can add other users here if you want
def seed_stocks():
    TSLA = Stock(
            name='Tesla, Inc.',
            ticker='TSLA',
            marketCap=723124617216,
            dayHigh=749.91,
            dayLow=697.03,
            currentPrice=697.99,
            longBusinessSummary='Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. The company operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits. It provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; and purchase financing and leasing services. This segment is also involved in the provision of non-warranty after-sales vehicle services, sale of used vehicles, retail merchandise, and vehicle insurance, as well as sale of products to third party customers; services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners. This segment also offers service and repairs to its energy product customers, including under warranty; and various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was incorporated in 2003 and is headquartered in Austin, Texas.',
            fullTimeEmployees=99290,
            city='Austin',
            state='TX',
            trailingPE=94.32297,
            dividendYield=None,
            averageVolume=29000690,
            regularMarketOpen=733.45,
            volume=30062991,
            fiftyTwoWeekHigh=1243.49,
            fiftyTwoWeekLow=620.46,
            recommendationKey='buy',
            industry='Auto Manufacturers'
            )
    db.session.add(TSLA)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_stocks():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
