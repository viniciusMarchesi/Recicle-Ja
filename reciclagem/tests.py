from django.test import TestCase, Client
from django.urls import reverse
from .models import Material, PontoDeColeta, Feedback
import json

class ReciclagemTestCase(TestCase):
    def setUp(self):
        # Cria materiais
        self.plastico = Material.objects.create(
            nome="Plástico", 
            slug="plastico", 
            instrucoes_preparo="Lave bem.", 
            icone="bi-droplet"
        )
        self.vidro = Material.objects.create(
            nome="Vidro", 
            slug="vidro", 
            instrucoes_preparo="Cuidado ao quebrar.", 
            icone="bi-cup"
        )
        
        # Cria ecopontos
        self.ponto_centro = PontoDeColeta.objects.create(
            nome="Ecoponto Centro",
            endereco="Rua A, 100",
            latitude=-22.9064,
            longitude=-47.0612,
            ativo=True
        )
        self.ponto_centro.materiais_aceitos.add(self.plastico, self.vidro)
        
        self.ponto_taquaral = PontoDeColeta.objects.create(
            nome="Ecoponto Taquaral",
            endereco="Parque Taquaral",
            latitude=-22.8732,
            longitude=-47.0498,
            ativo=True
        )
        self.ponto_taquaral.materiais_aceitos.add(self.plastico)
        
        self.client = Client()

    def test_models_creation(self):
        """Verifica se os modelos são criados corretamente."""
        self.assertEqual(Material.objects.count(), 2)
        self.assertEqual(PontoDeColeta.objects.count(), 2)
        self.assertEqual(str(self.plastico), "Plástico")
        self.assertEqual(str(self.ponto_centro), "Ecoponto Centro")

    def test_home_view(self):
        """Verifica se a página inicial carrega corretamente com status 200."""
        response = self.client.get(reverse('reciclagem:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Recicle-Já")
        self.assertContains(response, "Plástico")

    def test_api_pontos_coleta_all(self):
        """Verifica o endpoint JSON que retorna todos os ecopontos."""
        response = self.client.get(reverse('reciclagem:api_pontos_coleta'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['nome'], "Ecoponto Centro")
        self.assertIn("Plástico", data[0]['materiais'])

    def test_api_pontos_coleta_filter(self):
        """Verifica a filtragem de pontos de coleta por tipo de material."""
        # Filtra por Vidro (apenas Ecoponto Centro aceita)
        response = self.client.get(reverse('reciclagem:api_pontos_coleta') + "?material=vidro")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nome'], "Ecoponto Centro")

        # Filtra por Plástico (ambos aceitam)
        response = self.client.get(reverse('reciclagem:api_pontos_coleta') + "?material=plastico")
        self.assertEqual(len(json.loads(response.content)), 2)

    def test_enviar_feedback_valid(self):
        """Verifica o envio de feedback válido."""
        feedback_data = {
            'nome': 'João Teste',
            'email': 'joao@teste.com',
            'tipo_feedback': 'sugestao',
            'ponto_coleta': self.ponto_centro.id,
            'mensagem': 'Excelente iniciativa de coleta.'
        }
        response = self.client.post(
            reverse('reciclagem:enviar_feedback'), 
            data=feedback_data
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        
        # Verifica se salvou no banco
        self.assertEqual(Feedback.objects.count(), 1)
        fb = Feedback.objects.first()
        self.assertEqual(fb.nome, 'João Teste')
        self.assertEqual(fb.ponto_coleta, self.ponto_centro)

    def test_enviar_feedback_invalid(self):
        """Verifica se há erro ao enviar feedback sem mensagem obrigatória."""
        feedback_data = {
            'nome': 'Sem Mensagem',
            'email': '',
            'tipo_feedback': 'outro',
            'mensagem': ''  # Vazio (inválido)
        }
        response = self.client.post(
            reverse('reciclagem:enviar_feedback'), 
            data=feedback_data
        )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(Feedback.objects.count(), 0)
