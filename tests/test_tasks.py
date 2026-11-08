
import unittest
from tasks import add_task, complete_task


class TestTaskFlow(unittest.TestCase):

    def test_agregar_tarea(self):
        tareas = []
        add_task(tareas, "Estudiar Python")

        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["title"], "Estudiar Python")
        self.assertFalse(tareas[0]["completed"])

    def test_evitar_duplicados(self):
        tareas = []
        add_task(tareas, "Estudiar Python")
        add_task(tareas, "estudiar python")

        self.assertEqual(len(tareas), 1)

    def test_completar_tarea(self):
        tareas = []
        add_task(tareas, "Realizar actividad")
        complete_task(tareas, 1)

        self.assertTrue(tareas[0]["completed"])


if __name__ == "__main__":
    unittest.main()
