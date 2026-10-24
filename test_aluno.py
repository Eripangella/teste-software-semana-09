class Aluno:
    def __init__(self, nome, sobrenome, nota):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota)

class TestAluno(unittest.TestCase):
    
    def test_mostrar_aluno(self):
        aluno = Aluno("Carlos", "Silva", 8.5)
        resultado_esperado = "Aluno: Carlos Silva - Nota: 8.5"
        self.assertEqual(aluno.mostrarAluno(), resultado_esperado)

    def test_atributos_aluno(self):
        aluno = Aluno("Ana", "Souza", 10)
        self.assertEqual(aluno.nome, "Ana")
        self.assertEqual(aluno.sobrenome, "Souza")
        self.assertEqual(aluno.nota, 10)

if __name__ == '__main__':
    unittest.main()
