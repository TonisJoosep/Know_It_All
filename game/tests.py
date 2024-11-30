from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Game  # Impordime Game mudeli

class GameModelTest(TestCase):
    """
    Testiklass Game mudeli testimiseks.
    """
    def test_game_creation(self):
        """
        Test, mis kontrollib Game objekti loomist ja atribuutide õigsust.
        """
        user = User.objects.create_user(username='testuser', password='testpassword')  # Loome testkasutaja
        game = Game.objects.create(
            points=100,
            category='General Knowledge',
            difficulty='E',
            user=user  # Seome mängu testkasutajaga
        )
        # Kontrollime, kas mängu string representatsioon on ootuspärane
        self.assertEqual(str(game), "General Knowledge - E - testuser")
        self.assertEqual(game.points, 100)  # Kontrollime punktide väärtust
        self.assertEqual(game.category, "General Knowledge")  # Kontrollime kategooria väärtust
        self.assertEqual(game.difficulty, 'E')  # Kontrollime raskusastme väärtust
        self.assertEqual(game.user, user)  # Kontrollime, kas kasutaja on õigesti seotud


class SimpleViewsTestCase(TestCase):
    """
    Testiklass vaadete testimiseks.
    """
    def setUp(self):
        """
        See meetod käivitatakse enne iga testi, et luua vajalikud objektid.
        """
        self.client = Client()  # Loome kliendi HTTP päringute simuleerimiseks
        self.user = User.objects.create_user(username='testuser', password='testpassword')  # Loome testkasutaja

    def test_index_view(self):
        """
        Test index vaate (/) jaoks.
        """
        response = self.client.get('/')  # Simuleerime GET päringut avalehele
        self.assertEqual(response.status_code, 200)  # Kontrollime, kas päring oli edukas (status code 200)
        self.assertTemplateUsed(response, 'index.html')  # Kontrollime, kas kasutatakse õiget malli

    def test_options_view(self):
        """
        Test options vaate (/options/) jaoks.
        """
        response = self.client.get('/options/General Knowledge/')  # Simuleerime GET päringut
        self.assertEqual(response.status_code, 200)  # Kontrollime staatuse koodi
        self.assertTemplateUsed(response, 'options.html')  # Kontrollime malli
        # Kontrollime, kas kontekstis on olemas 'category_name' ja selle väärtus on õige
        self.assertEqual(response.context['category_name'], 'General Knowledge')

    def test_login_view_get(self):
        """
        Test login vaate GET päringu (/login/) jaoks.
        """
        response = self.client.get('/login/')  # Simuleerime GET päringut sisselogimise lehele
        self.assertEqual(response.status_code, 200)  # Kontrollime staatuse koodi
        self.assertTemplateUsed(response, 'registration/login.html')  # Kontrollime malli

    def test_login_view_post(self):
        """
        Test login vaate POST päringu (/login/) jaoks.
        """
        # Simuleerime POST päringut sisselogimise andmetega
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  # Kontrollime, kas toimub ümbersuunamine (302)
