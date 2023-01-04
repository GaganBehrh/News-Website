from django.test import SimpleTestCase
from django.urls import reverse, resolve
from newsblog.views import PostView



# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_post(self):
        url = reverse('post_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func, views.PostView)
