"""added images

Revision ID: 3fedbfb64715
Revises: 8c0b4695f88a
Create Date: 2024-08-25 19:45:09.430047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fedbfb64715'
down_revision: Union[str, None] = '8c0b4695f88a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_blogs_id', table_name='blogs')
    op.drop_table('blogs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('title', sa.VARCHAR(length=30), nullable=True),
    sa.Column('slug', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('tag', sa.VARCHAR(length=20), nullable=True),
    sa.Column('members_only', sa.BOOLEAN(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_added', sa.DATETIME(), nullable=True),
    sa.Column('date_last_updated', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.create_index('ix_blogs_id', 'blogs', ['id'], unique=False)
    # ### end Alembic commands ###
