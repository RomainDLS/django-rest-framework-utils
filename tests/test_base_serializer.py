# -*- coding: utf-8 -*-

import pytest

from nested_serializers.serializers import NestedSerializer
from testapp.models import Shop, Article



# ************ Test functions ************

@pytest.mark.django_db
def test_base_serialization():

    class ArticleSerializer(NestedSerializer):
        class Meta:
            model = Article
            fields = ('name', 'price')

    class ShopSerializer(NestedSerializer):
        
        articles = ArticleSerializer(many=True, required=False)
        class Meta:
            model = Shop
            fields = ('name', 'articles')

    # Create shop with serializer
    data = {
        'name': 'Shop 1',
        'articles': [
            {'name': 'Article 1', 'price': 24},
            {'name': 'Article 2', 'price': 29},
            {'name': 'Article 3', 'price': 34},
        ]
    }
    serializer = ShopSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    shop = Shop.objects.get(name='Shop 1')
    assert shop.articles.get(name='Article 1').price == 24
    assert shop.articles.get(name='Article 2').price == 29
    assert shop.articles.get(name='Article 3').price == 34