"""player and coaching tables

Revision ID: 0acf4c156113
Revises: 7abbdd147499
Create Date: 2023-11-16 15:39:53.618971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0acf4c156113'
down_revision = '7abbdd147499'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coaching',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tactics', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('attendance', sa.String(length=200), nullable=True),
    sa.Column('fitness', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_player_attendance'), ['attendance'], unique=False)
        batch_op.create_index(batch_op.f('ix_player_date_of_birth'), ['date_of_birth'], unique=False)
        batch_op.create_index(batch_op.f('ix_player_firstname'), ['firstname'], unique=False)
        batch_op.create_index(batch_op.f('ix_player_fitness'), ['fitness'], unique=False)
        batch_op.create_index(batch_op.f('ix_player_lastname'), ['lastname'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('player', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_player_lastname'))
        batch_op.drop_index(batch_op.f('ix_player_fitness'))
        batch_op.drop_index(batch_op.f('ix_player_firstname'))
        batch_op.drop_index(batch_op.f('ix_player_date_of_birth'))
        batch_op.drop_index(batch_op.f('ix_player_attendance'))

    op.drop_table('player')
    op.drop_table('coaching')
    # ### end Alembic commands ###
