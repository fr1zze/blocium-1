import pytest
from django.http import Http404
from django.urls import reverse

from blog.views import post_detail


@pytest.mark.parametrize('post_id', (3, 999))
def test_missing_post_returns_404(client, post_id):
    url = reverse('blog:post_detail', kwargs={'post_id': post_id})
    assert client.get(url).status_code == 404


@pytest.mark.parametrize('post_id', (-1, 3, 999))
def test_missing_post_error_contains_id(rf, post_id):
    with pytest.raises(Http404, match=f'id={post_id}'):
        post_detail(rf.get(f'/posts/{post_id}/'), post_id=post_id)


@pytest.mark.parametrize('value', ('-1', 'abc', '1.5'))
def test_invalid_post_url_returns_404(client, value):
    assert client.get(f'/posts/{value}/').status_code == 404
