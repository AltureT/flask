"""empty message

Revision ID: 98636ccfa94e
Revises: a6815f1ca516
Create Date: 2021-06-14 19:52:41.436325

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '98636ccfa94e'
down_revision = 'a6815f1ca516'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follow',
                    sa.Column('follower_id', sa.Integer(), nullable=False),
                    sa.Column('followed_id', sa.Integer(), nullable=False),
                    sa.Column('timestamp', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
                    )
    op.drop_table('follows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
                    sa.Column('follower_id', sa.INTEGER(), nullable=False),
                    sa.Column('followed_id', sa.INTEGER(), nullable=False),
                    sa.Column('timestamp', sa.DATETIME(), nullable=True),
                    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
                    )
    op.drop_table('follow')
    # ### end Alembic commands ###
