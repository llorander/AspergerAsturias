class TaskInteractor:
    def __init__(self, config, task_repository):
        self.config = config
        self.task_repository = task_repository

    def get_all_tasks(self):
        return self.task_repository.get_all()

    def get_task_by_id(self, id):
        return self.task_repository.get_by_id(id)

    def save_task(self, task):
        return self.task_repository.save_task(task)

    def delete_task(self, id):
        return self.task_repository.delete_task(id)