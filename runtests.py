import unittest
from server import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_01_server_rodando(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200, 'Servidor não está rodando')
    
    def test_02_telefone_9_digitos(self):
        data = {'ddd': '11', 'telefone': '912345678'}
        response = self.app.get('/telefone', query_string = data) #(f'/telefone?ddd={data["ddd"]}&telefone={data["telefone"]}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('válido', response.get_data(as_text=True), 'Esperado mensagem de telefone válido')
        self.assertIn("São Paulo", response.get_data(as_text=True), 'Esperado informação do Estado do DDD')

    def test_03_telefone_8_digitos(self):
        data = {'ddd': '35', 'telefone': '91234567'}
        response = self.app.get('/telefone', query_string = data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('válido', response.text, 'Esperado mensagem de telefone válido')
        self.assertIn('Minas Gerais', response.text, 'Esperado informação do Estado do DDD')

    def test_04_telefone_10_digitos(self):
        data = {'ddd': '51', 'telefone': '9123456789'}
        response = self.app.get('/telefone', query_string = data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Telefone precisa ter no máximo 9 dígitos', response.text, 'Esperado mensagem de erro do telefone')
    
    def test_05_ddd_invalido(self):
        data = {'ddd': '511', 'telefone': '912345678'}
        response = self.app.get('/telefone', query_string = data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('DDD precisa ter exatamente 2 dígitos', response.text, 'Esperado mensagem de erro do DDD')
        
    def test_06_ddd_e_telefone_invalidos(self):
        data = {'ddd': '511', 'telefone': '91234'}
        response = self.app.get('/telefone', query_string = data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('DDD precisa ter exatamente 2 dígitos', response.text, 'Esperado mensagem de erro do DDD')
        self.assertIn('Telefone precisa ter pelo menos 8 dígitos', response.text, 'Esperado mensagem de erro do telefone')
    

if __name__ == "__main__":
    unittest.main(failfast=True)
