"""creating default user

Revision ID: 868a083ecfc4
Revises: 5b3f5c2f129a
Create Date: 2024-01-27 16:35:04.641495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '868a083ecfc4'
down_revision: Union[str, None] = '5b3f5c2f129a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""INSERT INTO USERS (email, password, first_name, last_name, cpf, created_at, updated_at)
                values 
                ('foo@test.com', '12345', 'Foo', 'User', '12345678911', now(), now())""")


def downgrade() -> None:
    op.execute("""DELETE FROM USER 
               where first_name='Foo' AND last_name='User' """)
