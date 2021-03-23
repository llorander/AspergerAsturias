import pytest  # type: ignore

from src.domain.repository.task_repository import TaskRepository
from src.domain.interactor.task_interactor import TaskInteractor

import sqlite3


@pytest.fixture
def database():
    conn = sqlite3.connect(":memory:")
    conn.executescript(
        """
        DROP TABLE IF EXISTS tasks;
        CREATE TABLE tasks (
            id_task varchar primary key,
            name_task varchar,
            description_task varchar,
            points_task integer,
            start_datetime varchar,
            end_datetime varchar,
            pending_task varchar,
            id_user varchar
        );
        """
    )
    return conn


def test_should_get_empty_array_if_no_data(database):
    task_repository = TaskRepository(None, database)

    interactor = TaskInteractor(None, task_repository)

    all_tasks = interactor.get_all_tasks()

    assert all_tasks == []


def test_should_get_array_if_data(database):

    database.executescript(
        """
        INSERT INTO tasks (id_task, name_task, description_task, points_task, start_datetime, end_datetime, pending_task, id_user) values
            ("task-01", "task-name-01", "task-description-01", "10", "start-datetime-01", "end-datetime-01", "0", "id-user-01"),
            ("task-02", "task-name-02", "task-description-02", "10", "start-datetime-02", "end-datetime-02", "0", "id-user-02"),
            ("task-03", "task-name-03", "task-description-03", "10", "start-datetime-03", "end-datetime-03", "0", "id-user-03");
        """
    )
    task_repository = TaskRepository(None, database)

    interactor = TaskInteractor(None, task_repository)

    all_tasks = interactor.get_all_tasks()

    assert len(all_tasks) == 3

    assert all_tasks[0].id_task == "task-01"
    assert all_tasks[0].name_task == "task-name-01"
    assert all_tasks[0].description_task == "task-description-01"
    assert all_tasks[0].points_task == 10
    assert all_tasks[0].start_datetime == "start-datetime-01"
    assert all_tasks[0].end_datetime == "end-datetime-01"
    assert all_tasks[0].pending_task == False
    assert all_tasks[0].id_user == "id-user-01"

def test_should_get_task_by_id(database):

    database.executescript(
        """
        INSERT INTO tasks (id_task, name_task, description_task, points_task, start_datetime, end_datetime, pending_task, id_user) values
            ("task-01", "task-name-01", "task-description-01", "10", "start-datetime-01", "end-datetime-01", "0", "id-user-01"),
            ("task-02", "task-name-02", "task-description-02", "10", "start-datetime-02", "end-datetime-02", "0", "id-user-02"),
            ("task-03", "task-name-03", "task-description-03", "10", "start-datetime-03", "end-datetime-03", "1", "id-user-03");
        """
    )
    task_repository = TaskRepository(None, database)

    interactor = TaskInteractor(None, task_repository)

    requested_task = interactor.get_task_by_id("task-03")

    assert requested_task.id_task == "task-03"
    assert requested_task.name_task == "task-name-03"
    assert requested_task.pending_task == True

def test_should_save_task(database):

    task_repository = TaskRepository(None, database)
    interactor = TaskInteractor(None, task_repository)

    task = {
        "id_task" : "task-01",
        "name_task" : "name-task-01",
        "description_task" : "description-task-01",
        "points_task" : "10",
        "start_datetime" : "start-datetime-01",
        "end_datetime" : "end-datetime",
        "pending_task" : "0",
        "id_user" : "user-01",
    }

    interactor.save_task(task)
    requested_task = interactor.get_task_by_id("task-01")

    assert requested_task.id_task == "task-01"
    assert requested_task.name_task == "name-task-01"
    assert requested_task.pending_task == False

def test_should_delete_by_id(database):

    task_repository = TaskRepository(None, database)
    interactor = TaskInteractor(None, task_repository)

    database.executescript(
        """
        INSERT INTO tasks (id_task, name_task, description_task, points_task, start_datetime, end_datetime, pending_task, id_user) values
            ("task-01", "task-name-01", "task-description-01", "10", "start-datetime-01", "end-datetime-01", "0", "id-user-01"),
            ("task-02", "task-name-02", "task-description-02", "10", "start-datetime-02", "end-datetime-02", "0", "id-user-02"),
            ("task-03", "task-name-03", "task-description-03", "10", "start-datetime-03", "end-datetime-03", "1", "id-user-03");
        """
    )

    interactor.delete_task("task-02")
    all_tasks = interactor.get_all_tasks()

    assert len(all_tasks) == 2
    assert all_tasks[0].id_task == "task-01"
    assert all_tasks[1].id_task == "task-03"