from django.test import TestCase, RequestFactory, Client
from bidplacing.models import *
from django.utils import timezone
from datetime import timedelta, datetime, time, date
from django.core.urlresolvers import reverse
from bidplacing.views import *
from bidplacing import forms


class ModelsTestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='test_un', password='test_pw')
        self.u2 = User.objects.create(username='test_un2', password='test_pw2')
        self.c = Category()
        self.p = Product()

        category = Category(category_name='test_category')
        self.c = category
        self.c.save()

        self.request = RequestFactory()

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

    #TODO continue last test
    #def testPlaceBadBid(self):
        #client = Client()
        #response = client.post('products/product/'+self.p.id+'/new-bid', {'amount': 4})
        #print response.status_code

#if __name__ == '__main__':
#    unittest.main()