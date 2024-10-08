"""tweaking things

Revision ID: b0c1157e30d5
Revises: 3fedbfb64715
Create Date: 2024-08-26 04:43:21.455831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0c1157e30d5'
down_revision: Union[str, None] = '3fedbfb64715'
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
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_added', sa.DATETIME(), nullable=True),
    sa.Column('date_last_updated', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.create_index('ix_blogs_id', 'blogs', ['id'], unique=False)
    # ### end Alembic commands ###