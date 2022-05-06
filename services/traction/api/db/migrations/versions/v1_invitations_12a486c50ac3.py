"""v1-invitations

Revision ID: 12a486c50ac3
Revises: 0fbab19dd1f4
Create Date: 2022-05-04 13:00:33.959764

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "12a486c50ac3"
down_revision = "0fbab19dd1f4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "invitation",
        sa.Column(
            "invitation_id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("tags", postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column("connection", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("invitation", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("tenant_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("state", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("reusable", sa.Boolean(), nullable=False),
        sa.Column("public", sa.Boolean(), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False),
        sa.Column("connection_id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "connection_alias", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("invitation_url", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("invitation_key", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["tenant_id"],
            ["tenant.id"],
        ),
        sa.PrimaryKeyConstraint("invitation_id"),
    )
    op.create_index(op.f("ix_invitation_name"), "invitation", ["name"], unique=False)
    op.create_index(
        op.f("ix_invitation_invitation_key"),
        "invitation",
        ["invitation_key"],
        unique=False,
    )
    op.create_index(
        op.f("ix_invitation_tenant_id"), "invitation", ["tenant_id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_invitation_tenant_id"), table_name="invitation")
    op.drop_index(op.f("ix_invitation_name"), table_name="invitation")
    op.drop_table("invitation")
    # ### end Alembic commands ###
