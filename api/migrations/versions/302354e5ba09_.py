"""empty message

Revision ID: 302354e5ba09
Revises: cb19e34e3060
Create Date: 2018-12-11 10:18:51.743684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '302354e5ba09'
down_revision = 'cb19e34e3060'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exam', sa.Column('exam_received_date', sa.DateTime(), nullable=True))
    op.drop_constraint('exam_ibfk_1', 'exam', type_='foreignkey')
    op.create_foreign_key(None, 'exam', 'booking', ['booking_id'], ['booking_id'], ondelete='set null')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'exam', type_='foreignkey')
    op.create_foreign_key('exam_ibfk_1', 'exam', 'booking', ['booking_id'], ['booking_id'])
    op.drop_column('exam', 'exam_received_date')
    # ### end Alembic commands ###