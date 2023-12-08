import requests
from assertpy import assert_that

from api_testing.base_request import BaseRequest

BASE_URL = "https://dog.ceo/api"


class BreedsList(BaseRequest):
    def __init__(self, path):
        self.path = f'{BASE_URL}{path}'


def should_get_list_sub_breeds():
    by_sub_breed = BreedsList(path="/breed/hound/list")
    response = by_sub_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_images_by_sub_breed():
    by_sub_breed = BreedsList(path="/breed/hound/afghan/images")
    response = by_sub_breed.get()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).is_instance_of(list)
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_random_image_by_sub_breed():
    by_sub_breed = BreedsList(path="/breed/hound/afghan/images/random")
    response = by_sub_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.json()["message"]).contains("jpg")
    assert_that(response.json()["status"]).is_equal_to("success")


def should_get_error_when_list_not_found_by_sub_breed():
    by_breed = BreedsList(path="/breed/ddd/list")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()["message"]).contains("not found")
    assert_that(response.json()["status"]).is_equal_to("error")


def should_get_error_when_all_list_not_found_by_sub_breed():
    by_breed = BreedsList(path="/breed/hound/ddd/images")
    response = by_breed.get(BreedsList)

    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.json()["message"]).contains("not found")
    assert_that(response.json()["status"]).is_equal_to("error")


should_get_list_sub_breeds()
should_get_images_by_sub_breed()
should_get_random_image_by_sub_breed()
should_get_error_when_list_not_found_by_sub_breed()
should_get_error_when_all_list_not_found_by_sub_breed()
