"""Establish the migration chain for the modular monolith.

Revision ID: 20260816_0001
Revises: None
"""

revision: str = "20260816_0001"
down_revision: str | None = None
branch_labels: None = None
depends_on: None = None


def upgrade() -> None:
    """Domain tables are introduced by their owning product phases."""


def downgrade() -> None:
    """The foundation revision has no schema objects to remove."""
