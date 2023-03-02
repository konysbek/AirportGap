import requests, pytest

BASE_LINK = 'https://airportgap.dev-tester.com/'
BASE_API_LINK = 'https://airportgap.dev-tester.com/api'


def test_base_link_is_ok():
    res = requests.get(BASE_LINK)
    assert res.status_code == 200, "BASE LINK BROKEN: " + str(res.status_code)


def test_get_airports():
    res = requests.get(BASE_API_LINK + '/airports')
    assert res.status_code == 200, "AIRPORT LINK BROKEN: " + str(res.status_code)


@pytest.mark.parametrize('air_id', ['KIX', 'NRT'])
def test_get_airport_by_id(air_id):
    res = requests.get(BASE_API_LINK + '/airports/' + air_id)
    assert res.status_code == 200, "NO SUCH AIRPORT: " + str(res.status_code)

# need to be parametrized
@pytest.mark.parametrize('par', ['?from=KIX&to=NRT'])
def test_calc_distance(par):
    res = requests.post(BASE_API_LINK + '/airports/distance' + par)
    assert res.json()['data']['attributes']['kilometers'] == 490.8053652969214, "WRONG KM DISTANCE"
    assert res.json()['data']['attributes']['miles'] == 304.76001022047103, "WRONG MILES DISTANCE"
    assert res.json()['data']['attributes']['nautical_miles'] == 264.82908133654655, "WRONG NM DISTANCE"
