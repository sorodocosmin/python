import unittest
from stack import Stack, EmptyStackException


class MyTestCase(unittest.TestCase):
    def test_function_push(self):
        stack = Stack()
        self.assertEqual(0, stack.size())

        stack.push(1)
        self.assertEqual(1, stack.size())

        stack.push(["1", "2", "3"])
        self.assertEqual(2, stack.size())

        stack.push({
            "name": "Cosmin",
            "test": "test"
        })
        self.assertEqual(3, stack.size())

    def test_function_peek(self):
        stack = Stack()

        with self.assertRaises(EmptyStackException):
            stack.peek()

        stack.push("elem_1")
        stack.push("elem_2")

        self.assertEqual("elem_2", stack.peek())
        self.assertEqual(2, stack.size())

        stack.push((1, 2, 3, 4, 5))
        stack.push({"key": 'last_elem'})
        self.assertEqual({"key": 'last_elem'}, stack.peek())

        stack.push([1, 2, 3])
        list_elem = stack.peek()
        list_elem.append(4)
        # now, the last element in the stack should be [1, 2, 3]
        # it uses deepcopy
        self.assertEqual([1, 2, 3], stack.peek())

        self.assertEqual(5, stack.size())

    def test_function_pop(self):
        stack = Stack()

        with self.assertRaises(EmptyStackException):
            stack.pop()

        stack.push("elem_1")
        stack.push("elem_2")
        stack.push("elem_3")

        self.assertEqual("elem_3", stack.pop())
        self.assertEqual("elem_2", stack.pop())
        self.assertEqual(1, stack.size())

        stack.push([1, 2, 3])
        self.assertEqual([1, 2, 3], stack.pop())
        self.assertEqual("elem_1", stack.pop())

        with self.assertRaises(EmptyStackException):
            stack.pop()

        self.assertEqual(0, stack.size())


if __name__ == '__main__':
    unittest.main()
