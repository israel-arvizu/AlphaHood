"""empty message

Revision ID: d8c49b2dd869
Revises:
Create Date: 2022-06-26 23:31:49.752861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8c49b2dd869'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stocks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=60), nullable=True),
    sa.Column('Ticker', sa.String(length=5), nullable=True),
    sa.Column('MarketCap', sa.Float(), nullable=True),
    sa.Column('HighToday', sa.Float(), nullable=True),
    sa.Column('LowToday', sa.Float(), nullable=True),
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
    op.create_table('watchlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('stockId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stockId'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchaseHistories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('stockId', sa.Integer(), nullable=False),
    sa.Column('priceBought', sa.Float(), nullable=False),
    sa.Column('sharesBought', sa.Integer(), nullable=False),
    sa.Column('dateBought', sa.Date(), nullable=False),
    sa.Column('priceSold', sa.Float(), nullable=True),
    sa.Column('sharesSold', sa.Float(), nullable=True),
    sa.Column('dateSold', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['stockId'], ['stocks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('watchlists')
    op.drop_table('portfolios')
    op.drop_table('users')
    op.drop_table('stocks')
    op.drop_table('purchaseHistories')
    # ### end Alembic commands ###
