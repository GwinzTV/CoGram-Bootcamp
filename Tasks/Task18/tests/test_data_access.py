import unittest
from data_access import TaskRepository


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # create a new task manager instance before each test
        self.task_man = TaskRepository()

    def test_add_task_fail(self):
        # Test if save_task method adds a task
        task_details = ['test1', 'this is test1', '2024-05-09']
        initial_task_num = len(self.task_man.get_tasks())
        self.task_man.save_task(task_details)
        final_task_num = len(self.task_man.get_tasks())
        self.assertEqual(final_task_num, initial_task_num)

    def test_add_task(self):
        # Test if save_task method adds a task
        task_details = ['test2', 'this is test2', '2024-05-09']
        initial_task_num = len(self.task_man.get_tasks())
        self.task_man.save_task(task_details)
        final_task_num = len(self.task_man.get_tasks())
        self.assertEqual(final_task_num, initial_task_num + 1)

    def test_remove_task(self):
        # test if delete task method correctly removes task
        task_title = 'test2'
        initial_task_num = len(self.task_man.get_tasks())
        self.task_man.delete_task(task_title)
        final_task_num = len(self.task_man.get_tasks())
        self.assertEqual(final_task_num, initial_task_num - 1)


if __name__ == "__main__":
    unittest.main()
