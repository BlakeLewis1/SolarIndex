import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db 
from application.models import Planets, Solar
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()



    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class Testsolar(TestBase):

    def test_add_new_solar(self):
        with self.client:
            response = self.client.post(
                '/solar',
                data=dict(
                    solar_name="Test Title"
                    
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)

    def test_add_new_planet(self):
        with self.client:
            self.client.post(
                '/solar',
                data=dict(
                    solar_name="Test Title"
                    
                ),
                follow_redirects=True
            )
            response = self.client.post(
                '/planet',
                data=dict(
                    planet_name="Test Title",
                    astronomical_type="Test Title",
                    describe="Test Title",
                    ssystem=1
                    
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)
            self.assertEqual(response.status_code, 200)

    def test_add_new_planeterror(self):
        with self.client:
            self.client.post(
                '/solar',
                data=dict(
                    solar_name="Test Title"
                    
                ),
                follow_redirects=True
            )
            response = self.client.post(
                '/planet',
                data=dict(
                    planet_name="",
                    astronomical_type="",
                    describe="",
                    ssystem=1
                    
                ),
                follow_redirects=True
            )
            self.assertIn(b'Test Title', response.data)

    def test_update_planet(self):
        with self.client:
            self.client.post(
                '/solar',
                data=dict(
                    solar_name="Test Title"
                    
                ),
                follow_redirects=True
            )
            response = self.client.post(
                '/planet',
                data=dict(
                    planet_name="test title",
                    astronomical_type="test title",
                    describe="test title",
                    ssystem=1
                    
                ),
                follow_redirects=True
            )

            response = self.client.post(
                '/test title/update',
                data=dict(
                    planet_name="test planet",
                    astronomical_type="test planet",
                    describe="test planet",
                    ssystem=1
                ),
                follow_redirects=True
            )
            self.assertIn(b'test planet', response.data)

    def test_delete_planet(self):
        with self.client:
            self.client.post(
                '/solar',
                data=dict(
                    solar_name="Test Title"
                    
                ),
                follow_redirects=True
            )
            response = self.client.post(
                '/planet',
                data=dict(
                    planet_name="test planet",
                    astronomical_type="test planet",
                    describe="test planet",
                    ssystem=1
                    
                ),
                follow_redirects=True
            )
            redirectpage=url_for('deleteplanet', name = "test planet")
            response = self.client.get(redirectpage)
            self.assertEqual(Planets.query.count(),0) 

    def test_delete_solar(self):
        with self.client:
            self.client.post(
                '/solar',
                data=dict(
                    solar_name="test title"
                    
                ),
                follow_redirects=True
            )
            self.client.post(
                '/planet',
                data=dict(
                    planet_name="test planet",
                    astronomical_type="test planet",
                    describe="test planet",
                    ssystem=1
                ),
                follow_redirects=True
            )
            
            redirectpage=url_for('deletesolar', name = 1)
            response = self.client.get(redirectpage)
            self.assertEqual(Solar.query.count(),0)
            self.assertEqual(Solar)



         
