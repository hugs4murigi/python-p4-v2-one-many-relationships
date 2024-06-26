"""changed tests

Revision ID: 910474d6adeb
Revises: abd424bc184b
Create Date: 2024-04-09 15:43:29.933621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '910474d6adeb'
down_revision = 'abd424bc184b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    # ### end Alembic commands ###