import unittest
from queue import Queue, EmptyQueueException


class MyTestCase(unittest.TestCase):
    def test_function_push(self):
        queue = Queue()
        self.assertEqual(0, queue.size())

        queue.push(1)
        self.assertEqual(1, queue.size())

        queue.push(["1", "2", "3"])
        self.assertEqual(2, queue.size())

        queue.push({
            "name": "Cosmin",
            "test": "test"
        })
        self.assertEqual(3, queue.size())

    def test_function_peek(self):
        queue = Queue()

        # Ensure that peek on an empty queue raises EmptyQueueException
        with self.assertRaises(EmptyQueueException):
            queue.peek()

        queue.push("elem_1")
        queue.push("elem_2")

        self.assertEqual("elem_1", queue.peek())
        self.assertEqual(2, queue.size())

        queue.push((1, 2, 3, 4, 5))
        queue.push({"key": 'last_elem'})
        self.assertEqual("elem_1", queue.peek())

        queue.push([1, 2, 3])
        queue.pop()  # remove "elem_1"
        queue.pop()  # remove "elem_2"
        queue.pop()  # remove (1, 2, 3, 4, 5)
        queue.pop()  # remove {"key": 'last_elem'}

        list_elem = queue.peek()
        list_elem.append(4)
        # now, the last element in the stack should be [1, 2, 3]
        self.assertEqual([1, 2, 3], queue.peek())

        self.assertEqual(1, queue.size())

    def test_function_pop(self):
        queue = Queue()
        with self.assertRaises(EmptyQueueException):
            queue.pop()

        queue.push("elem_1")
        queue.push("elem_2")
        queue.push("elem_3")

        self.assertEqual("elem_1", queue.pop())
        self.assertEqual("elem_2", queue.pop())
        self.assertEqual(1, queue.size())

        queue.push([1, 2, 3])
        self.assertEqual("elem_3", queue.pop())
        self.assertEqual([1, 2, 3], queue.pop())

        with self.assertRaises(EmptyQueueException):
            queue.pop()
        self.assertEqual(0, queue.size())


if __name__ == '__main__':
    unittest.main()
