# -*- coding: utf-8 -*-

import pytest
from testapp.models import Shop


@pytest.mark.django_db
def test_base():
    # TODO: To remove
    # Test database connection
    Shop.objects.all()
    Shop.objects.create(name='batard')
    assert Shop.objects.count() == 1