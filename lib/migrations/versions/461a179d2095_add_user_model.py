"""Add User model

Revision ID: 461a179d2095
Revises: a28af33e6866
Create Date: 2023-06-12 12:49:46.417189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '461a179d2095'
down_revision = 'a28af33e6866'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_reviews_user_id_users'), 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_reviews_user_id_users'), type_='foreignkey')
        batch_op.drop_column('user_id')

    op.drop_table('users')
    # ### end Alembic commands ###
