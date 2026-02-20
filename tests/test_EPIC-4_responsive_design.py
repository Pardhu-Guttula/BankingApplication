import pytest


class TestResponsiveDesign:

    def test_page_load(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_responsive_layout(self):
        response = self.client.get('/')
        assert 'meta name="viewport"' in response.data.decode('utf-8')

    def test_element_visibility(self):
        response = self.client.get('/')
        assert '<div class="container">' in response.data.decode('utf-8')

    def test_style_inclusion(self):
        response = self.client.get('/')
        assert '<link rel="stylesheet" href="/static/css/styles.css">' in response.data.decode('utf-8')
