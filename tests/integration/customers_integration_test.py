# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import json

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers

@responses.activate
def test_customers_create():
    fixture = helpers.load_fixture('customers')['create']
    helpers.stub_response(fixture)
    response = helpers.client.customers.create(*fixture['url_params'])
    body = fixture['body']['customers']

    assert_is_instance(response, resources.Customer)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.company_name, body.get('company_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.email, body.get('email'))
    assert_equal(response.family_name, body.get('family_name'))
    assert_equal(response.given_name, body.get('given_name'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.language, body.get('language'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.swedish_identity_number, body.get('swedish_identity_number'))

@responses.activate
def test_customers_list():
    fixture = helpers.load_fixture('customers')['list']
    helpers.stub_response(fixture)
    response = helpers.client.customers.list(*fixture['url_params'])
    body = fixture['body']['customers']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Customer)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.address_line1 for r in response.records],
                 [b.get('address_line1') for b in body])
    assert_equal([r.address_line2 for r in response.records],
                 [b.get('address_line2') for b in body])
    assert_equal([r.address_line3 for r in response.records],
                 [b.get('address_line3') for b in body])
    assert_equal([r.city for r in response.records],
                 [b.get('city') for b in body])
    assert_equal([r.company_name for r in response.records],
                 [b.get('company_name') for b in body])
    assert_equal([r.country_code for r in response.records],
                 [b.get('country_code') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.email for r in response.records],
                 [b.get('email') for b in body])
    assert_equal([r.family_name for r in response.records],
                 [b.get('family_name') for b in body])
    assert_equal([r.given_name for r in response.records],
                 [b.get('given_name') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.language for r in response.records],
                 [b.get('language') for b in body])
    assert_equal([r.metadata for r in response.records],
                 [b.get('metadata') for b in body])
    assert_equal([r.postal_code for r in response.records],
                 [b.get('postal_code') for b in body])
    assert_equal([r.region for r in response.records],
                 [b.get('region') for b in body])
    assert_equal([r.swedish_identity_number for r in response.records],
                 [b.get('swedish_identity_number') for b in body])

@responses.activate
def test_customers_all():
    fixture = helpers.load_fixture('customers')['list']

    def callback(request):
        if 'after=123' in request.url:
          fixture['body']['meta']['cursors']['after'] = None
        else:
          fixture['body']['meta']['cursors']['after'] = '123'
        return [200, {}, json.dumps(fixture['body'])]

    url = 'http://example.com' + fixture['path_template']
    responses.add_callback(fixture['method'], url, callback)

    all_records = list(helpers.client.customers.all())
    assert_equal(len(all_records), len(fixture['body']['customers']) * 2)
    for record in all_records:
      assert_is_instance(record, resources.Customer)

@responses.activate
def test_customers_get():
    fixture = helpers.load_fixture('customers')['get']
    helpers.stub_response(fixture)
    response = helpers.client.customers.get(*fixture['url_params'])
    body = fixture['body']['customers']

    assert_is_instance(response, resources.Customer)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.company_name, body.get('company_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.email, body.get('email'))
    assert_equal(response.family_name, body.get('family_name'))
    assert_equal(response.given_name, body.get('given_name'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.language, body.get('language'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.swedish_identity_number, body.get('swedish_identity_number'))

@responses.activate
def test_customers_update():
    fixture = helpers.load_fixture('customers')['update']
    helpers.stub_response(fixture)
    response = helpers.client.customers.update(*fixture['url_params'])
    body = fixture['body']['customers']

    assert_is_instance(response, resources.Customer)

    assert_equal(response.address_line1, body.get('address_line1'))
    assert_equal(response.address_line2, body.get('address_line2'))
    assert_equal(response.address_line3, body.get('address_line3'))
    assert_equal(response.city, body.get('city'))
    assert_equal(response.company_name, body.get('company_name'))
    assert_equal(response.country_code, body.get('country_code'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.email, body.get('email'))
    assert_equal(response.family_name, body.get('family_name'))
    assert_equal(response.given_name, body.get('given_name'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.language, body.get('language'))
    assert_equal(response.metadata, body.get('metadata'))
    assert_equal(response.postal_code, body.get('postal_code'))
    assert_equal(response.region, body.get('region'))
    assert_equal(response.swedish_identity_number, body.get('swedish_identity_number'))

