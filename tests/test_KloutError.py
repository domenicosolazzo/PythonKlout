import unittest
from pythonklout import KloutError, RESPONSE_CODES

class PythonKloutErrorTestCase(unittest.TestCase):
    def setUp(self):
        self.error = KloutError(0, 'error')
    def tearDown(self):
        self.error = None
    def test_KloutErrorIsInstanceOfException(self):
        self.assertIsInstance(self.error, Exception)
    def test_KloutErrorAcceptACodeParamenter(self):
        error = KloutError(code=0)
        self.assertEquals(0, error.code)
        self.assertIsNotNone(error)
    def test_KloutErrorAcceptAMsgParamenter(self):
        error = KloutError(msg="Message")
        self.assertEquals("Message", error.msg)
        self.assertIsNotNone(error)
    def test_KloutErrorAsString(self):
        expected = '0: error'
        self.assertEquals(str(self.error), expected)

class ResponseCodeTestCase(unittest.TestCase):
    def testResponseCode200(self):
        expected = "OK: Success"
        actual = RESPONSE_CODES[200]
        self.assertEquals(actual, expected)
    def testResponseCode202(self):
        expected = "Accepted: The request was accepted and the user was queued for processing"
        actual = RESPONSE_CODES[202]
        self.assertEquals(actual, expected)
    def testResponseCode401(self):
        expected = "Not Authorized: either you need to provide authentication credentials, or the credentials provided aren't valid."
        actual = RESPONSE_CODES[401]
        self.assertEquals(actual, expected)
    def testResponseCode403(self):
        expected = "Bad Request: Your request is invalid and we'll return and error message that tells you why. This is the status code if you have exceeded the rate limit."
        actual = RESPONSE_CODES[403]
        self.assertEquals(actual, expected)
    def testResponseCode404(self):
        expected = "Not Found: either you are requesting an invalid URI or the resource in question doesn't exist."
        actual = RESPONSE_CODES[404]
        self.assertEquals(actual, expected)
    def testResponseCode500(self):
        expected = "Internal Server Error: we did something wrong."
        actual = RESPONSE_CODES[500]
        self.assertEquals(actual, expected)
    def testResponseCode502(self):
        expected = "Bad Gateway: returned if Klout is down or being upgraded."
        actual = RESPONSE_CODES[502]
        self.assertEquals(actual, expected)
    def testResponseCode503(self):
        expected = "Service Unavailable: the Klout servers are up, but are overloaded with requests. Try again later."
        actual = RESPONSE_CODES[503]
        self.assertEquals(actual, expected)
