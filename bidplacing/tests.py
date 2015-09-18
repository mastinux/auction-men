from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse
from bidplacing.views import *


class ModelsTestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='test_un', password='test_pw')
        self.u2 = User.objects.create(username='test_un2', password='test_pw2')
        self.c = Category.objects.create(category_name='test_category')

        self.client = Client()
        self.request = RequestFactory()

    def testPurchasedProductsPageRedirect(self):
        self.client.logout()
        response = self.client.get(reverse('bidplacing:purchased_products_page'))

        self.assertEqual(response.status_code, 302)

    def testAddProduct(self):
        request = self.request.post(reverse('bidplacing:new_product'), {'product_name': 'test_product',
                                                                        'start_price': 5,
                                                                        'category': self.c})
        request.user = self.u
        response = new_product(request)

        self.assertEqual(response.status_code, 200)

    def testAddProductNegativePrice(self):
        form = ProductForm({'product_name': 'test_product',
                            'start_price': -64,
                            'category': self.c})

        self.assertFalse(form.is_valid())