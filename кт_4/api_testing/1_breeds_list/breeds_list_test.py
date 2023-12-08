import requests
from assertpy import assert_that

from api_testing.base_request import BaseRequest

BASE_URL = "https://dog.ceo/api"


class BreedsList(BaseRequest):
    def __init__(self, path):
        self.path = f'{BASE_URL}{path}'


def should_get_breeds_list():
    list_all_breeds = BreedsList(path="/breeds/list/all")
    response = list_all_breeds.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(dict)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_error_when_incorrect_request_method():
    list_all_breeds = BreedsList(path="/breeds/list/all")
    response = list_all_breeds.post(True)

    assert_that(response.status_code).is_equal_to(requests.codes.method_not_allowed)
    assert_that(response.json()["code"]).is_equal_to(405)
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_random_image_by_dog_name():
    list_all_breeds = BreedsList(path="/breed/affenpinscher/images/random")
    response = list_all_breeds.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).contains("jpg")
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_error_when_not_found_by_dog_name():
    list_all_breeds = BreedsList(path="/breed/dog/images/random")
    response = list_all_breeds.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()["message"]).contains("not found")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_error_when_not_found_by_dog_name_is_integer():
    list_all_breeds = BreedsList(path="/breed/1/images/random")
    response = list_all_breeds.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


should_get_breeds_list()
should_get_error_when_incorrect_request_method()
should_get_random_image_by_dog_name()
should_get_error_when_not_found_by_dog_name()
should_get_error_when_not_found_by_dog_name_is_integer()
