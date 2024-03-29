"""empty message

Revision ID: 47cafadb8f46
Revises: ebb2ca6b35f6
Create Date: 2021-05-26 18:49:10.548038

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '47cafadb8f46'
down_revision = 'ebb2ca6b35f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
