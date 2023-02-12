import requests, pytest

BASE_LINK = 'https://airportgap.dev-tester.com/'
BASE_API_LINK = 'https://airportgap.dev-tester.com/api'

def test_base_link_is_ok():
    res = requests.get(BASE_LINK)
    assert res.status_code == 200, "BASE LINK BROKEN +" + str(res.status_code)

def test_get_airports():
    res = requests.get(BASE_API_LINK + '/airports')
    print('\n' + res.text)
    assert res.status_code == 200, "AIRPORT LINK BROKEN +" + str(res.status_code)

