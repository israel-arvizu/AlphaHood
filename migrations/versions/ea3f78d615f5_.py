"""empty message

Revision ID: ea3f78d615f5
Revises: 
Create Date: 2022-06-29 15:19:38.271727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3f78d615f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('ticker', sa.String(length=5), nullable=True),
    sa.Column('marketCap', sa.BigInteger(), nullable=True),
    sa.Column('dayHigh', sa.Float(), nullable=True),
    sa.Column('dayLow', sa.Float(), nullable=True),
    sa.Column('currentPrice', sa.Float(), nullable=True),
    sa.Column('longBusinessSummary', sa.String(), nullable=True),
    sa.Column('fullTimeEmployees', sa.BigInteger(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('trailingPE', sa.Float(), nullable=True),
    sa.Column('dividendYield', sa.Float(), nullable=True),
    sa.Column('averageVolume', sa.BigInteger(), nullable=True),
    sa.Column('regularMarketOpen', sa.Float(), nullable=True),
    sa.Column('volume', sa.BigInteger(), nullable=True),
    sa.Column('fiftyTwoWeekHigh', sa.Float(), nullable=True),
    sa.Column('fiftyTwoWeekLow', sa.Float(), nullable=True),
    sa.Column('recommendationKey', sa.String(), nullable=True),
    sa.Column('industry', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('portfolios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('stockId', sa.Integer(), nullable=True),
    sa.Column('shares', sa.Integer(), nullable=True),
    sa.Column('priceBought', sa.Float(), nullable=True),
    sa.Column('dateBought', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['stockId'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('stockId', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('shares', sa.Float(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('type', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['stockId'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('watchlists',
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('stockId', sa.Integer(), nullable=True),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stockId'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watchlists')
    op.drop_table('transactions')
    op.drop_table('portfolios')
    op.drop_table('users')
    op.drop_table('stocks')
    # ### end Alembic commands ###