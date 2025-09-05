import pytest
import allure
import os
from db import Database


@pytest.fixture(scope="module")
def db():
    with allure.step("Connecting to the DB"):
        db = Database(
            host=os.getenv("POSTGRES_HOST", "postgres_db"),
            dbname=os.getenv("POSTGRES_DB", "testdb"),
            user=os.getenv("POSTGRES_USER", "testuser"),
            password=os.getenv("POSTGRES_PASSWORD", "testpass"),
        )
        db.create_table()
    yield db
    with allure.step("Closing DB connection"):
        db.close()


@allure.feature("Database")
@allure.story("Insert")
def test_insert(db):
    with allure.step("Add user"):
        user_id = db.insert_user("TestUser", "test@example.com")

    with allure.step(f"Verify that user with id id={user_id} added"):
        user = db.get_user(user_id)
        assert user is not None, "Can nto find user in the DB"
        assert user["name"] == "TestUser", "User name is not correct"
        assert user["email"] == "test@example.com", "Email is not correct"


@allure.feature("Database")
@allure.story("Update")
def test_update(db):
    with allure.step("Add user for the 'update' action"):
        user_id = db.insert_user("OldName", "old@example.com")

    with allure.step(f"Updating user name with id={user_id}"):
        db.update_user(user_id, "NewName")

    with allure.step(f"Verify that user with id={user_id} changed"):
        user = db.get_user(user_id)
        assert user["name"] == "NewName", "User name was not updated"


@allure.feature("Database")
@allure.story("Delete")
def test_delete(db):
    with allure.step("Add user for the 'delete' action"):
        user_id = db.insert_user("DeleteMe", "delete@example.com")

    with allure.step(f"Deleting user with id={user_id}"):
        db.delete_user(user_id)

    with allure.step(f"Verify that user with id={user_id} was deleted"):
        user = db.get_user(user_id)
        assert user is None, "User deleted"
