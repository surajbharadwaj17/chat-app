from typing import List
from sqlalchemy import MetaData, engine
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData, Table, Integer, Column, ForeignKey, String, ARRAY, event, TIMESTAMP
from sqlalchemy.dialects.postgresql import *
from sqlalchemy.schema import CreateSchema
from sqlalchemy.sql import func

class Tables:
    def __init__(self, schema:str, engine) -> None:
        self.schema = schema
        self.engine = engine
        self.metadata = MetaData(schema=self.schema, bind=self.engine)
        self.base = declarative_base(metadata=self.metadata)
    

    def user(self):
        return Table(
            "t_users",
            self.metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("name", String, nullable=False),
            Column("email", String, nullable=False),
            Column("created_at", TIMESTAMP, server_default=func.now())
        )

    def channel(self):
        return Table(
            "t_channels",
            self.metadata,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("name", String, nullable=False),
            Column("description",  String),
            Column("admin", Integer, ForeignKey("t_users.id")),
            Column("created_at", TIMESTAMP, server_default=func.now())
        )

    def _create(self):
        tables = [getattr(Tables,str(key))(self) for key in Tables.__dict__ if not key.startswith("_")]
        
        # Check if schema exists
        inspector = sqlalchemy.inspect(self.engine)
        if self.schema not in inspector.get_schema_names():
            self.engine.execute(CreateSchema(self.schema))

        self.metadata.create_all(self.engine)
        return self.metadata