"""Fixed many to many

Revision ID: 290f4591085c
Revises: 4a0968179297
Create Date: 2024-05-03 10:37:38.461660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '290f4591085c'
down_revision: Union[str, None] = '4a0968179297'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('phone_tag_association', 'phone_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('phone_tag_association', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('phone_tag_association_phone_id_tag_id_key', 'phone_tag_association', type_='unique')
    op.create_unique_constraint('idx_unique_tag_phone', 'phone_tag_association', ['phone_id', 'tag_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('idx_unique_tag_phone', 'phone_tag_association', type_='unique')
    op.create_unique_constraint('phone_tag_association_phone_id_tag_id_key', 'phone_tag_association', ['phone_id', 'tag_id'])
    op.alter_column('phone_tag_association', 'tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('phone_tag_association', 'phone_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
