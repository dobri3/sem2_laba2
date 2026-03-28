import unittest

from src.exceptions import InvalidDescriptionError, InvalidPriorityError, InvalidStatusError
from src.task import Task


class TestTask(unittest.TestCase):
    def test_task_correct_work(self):
        task = Task("обработать заказ", 1, "new")
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.description, "обработать заказ")
        self.assertEqual(task.status, "new")
        self.assertTrue(task.is_ready)

    def test_invalid_priority_error(self):
        with self.assertRaises(InvalidPriorityError):
            Task("ля ля ля", 1000, "new")

    def test_invalid_description_error(self):
        with self.assertRaises(InvalidDescriptionError):
            Task(123, 2, "new")

    def test_invelid_status_error(self):
        with self.assertRaises(InvalidStatusError):
            Task("la la la", 1, "old")

    def test_id_is_readonly(self):
        task = Task("tro lo lo", 1, "new")
        with self.assertRaises(AttributeError):
            task.id = "новый id"

    def test_created_at_is_readonly(self):
        task = Task("de lu lu", 2, "new")
        with self.assertRaises(AttributeError):
            task.created_at = "18:00"

    def test_is_ready_returns_false(self):
        task = Task("la la lend", 1, "done")
        self.assertEqual(task.is_ready, False)
