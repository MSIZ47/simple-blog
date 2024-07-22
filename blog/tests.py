from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


# we have 2 setup methods(1:setUp,2:setUptestData)-->in first one django create everything on setup before every singel test
# and delete it after test ends and recreate it for the second test but in second method its class method so django create
# everythin on setuptestdata for once then every test uses that.....so the point is if the thing you are creating in setup
# and you dont change it its better to use  setuptestdata but if any test is changing the values in setup method its better
# to use setup

class BlogPostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='post1',
            text='this is django',
            author=cls.user,
            status=Post.STATUS_CHOICES[0][0],
        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='this is django2',
            author=cls.user,
            status=Post.STATUS_CHOICES[1][0],
        )

    # testing attributes

    def test_post_model_str_is_returned(self):  # for checking __st__ of model
        self.assertEqual(str(self.post1), 'post1')

    def test_post_detail_is_truley_returned(self):
        self.assertEqual(self.post1.title, 'post1')

    # testing urls

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_on_blog_page_exists(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_name(self):
        response = self.client.get(
            reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_on_blog_detail_page_exists(self):
        response = self.client.get(
            reverse('post_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_post_id_exists_or_404(self):
        response = self.client.get(
            reverse('post_detail', args=[self.post1.id+500]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'Test Title',
            'text': 'Test Text',
            'author': self.user.id,
            'status': 'Pub'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Test Title')
        self.assertEqual(Post.objects.last().text, 'Test Text')

    def test_post_update_view(self):
        response = self.client.post(reverse('update_post', args=[self.post2.id]), {
            'title': 'Test Title',
            'text': 'this is django updated',
            'status': 'Pub',
            'author': self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Test Title')
        self.assertEqual(Post.objects.last().text, 'this is django updated')

    def test_post_delete_view(self):
        response = self.client.post(
            reverse('delete_post', args=[self.post2.id]))
        self.assertEqual(response.status_code, 302)


    