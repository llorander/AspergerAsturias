class Task:
    def __init__(self, id_task, name_task, description_task, points_task, start_datetime, end_datetime, pending_task, id_user):
        self.id_task = id_task
        self.name_task = name_task
        self.description_task = description_task
        self.points_task = points_task
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.pending_task = pending_task
        self.id_user = id_user 