# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

import requests
import responses
from nose.tools import assert_equal, assert_is_instance

from gocardless_pro import resources
from gocardless_pro import list_response

from .. import helpers

@responses.activate
def test_payouts_list():
    fixture = helpers.load_fixture('payouts')['list']
    helpers.stub_response(fixture)
    response = helpers.client.payouts.list(*fixture['url_params'])
    body = fixture['body']['payouts']

    assert_is_instance(response, list_response.ListResponse)
    assert_is_instance(response.records[0], resources.Payout)

    assert_equal(response.before, fixture['body']['meta']['cursors']['before'])
    assert_equal(response.after, fixture['body']['meta']['cursors']['after'])

    assert_equal([r.amount for r in response.records],
                 [b.get('amount') for b in body])
    assert_equal([r.created_at for r in response.records],
                 [b.get('created_at') for b in body])
    assert_equal([r.currency for r in response.records],
                 [b.get('currency') for b in body])
    assert_equal([r.id for r in response.records],
                 [b.get('id') for b in body])
    assert_equal([r.reference for r in response.records],
                 [b.get('reference') for b in body])
    assert_equal([r.status for r in response.records],
                 [b.get('status') for b in body])

@responses.activate
def test_payouts_get():
    fixture = helpers.load_fixture('payouts')['get']
    helpers.stub_response(fixture)
    response = helpers.client.payouts.get(*fixture['url_params'])
    body = fixture['body']['payouts']

    assert_is_instance(response, resources.Payout)

    assert_equal(response.amount, body.get('amount'))
    assert_equal(response.created_at, body.get('created_at'))
    assert_equal(response.currency, body.get('currency'))
    assert_equal(response.id, body.get('id'))
    assert_equal(response.reference, body.get('reference'))
    assert_equal(response.status, body.get('status'))
    assert_equal(response.links.creditor,
                 body.get('links')['creditor'])
    assert_equal(response.links.creditor_bank_account,
                 body.get('links')['creditor_bank_account'])

