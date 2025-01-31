from src.model.settings.db_metadata import metadata
from sqlalchemy import Table, Column, Integer, String

Pessoas = Table(
    "pessoas", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String)
)