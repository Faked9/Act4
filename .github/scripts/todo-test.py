import unittest 
from todo import Task, Taskpool
from io import StringIO 
import sys 

class TestTaskPool(unittest.TestCase):

  def setUp(self)
      self.pool = TaskPool()

  def test_add_task(self):
      task = Task("New Task")
      self.pool.add_task(task)
      self.assertEqual(len(self.pool.tasks), 1)


  def test_get_open_tasks(self):
      self.pool.populate()
      open_tasks = self.pool.get_open_tasks()
      self.assertEqual(len(open_tasks), 3)
      self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

  def test_get_done_tasks(self):
      self.pool.populate()
      done_tasks = self.pool.get_done_tasks()
      self.assertEqual(len(done_tasks), 3)
      self.assertTrue(all(task.status == "Done" for task in done_tasks))

if __name__ == "__main__": 
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)

  captured_output = StringIO()

  #run tests with verbosity 2 
  result = unittest.TextTestRunner(stream=captured_output, verbosity=2).run(suite)

  #capture the relevant output 
  output_lines = captured_output.getvalue().splitlines()

  #print the output of each test with the status ok 
  for line in output_lines:
      if "ok" in line:
          print(line.spilt('')[0] +' ... ok')

  #print total, passed and failed summary
  total_test = result.testsRun
  failed_tests = [t[0] for t in result.failures + result.errors]
  passed_tests = [test for test in suite if test not in failed_tests]

  print(f"Total Tests: {total_tests}")
  print(f"Passed: {len(passed_tests)} ({(len(passed_tests) / total_tests) * 100:.2f}%)")
  print(f"Failed: {len(failed_tests)} ({(len(failed_tests) / total_tests) * 100:.2f}%)")
