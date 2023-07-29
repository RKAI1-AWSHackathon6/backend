"""01 create new table v1

Revision ID: ed83b9d9ba93
Revises: d4867f3a4c0a
Create Date: 2023-07-29 10:07:20.527387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed83b9d9ba93'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    
    # Create favourite table
    op.create_table(
        "favourites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("icon", sa.String(), nullable=True),
        sa.Column("symbol", sa.String(), nullable=True),
        sa.Column("rank", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_unique_constraint('uq_symbol', 'favourites', ['symbol'], schema='public')


    # Create Sentiment table
    op.create_table(
        "sentiments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("type", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("color", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create table sources
    op.create_table(
        "newspapersites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_rss", sa.String(), nullable=False),
        sa.Column("source_url", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create table rawdatas		
    op.create_table(	
        "articles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("body", sa.String(), nullable=False),
        sa.Column("tag", sa.String(), nullable=True),
        sa.Column("published_timestamp", sa.Integer(), nullable=True),
        sa.Column("thumbnail_image_link", sa.String(), nullable=False),
        sa.Column("origin_link", sa.String(), nullable=False),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("author", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("body_image", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(	
        "headlines",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("sentiment_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("hint", sa.String(), nullable=False),
        sa.Column("thumbnail_image_link", sa.String(), nullable=False),
        sa.Column("origin_link", sa.String(), nullable=False),
        sa.Column("publish_date", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.Integer(), nullable=False),
        sa.Column("tag", sa.String(), nullable=True),
        sa.Column("body", sa.String(), nullable=True),
        sa.Column("explain", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(	
        "userfavourites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("favourite_id", sa.Integer(), nullable=False),
        sa.Column("visible", sa.Boolean(), nullable=False, server_default="True"),
        sa.PrimaryKeyConstraint("id"),
    )
					
    op.create_table(
        "headlinefavourites",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("favourite_id", sa.Integer(), nullable=False),
        sa.Column("headline_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

def downgrade():
    
    op.drop_table("favourites")

    op.drop_table("sentiments")

    op.drop_table("sources")

    op.drop_table("rawdatas")

    op.drop_table("headlines")

    op.drop_table("userfavourites")
    
    op.drop_table("headlinefavourites")
