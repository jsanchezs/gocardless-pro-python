# WARNING: Do not edit by hand, this file was generated by Crank:
#
#   https://github.com/gocardless/crank
#

class MandatePdf(object):
    """A thin wrapper around a mandate_pdf, providing easy access to its
    attributes.

    Example:
      mandate_pdf = client.mandate_pdfs.get()
      mandate_pdf.id
    """

    def __init__(self, attributes, api_response):
        self.attributes = attributes
        self.api_response = api_response

    @property
    def expires_at(self):
        return self.attributes.get('expires_at')

    @property
    def url(self):
        return self.attributes.get('url')

