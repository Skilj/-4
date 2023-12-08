import requests
from assertpy import assert_that

from api_testing.base_request import BaseRequest

BASE_URL = "https://dog.ceo/api"


class BreedsList(BaseRequest):
    def __init__(self, path):
        self.path = f'{BASE_URL}{path}'


def should_get_list_images_by_breed():
    by_breed = BreedsList(path="/breed/hound/images")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_image_by_breed():
    by_breed = BreedsList(path="/breed/hound/images/random")
    response = by_breed.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).contains("jpg")
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_image_by_breed_with_quantity_50():
    by_breed = BreedsList(path="/breed/hound/images/random/50")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_error_when_not_found_breed():
    by_breed = BreedsList(path="/breed/ddd/images")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()["message"]).contains("not found")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_error_when_random_image_not_found_by_breed():
    by_breed = BreedsList(path="/breed/sss/images/random")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()["message"]).contains("not found")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_validation_when_quantity_is_negative():
    by_breed = BreedsList(path="/breed/hound/images/random/-1")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_validation_when_quantity_is_symbol():
    by_breed = BreedsList(path="/breed/hound/images/random/k")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.bad_request)
    assert_that(response.json()["message"]).contains("validation error")
    assert_that(response.json()["status"]).is_equal_to("error")


should_get_list_images_by_breed()
should_get_random_image_by_breed()
should_get_random_image_by_breed_with_quantity_50()
should_get_error_when_not_found_breed()
should_get_error_when_random_image_not_found_by_breed()
should_get_validation_when_quantity_is_negative()
should_get_validation_when_quantity_is_symbol()
