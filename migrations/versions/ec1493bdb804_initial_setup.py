"""initial setup

Revision ID: ec1493bdb804
Revises: 
Create Date: 2019-09-12 16:14:52.770804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec1493bdb804'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('golink',
    sa.Column('destination_url', sa.String(length=300), nullable=True),
    sa.Column('keyword', sa.String(length=300), nullable=False),
    sa.Column('keyword_prefix', sa.String(length=300), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('keyword')
    )
    op.create_index(op.f('ix_golink_date_added'), 'golink', ['date_added'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_golink_date_added'), table_name='golink')
    op.drop_table('golink')
    # ### end Alembic commands ###
