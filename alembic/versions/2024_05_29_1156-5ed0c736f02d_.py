"""empty message

Revision ID: 5ed0c736f02d
Revises: f401365a6e35
Create Date: 2024-05-29 11:56:20.680175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ed0c736f02d'
down_revision: Union[str, None] = 'f401365a6e35'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
