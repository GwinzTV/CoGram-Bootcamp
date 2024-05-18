from data_access import TaskRepository


class TaskService:
    def __init__(self):
        ''' Initialises TaskService with a TaskRepository. '''
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        ''' Get all tasks from the data source. '''
        return self.task_repository.get_tasks()

    def add_task(self, task):
        ''' Add new task to the data source. '''
        self.task_repository.save_task(task)

    def remove_task(self, task_title):
        ''' Delete task from data source '''
        self.task_repository.delete_task(task_title)
