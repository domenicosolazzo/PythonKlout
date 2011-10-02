import unittest
from pythonklout import Klout, KloutService, TestKloutService
class PythonKloutTestCase(unittest.TestCase):

    def setUp(self):
        key = "Key"
        self.klout = Klout(key,serviceType="test")

    def tearDown(self):
        self.klout = None

    def test_kloutInstanceIsNotNone(self):
        self.assertIsNotNone(self.klout)
    def test_kloutKeyIsNotNone(self):
        self.assertIsNotNone(self.klout._apiKey)
    """
        GetProxyFactory method
    """
    def test_getProxyFactory_exists(self):
        self.assertTrue(callable(getattr(self.klout, "_Klout__getProxyFactory")))
    def test_getProxyFactory_returnsAKloutServiceInstance(self):
        self.assertIsInstance(self.klout._Klout__getProxyFactory("test"), KloutService)
    def test_getProxyFactory_returnsATestKloutServiceInstance(self):
        self.assertIsInstance(self.klout._Klout__getProxyFactory("test"), TestKloutService)
    """
        Score method
    """
    def test_score_exists(self):
        self.assertTrue(callable(getattr(self.klout, "score")))
    def test_score_ShouldRaiseAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.klout.score,None)
        self.assertRaises(Exception, self.klout.score, 1)
        self.assertRaises(Exception, self.klout.score, "Score")
        self.assertRaises(Exception, self.klout.score, Klout(""))
    def test_score_ShouldAcceptAListOrTuple(self):
        self.assertIsInstance(getattr(self.klout, "score")(["user"]), type({}))
    def test_score_raisesExceptionIfInputIsEmpty(self):
        self.assertRaises(Exception, self.klout.score, [])
        self.assertRaises(Exception, self.klout.score, ())
    def test_score_resultIsNotEmpty(self):
        self.assertNotEquals(self.klout.score(["user"]), [])
    """
        Show method
    """
    def test_show_exists(self):
        self.assertTrue(callable(getattr(self.klout, "show")))
    def test_show_ShourldRaiseAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.klout.show, None)
        self.assertRaises(Exception, self.klout.show, 1)
        self.assertRaises(Exception, self.klout.show, "Score")
        self.assertRaises(Exception, self.klout.show, Klout(""))
    def test_show_ShouldAcceptAListOrTuple(self):
        self.assertIsInstance(getattr(self.klout, "show")(["user"]), type({}))
        self.assertIsInstance(getattr(self.klout, "show")(("user",)), type({}))
    def test_show_raisesExceptionIfInputIsEmpty(self):
        self.assertRaises(Exception, self.klout.show, [])
        self.assertRaises(Exception, self.klout.show, ())
    def test_score_resultIsNotEmpty(self):
        self.assertNotEquals(self.klout.show(["user"]), {})
    """
        Topics method
    """
    def test_topics_exists(self):
        self.assertTrue(callable(getattr(self.klout, "topics")))
    def test_topics_ShourldRaiseAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.klout.topics, None)
        self.assertRaises(Exception, self.klout.topics, 1)
        self.assertRaises(Exception, self.klout.topics, "Score")
        self.assertRaises(Exception, self.klout.topics, Klout(""))
    def test_topics_ShouldAcceptAListOrTuple(self):
        self.assertIsInstance(getattr(self.klout, "topics")(["user"]), type({}))
    def test_topics_raisesExceptionIfInputIsEmpty(self):
        self.assertRaises(Exception, self.klout.topics, [])
        self.assertRaises(Exception, self.klout.topics, ())
    def test_topics_resultIsNotEmpty(self):
        self.assertNotEquals(self.klout.topics(["user"]), [])
    """
        InfluencerOf method
    """
    def test_influencerOf_exists(self):
        self.assertTrue(callable(getattr(self.klout, "influencerOf")))
    def test_influencerOf_ShourldRaiseAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.klout.influencerOf, None)
        self.assertRaises(Exception, self.klout.influencerOf, 1)
        self.assertRaises(Exception, self.klout.influencerOf, "Score")
        self.assertRaises(Exception, self.klout.influencerOf, Klout(""))
    def test_influencerOf_ShouldAcceptAListOrTuple(self):
        self.assertIsInstance(getattr(self.klout, "influencerOf")(["user"]), type({}))
    def test_influencerOf_raisesExceptionIfInputIsEmpty(self):
        self.assertRaises(Exception, self.klout.influencerOf, [])
        self.assertRaises(Exception, self.klout.influencerOf, ())
    def test_influencerOf_resultIsNotEmpty(self):
        self.assertNotEquals(self.klout.influencerOf(["user"]), [])
    """
        InfluencedBy method
    """
    def test_influencedBy_exists(self):
        self.assertTrue(callable(getattr(self.klout, "influencedBy")))
    def test_influencedBy_ShourldRaiseAnExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.klout.influencedBy, None)
        self.assertRaises(Exception, self.klout.influencedBy, 1)
        self.assertRaises(Exception, self.klout.influencedBy, "Score")
        self.assertRaises(Exception, self.klout.influencedBy, Klout(""))
    def test_influencedBy_ShouldAcceptAListOrTuple(self):
        self.assertIsInstance(getattr(self.klout, "influencedBy")(["user"]), type({}))
    def test_influencedBy_raisesExceptionIfInputIsEmpty(self):
        self.assertRaises(Exception, self.klout.influencedBy, [])
        self.assertRaises(Exception, self.klout.influencedBy, ())
    def test_influencedBy_resultIsNotEmpty(self):
        self.assertNotEquals(self.klout.influencedBy(["user"]), [])
