from src.lib.sqlite_based_repository import SqliteBasedRepository

from src.domain.model.task import Task


class TaskRepository(SqliteBasedRepository):
    def get_all(self):
        cursor = self._conn().cursor()
        cursor.execute("SELECT * FROM tasks;")
        return [
            Task(id_task=record["id_task"],
            name_task=record["name_task"],
            description_task=record["description_task"],
            points_task = record["points_task"],
            start_datetime = record["start_datetime"],
            end_datetime = record["end_datetime"],
            pending_task = bool(int(record["pending_task"])),
            id_user = record["id_user"])
            for record in cursor.fetchall()
        ]

    def get_by_id(self, id):
        cursor = self._conn().cursor()
        cursor.execute("""SELECT * FROM tasks WHERE tasks.id_task = ?""", (id,))
        record = cursor.fetchone()
        return Task(id_task=record["id_task"],
            name_task=record["name_task"],
            description_task=record["description_task"],
            points_task = record["points_task"],
            start_datetime = record["start_datetime"],
            end_datetime = record["end_datetime"],
            pending_task = bool(int(record["pending_task"])),
            id_user = record["id_user"])
        

    def save_task(self, task):
        conn = self._conn()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT or REPLACE INTO tasks
            ("id_task", "name_task", "description_task", "points_task", "start_datetime", "end_datetime", "pending_task", "id_user")
            VALUES (:id_task, :name_task, :description_task, :points_task, :start_datetime, :end_datetime, :pending_task, :id_user)
            """,
            {
                "id_task" : task["id_task"],
                "name_task" : task["name_task"], 
                "description_task" : task["description_task"],
                "points_task" : task["points_task"],
                "start_datetime" : task["start_datetime"],
                "end_datetime" : task["end_datetime"],
                "pending_task" : task["pending_task"],
                "id_user" : task["id_user"],
            },
        )
        conn.commit()

    def delete_task(self, id):
        conn = self._conn()
        cursor = conn.cursor()
        cursor.execute(
            """DELETE FROM tasks WHERE tasks.id_task = ?""", (id,))
        conn.commit()
