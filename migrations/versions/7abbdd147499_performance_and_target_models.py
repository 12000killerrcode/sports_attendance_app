"""performance and target models

Revision ID: 7abbdd147499
Revises: b2fe1016d226
Create Date: 2023-11-16 14:46:49.599220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7abbdd147499'
down_revision = 'b2fe1016d226'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.String(length=120), nullable=True),
    sa.Column('season', sa.String(length=120), nullable=True),
    sa.Column('wins', sa.Integer(), nullable=True),
    sa.Column('losses', sa.Integer(), nullable=True),
    sa.Column('draws', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('performance', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_performance_draws'), ['draws'], unique=False)
        batch_op.create_index(batch_op.f('ix_performance_losses'), ['losses'], unique=False)
        batch_op.create_index(batch_op.f('ix_performance_season'), ['season'], unique=False)
        batch_op.create_index(batch_op.f('ix_performance_wins'), ['wins'], unique=False)
        batch_op.create_index(batch_op.f('ix_performance_year'), ['year'], unique=False)

    op.create_table('target',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.String(length=120), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('target', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_target_year'), ['year'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('target', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_target_year'))

    op.drop_table('target')
    with op.batch_alter_table('performance', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_performance_year'))
        batch_op.drop_index(batch_op.f('ix_performance_wins'))
        batch_op.drop_index(batch_op.f('ix_performance_season'))
        batch_op.drop_index(batch_op.f('ix_performance_losses'))
        batch_op.drop_index(batch_op.f('ix_performance_draws'))

    op.drop_table('performance')
    # ### end Alembic commands ###
