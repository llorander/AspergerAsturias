import pytest  # type: ignore

import sqlite3

from src.domain.model.user import hash_password


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        f"""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id varchar primary key,
            username varchar,
            name varchar,
            password varchar,
            is_admin boolean
        );
        INSERT INTO users ( id, username, name, password, is_admin) values 
            ("user-1", "user-1@example.com", "User 1", '{hash_password("user-1-password")}', 1),
            ("user-2", "user-2@example.com", "User 2", '{hash_password("user-2-password")}', 0),
            ("user-3", "user-3@example.com", "User 3", '{hash_password("user-3-password")}', 0),
            ("user-4", "user-4@example.com", "User 4", '{hash_password("user-4-password")}', 0);
        """
    )
    return conn
