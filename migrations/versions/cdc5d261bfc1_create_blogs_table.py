"""Create blogs table

Revision ID: cdc5d261bfc1
Revises: cacc8cf1e066
Create Date: 2024-08-23 15:59:55.372984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdc5d261bfc1'
down_revision: Union[str, None] = 'cacc8cf1e066'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###