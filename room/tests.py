from django.test import Client, TestCase

from core.models import User
from room.models import Room


class PureEndpointsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(PureEndpointsTest, cls).setUpClass()
        cls.client1 = Client()
        cls.client2 = Client()
        cls.client3 = Client()

        cls.room1 = Room.objects.create(
            user_count=3,
            status=Room.Status.ACTIVE,
            figure=Room.Figure.SQUARE,
        )

        cls.room2 = Room.objects.create(
            user_count=4,
            status=Room.Status.DONE,
            figure=Room.Figure.SQUARE,
        )

    def test_room_creating(self):
        response = self.client1.post('/api/v1/rooms/', data={
            'user_count': 4,
            'figure': 1,
        })

        self.assertEqual(response.status_code, 201)

    def test_rooms_active_list(self):
        response = self.client1.get('/api/v1/rooms/')
        self.assertEqual(response.data['count'], 1)

    def test_rooms_done_list(self):
        response = self.client1.get('/api/v1/rooms/done/')
        self.assertEqual(response.data['count'], 0)

    def test_dot_creating(self):
        response = self.client1.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.4,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(float(response.data['dot']['abscissa']), 0.4)

        response = self.client1.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.5,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(float(response.data['dot']['abscissa']), 0.5)

    def test_game_played(self):
        response = self.client1.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.2,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 201)

        response = self.client2.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.1,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 201)

        response = self.client3.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.7,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 201)

        response = self.client1.get('/api/v1/rooms/done/')
        self.assertEqual(response.data['count'], 1)

        response = self.client3.post('/api/v1/join/', content_type='application/json', data={
            'room': self.room1.id,
            'dot': {
                'abscissa': 0.7,
                'ordinate': 0.6
            },
        })
        self.assertEqual(response.status_code, 400)
