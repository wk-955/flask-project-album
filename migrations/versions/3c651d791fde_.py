"""empty message

Revision ID: 3c651d791fde
Revises: 
Create Date: 2019-11-14 16:56:32.921948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c651d791fde'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tag_name'), 'tag', ['name'], unique=True)
    op.create_table('roles_permissions',
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], )
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=254), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('website', sa.String(length=255), nullable=True),
    sa.Column('bio', sa.String(length=120), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('avatar_s', sa.String(length=64), nullable=True),
    sa.Column('avatar_m', sa.String(length=64), nullable=True),
    sa.Column('avatar_l', sa.String(length=64), nullable=True),
    sa.Column('avatar_raw', sa.String(length=64), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('locked', sa.Boolean(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('public_collections', sa.Boolean(), nullable=True),
    sa.Column('receive_comment_notification', sa.Boolean(), nullable=True),
    sa.Column('receive_follow_notification', sa.Boolean(), nullable=True),
    sa.Column('receive_collect_notification', sa.Boolean(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('follow',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_timestamp'), 'notification', ['timestamp'], unique=False)
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('filename', sa.String(length=64), nullable=True),
    sa.Column('filename_s', sa.String(length=64), nullable=True),
    sa.Column('filename_m', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('can_comment', sa.Boolean(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_photo_timestamp'), 'photo', ['timestamp'], unique=False)
    op.create_table('collect',
    sa.Column('collector_id', sa.Integer(), nullable=False),
    sa.Column('collected_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['collected_id'], ['photo.id'], ),
    sa.ForeignKeyConstraint(['collector_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('collector_id', 'collected_id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('replied_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], ),
    sa.ForeignKeyConstraint(['replied_id'], ['comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_timestamp'), 'comment', ['timestamp'], unique=False)
    op.create_table('tagging',
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tagging')
    op.drop_index(op.f('ix_comment_timestamp'), table_name='comment')
    op.drop_table('comment')
    op.drop_table('collect')
    op.drop_index(op.f('ix_photo_timestamp'), table_name='photo')
    op.drop_table('photo')
    op.drop_index(op.f('ix_notification_timestamp'), table_name='notification')
    op.drop_table('notification')
    op.drop_table('follow')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('roles_permissions')
    op.drop_index(op.f('ix_tag_name'), table_name='tag')
    op.drop_table('tag')
    op.drop_table('role')
    op.drop_table('permission')
    # ### end Alembic commands ###
