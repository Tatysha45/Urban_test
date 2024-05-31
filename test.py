#-*- coding: utf-8 -*-


import unittest
from main import Student


class Student:
    def __init__(self):
        self.distance = 0

    def run(self):
        self.distance += 100

    def walk(self):
        self.distance += 50


class StudentMoveTest(unittest.TestCase):

    def test_walk_distance(self):
        student = Student()
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, "Дистанции не равны")

    def test_run_distance(self):
        student = Student()
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, "Дистанции не равны")

    def test_race(self):
        runner = Student()
        walker = Student()
        for _ in range(10):
            runner.run()
            walker.walk()
        self.assertGreater(runner.distance, walker.distance, "[бегущий человек] должен преодолеть дистанцию больше, чем [идущий человек]")


if __name__ == "__main__":
    unittest.main()
