import config


class TaskRepository:
    def __init__(self):
        self.db = config.FILENAME
        self.localCache = []
        self.updated = False

    def get_tasks(self):
        ''' Retrieve tasks from data source. '''
        if not self.updated:
            tasks = []
            with open(self.db, 'r') as file:
                for line in file:
                    task_details = line.strip().split(" : ")
                    tasks.append(task_details)
                # each task = [title, details, due time]
                self.localCache = tasks
                self.updated = True
                return tasks
        return self.localCache

    def save_task(self, task_details):
        ''' Save a task to the data sink. '''
        with open(self.db, 'a') as file:
            task_line = ' : '.join(task_details) + '\n'
            file.write(task_line)
        self.updated = False

    def delete_task(self, task_title):
        ''' Delete a task from data source '''
        # read the file
        with open(self.db, 'r') as file:
            lines = file.readlines()
        # filter the task list to exclude task to delete
        lines = [line for line in lines if task_title not in line]
        # update the file
        with open(self.db, 'w') as file:
            file.writelines(lines)
        self.updated = False
