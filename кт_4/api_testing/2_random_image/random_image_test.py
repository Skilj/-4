import requests
from assertpy import assert_that

from api_testing.base_request import BaseRequest

BASE_URL = "https://dog.ceo/api"


class BreedsList(BaseRequest):
    def __init__(self, path):
        self.path = f'{BASE_URL}{path}'


def should_get_random_image_from_dogs_list():
    random_image = BreedsList(path="/breeds/image/random")
    response = random_image.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).contains("jpg")
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_list_by_quantity():
    random_image = BreedsList(path="/breeds/image/random/1")
    response = random_image.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_validation_error_when_by_zero():
    random_image = BreedsList(path="/breeds/image/random/0")
    response = random_image.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_validation_error_when_negative_integer():
    random_image = BreedsList(path="/breeds/image/random/-1")
    response = random_image.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_random_list_by_quantity_2():
    random_image = BreedsList(path="/breeds/image/random/2")
    response = random_image.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_list_by_quantity_49():
    random_image = BreedsList(path="/breeds/image/random/49")
    response = random_image.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_list_by_quantity_50():
    random_image = BreedsList(path="/breeds/image/random/50")
    response = random_image.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_error_when_random_list_by_quantity_51():
    random_image = BreedsList(path="/breeds/image/random/51")
    response = random_image.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


should_get_random_image_from_dogs_list()
should_get_random_list_by_quantity()
should_get_validation_error_when_by_zero()
should_get_random_list_by_quantity_2()
should_get_random_list_by_quantity_49()
should_get_random_list_by_quantity_50()
should_get_error_when_random_list_by_quantity_51()
