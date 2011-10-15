import unittest 
from pythonklout import KloutService, TestKloutService

class KloutServiceTestCase(unittest.TestCase):
      def setUp(self):
        self.service = KloutService("key")
      def tearDown(self):
        self.service = None
      def test_makeCall_exists(self):
        self.assertTrue(callable(getattr(self.service, "makeCall")))
      def test_makeCall_raisesAnException(self):
        self.assertRaises(Exception, self.service.makeCall, *("url", "query"))
      def test_getCallUrl_exists(self):
        self.assertTrue(callable(getattr(self.service, "getCallUrl")))
      def test_getCallUrl_returnsTheScoreUrl(self):
        scoreUrl = "/1/klout.json"
        self.assertEquals(scoreUrl, self.service.getCallUrl("score"))
      def test_getCallUrl_returnsUserUrl(self):
        userUrl = "/1/users/show.json"
        self.assertEquals(userUrl, self.service.getCallUrl("user"))
      def test_getCallUrl_returnsTopicsUrl(self):
        topicUrl = "/1/users/topics.json"
        self.assertEquals(topicUrl, self.service.getCallUrl("topics"))
      def test_getCallUrl_returnsInfluencedByUrl(self):
        influencedByUrl = "/1/soi/influenced_by.json"
        self.assertEquals(influencedByUrl, self.service.getCallUrl("influencedBy"))
      def test_getCallUrl_returnsInfluencerOfUrl(self):
        influencerOfUrl = "/1/soi/influencer_of.json"
        self.assertEquals(influencerOfUrl, self.service.getCallUrl("influencerOf"))
      def test_getCallUrl_raisesAnException(self):
        self.assertRaises(Exception, self.service.getCallUrl, "NotExist")
      """
         _remove_empty_params method
      """
      def  test_remove_empty_params_exists(self):
        self.assertTrue(callable(getattr(self.service, "_remove_empty_params")))
      def  test_remove_empty_params_returnsADictionary(self):
        self.assertIsInstance(self.service._remove_empty_params({}), type({}))
      def test_remove_empty_params_raisesExceptionWithWrongInput(self):
        self.assertRaises(Exception, self.service._remove_empty_params, "wrong")
        self.assertRaises(Exception, self.service._remove_empty_params, 1)
        self.assertRaises(Exception, self.service._remove_empty_params, ["wrong"])
        self.assertRaises(Exception, self.service._remove_empty_params, ("wrong",))
      def test_remove_empty_params_removesTheEmptyParams(self):
        query = {"first":1, "second":2, "third":None}
        expectedQuery = {"first":1, "second":2}
        self.assertEquals(expectedQuery, self.service._remove_empty_params(query))

class TestKloutServiceTestCase(unittest.TestCase):
      def setUp(self):
        self.service = TestKloutService("key")
        self.userResponse = self.service.makeCall("user", {})
        self.scoreResponse = self.service.makeCall("score", {})
        self.topicsResponse = self.service.makeCall("topics", {})
        self.influencedByResponse = self.service.makeCall("influencedBy", {})
        self.influencerOfResponse = self.service.makeCall("influencerOf", {})
        self.historyResponse = self.service.makeCall("history", {})
      def tearDown(self):
        self.service = None
      # MakeCall("score", ...
      def test_makeCall_WithScoreAsCallName_returnsAnArray(self):
        self.assertIsInstance(self.service.makeCall("score", {}), type({}))
      def test_makeCall_WithScoreAsCallName(self):
        expectedResult = {"users":[{"twitter_screen_name":"user1", "kscore":23.02}]}
        actualResult = self.service.makeCall("score", {"users":["user1"]})
        self.assertEquals(expectedResult, actualResult)
      def test_makeCall_WithScoreAsCallName_hasUsersKey(self):
        actual = self.scoreResponse.get("users")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, type([]))
      def test_makeCall_WithScoreAsCallName_ContainsAtLeastOneDictionary(self):
        actual = self.scoreResponse.get("users")[0]
        self.assertIsInstance(actual, type({}))
      def test_makeCall_ScoreCallName_containsTwitterScreenNameProperty(self):
        users = self.scoreResponse.get("users")[0]
        actual = users.get("twitter_screen_name")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_ScoreCallName_containsKScoreProperty(self):
        users = self.scoreResponse.get("users")[0]
        actual = users.get("kscore")
        self.assertIsInstance(actual, type(22.22))
        self.assertIsNotNone(actual) 
      # MakeCall("topics", ...
      def test_makeCall_WithTopicsAsCallName_returnsAnArray(self):
        self.assertIsInstance(self.service.makeCall("topics", {}), type({}))
      def test_makeCall_WithTopicsAsCallName(self):
        expectedResult = {"users":[{"twitter_screen_name":"user1", "topics":["python"]}]}
        actualResult = self.service.makeCall("topics", {"users":["user1"]})
        self.assertEquals(expectedResult, actualResult)
      def test_makeCall_WithTopicsAsCallName_hasUsersKey(self):
        actual = self.topicsResponse.get("users")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, type([]))
      def test_makeCall_WithTopicsAsCallName_ContainsAtLeastOneDictionary(self):
        actual = self.topicsResponse.get("users")[0]
        self.assertIsInstance(actual, type({}))
      def test_makeCall_TopicsCallName_containsTwitterScreenNameProperty(self):
        users = self.topicsResponse.get("users")[0]
        actual = users.get("twitter_screen_name")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_TopicsCallName_containsTopicsProperty(self):
        users = self.topicsResponse.get("users")[0]
        actual = users.get("topics")
        self.assertIsInstance(actual, type([]))
        self.assertIsNotNone(actual) 
      # MakeCall("influencedBy", ...
      def test_makeCall_WithInfluencedByAsCallName_returnsAnArray(self):
        self.assertIsInstance(self.service.makeCall("influencedBy", {}), type({}))
      def test_makeCall_WithInfluencedByAsCallName(self):
        expectedResult = {"users":[{"twitter_screen_name":"user1", "influencers":[{
"twitter_screen_name":"user2", "kscore":10.00}]}]}
        actualResult = self.service.makeCall("influencedBy", {"users":["user1"]})
        self.assertEquals(expectedResult, actualResult)
      def test_makeCall_WithInfluencedByAsCallName_hasUsersKey(self):
        actual = self.influencedByResponse.get("users")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, type([]))
      def test_makeCall_WithInfluencedByAsCallName_ContainsAtLeastOneDictionary(self):
        actual = self.influencedByResponse.get("users")[0]
        self.assertIsInstance(actual, type({}))
      def test_makeCall_InfluencedByCallName_containsTwitterScreenNameProperty(self):
        users = self.influencedByResponse.get("users")[0]
        actual = users.get("twitter_screen_name")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_influencedByCallName_containsInfluencersProperty(self):
        users = self.influencedByResponse.get("users")[0]
        actual = users.get("influencers")
        self.assertIsInstance(actual, type([]))
        self.assertIsNotNone(actual) 
      # MakeCall("influencerOf", ...
      def test_makeCall_WithInfluencerOfAsCallName_returnsAnArray(self):
        self.assertIsInstance(self.service.makeCall("influencerOf", {}), type({}))
      def test_makeCall_WithInfluencerOfAsCallName(self):
        expectedResult = {"users":[{"twitter_screen_name":"user1", "influencers":[{
"twitter_screen_name":"user2", "kscore":10.00}]}]}
        actualResult = self.service.makeCall("influencerOf", {"users":["user1"]})
        self.assertEquals(expectedResult, actualResult)
      def test_makeCall_WithInfluencerOfAsCallName_hasUsersKey(self):
        actual = self.influencedByResponse.get("users")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, type([]))
      def test_makeCall_WithInfluencerOfAsCallName_ContainsAtLeastOneDictionary(self):
        actual = self.influencedByResponse.get("users")[0]
        self.assertIsInstance(actual, type({}))
      def test_makeCall_InfluencerOfCallName_containsTwitterScreenNameProperty(self):
        users = self.influencerOfResponse.get("users")[0]
        actual = users.get("twitter_screen_name")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_influencerOfCallName_containsInfluencersProperty(self):
        users = self.influencerOfResponse.get("users")[0]
        actual = users.get("influencers")
        self.assertIsInstance(actual, type([]))
      # MakeCall("user"...
      def test_makeCall_WithUserAsCallName_returnsADictionary(self):
        self.assertIsInstance(self.service.makeCall("user", {}), type({}))
      def test_makeCall_WithUserAsCallName_hasUsersKey(self):
        actual = self.userResponse.get("users")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, type([]))
      def test_makeCall_WithUserAsCallName_ContainsAtLeastOneDictionary(self):
        actual = self.userResponse.get("users")[0]
        self.assertIsInstance(actual, type({}))
      def test_makeCall_UserCallName_containsTwitterIdProperty(self):
        users = self.userResponse.get("users")[0]
        actual = users.get("twitter_id")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_containsTwitterIdProperty(self):
        users = self.userResponse.get("users")[0]
        actual = users.get("twitter_screen_name")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_containsScoreProperty(self):
        users = self.userResponse.get("users")[0]
        actual = users.get("score")
        self.assertIsInstance(actual, type({}))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsKScoreProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("kscore")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsSlopeProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("slope")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsDescriptionProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("description")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsKClassIdProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("kclass_id")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsKClassProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("kclass")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsKClassDescriptionProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("kclass_description")
        self.assertIsInstance(actual, type(""))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsNetworkScoreProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("network_score")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsAmplificationScoreProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("amplification_score")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsDelta1DayProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("delta_1day")
        self.assertIsInstance(actual, type(0.5))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsDelta5DayProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("delta_5day")
        self.assertIsInstance(actual, type(0.5))
        self.assertIsNotNone(actual) 
      def test_makeCall_UserCallName_scoreContainsTrueReachProperty(self):
        users = self.userResponse.get("users")[0]
        score = users.get("score")
        actual = score.get("true_reach")
        self.assertIsInstance(actual, type(1))
        self.assertIsNotNone(actual) 
      # MakeCall("history"...
      def test_makeCall_WithHistoryAsCallName_returnsADictionary(self):
        self.assertIsInstance(self.service.makeCall("history", {}), type({}))
      def test_makeCall_HistoryCallName_containsDatesProperty(self):
        key = "dates"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsKlout_ScoreProperty(self):
        key = "klout_score"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsAmplificationProperty(self):
        key = "amplification"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsRetweetsProperty(self):
        key = "retweets"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsMentionsProperty(self):
        key = "mentions"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsNetworkProperty(self):
        key = "network"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsFollowers_FollowingProperty(self):
        key = "followers_following"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsFollowers_CountProperty(self):
        key = "followers_count"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsMentionersProperty(self):
        key = "mentioners"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsRetweetersProperty(self):
        key = "retweeters"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsTrueReachProperty(self):
        key = "true_reach"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
      def test_makeCall_HistoryCallName_containsInOutProperty(self):
        key = "in_out"
        self.assertTrue(key in self.historyResponse)
        self.assertIsInstance(self.historyResponse.get(key), type([]))
        
