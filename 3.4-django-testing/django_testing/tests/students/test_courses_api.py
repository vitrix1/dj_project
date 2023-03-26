import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course_factory(_quantity=1)
    response = client.get('/api/v1/courses/1/')
    data = response.json()
    expected = Course.objects.all()
    assert response.status_code == 200
    assert expected[0].id == data['id']


@pytest.mark.django_db
def test_check_courses_list(client, course_factory):
    course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert Course.objects.count() == len(response.json())


@pytest.mark.django_db
def test_check_filtered_data(client, course_factory):
    course_factory(_quantity=10)
    response = client.get('/api/v1/courses/', data={'id': 5})
    data = response.json()
    expected = Course.objects.get(id=5)
    assert response.status_code == 200
    assert expected.id == data[0]['id']


@pytest.mark.django_db
def test_check_name_filtered_data(client):
    Course(name='test').save()
    response = client.get('/api/v1/courses/', data={'id': 1})
    data = response.json()
    expected = Course.objects.get(name='test')
    assert response.status_code == 200
    assert expected.name == data[0]['name']


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'test_create_course'})
    expected = Course.objects.get(name='test_create_course')
    data = response.json()
    assert response.status_code == 201
    assert expected.name == data['name']


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course_factory(_quantity=10)
    response_put = client.put('/api/v1/courses/1/', data={'name': 'test_create_course'})
    response_get = client.get('/api/v1/courses/1/')
    expected = Course.objects.get(name='test_create_course')
    data = response_get.json()
    assert response_put.status_code == 200
    assert expected.name == data['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course_factory(_quantity=10)
    response_delete = client.delete('/api/v1/courses/1/')
    response_get = client.get('/api/v1/courses/')
    assert response_delete.status_code == 204
    assert Course.objects.count() == len(response_get.json())
