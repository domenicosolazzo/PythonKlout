__author__ = "Domenico Solazzo"
__version__ = "0.1"

RESPONSE_CODES = {
        200: "OK: Success",
        202: "Accepted: The request was accepted and the user was queued for processing",
        401: "Not Authorized: either you need to provide authentication credentials, or the credentials provided aren't valid.",
        403: "Bad Request: Your request is invalid and we'll return and error message that tells you why. This is the status code if you have exceeded the rate limit.",
        404: "Not Found: either you are requesting an invalid URI or the resource in question doesn't exist.",
        500: "Internal Server Error: we did something wrong.",
        502: "Bad Gateway: returned if Klout is down or being upgraded.",
        503: "Service Unavailable: the Klout servers are up, but are overloaded with requests. Try again later."
}
class KloutError( Exception ):
    def __init__(self, code=0, msg=''):
        super(KloutError, self).__init__()
        self.code = code
        self.msg = msg
    def __str__(self):
        return repr(self)
    def __repr__(self):
        return "%i: %s" % (self.code, self.msg)
 
class Klout( object ):
    def __init__(self, key, serviceType="service"):
        self._apiKey = key
        self.__service = self.__getProxyFactory(serviceType)

    def __getProxyFactory(self, serviceType):
        service = None
        if serviceType == "test":
            service = TestKloutService(serviceType)
        else:
            service = KloutService(self._apiKey)
        self.__service = service
        return self.__service
        
    def score(self, users):
        """
            Retrieve a Klout score
            @param: users - List of usernames
            @return: A list of tuples in the form (username, klout_score)
        """
        if not users:
            raise KloutError(0, "No Users")
        if not isinstance(users, (list, tuple)):
            raise KloutError(0, "Wrong input.")
        users = ",".join(users)
        query = {"users": users}
        result = self.__service.makeCall("score", query)
        
        return result
    def show(self, users):
        """
            Retrieve a user object
            @param: users - List of usernames
            @return: A dictionary with the returned data
        """
        if not users:
            raise KloutError(0, "No Users.")
        if not isinstance(users, (list, tuple)):
            raise KloutError(0, "Wrong input.")
        users = ",".join(users)
        query = {"users":users}
        result = self.__service.makeCall("user", query)
        return result
    def topics(self, users):
        """
            Returns the top 3 topics objects
            @param: users - A list of usernames
            @return: A list of dicts in the form [{username:['topic1, topic2, topic3]..}
        """
        if not users:
            raise Exception("Input is empty")
        if not isinstance(users, (list, tuple)):
            raise Exception("Not Implemented Yet")
        users = ",".join(users)
        query = {"users":users}
        result = self.__service.makeCall("topics", query)
        return result
    def influencerOf(self, users):
        """
            Returns up to 5 user score pairs for user that are influencer for the given user
            @param: users - A list of usernames
            @return: A list of dicts in the form [{username:[(username, score),..}
        """
        if not users:
            raise Exception("Input is empty")
        if not isinstance(users, (list, tuple)):
            raise Exception("Not Implemented Yet")
        users = ",".join(users)
        query = {"users":users}
        result = self.__service.makeCall("influencerOf", query)
        return result
    def influencedBy(self, users):
        """
            Returns up to 5 user score pairs for user that are influenced by the given user
            @param: users - A list of usernames
            @return: A list of dicts in the form [{username:[(username, score),..}
        """
        if not users:
            raise Exception("Input is empty")
        if not isinstance(users, (list, tuple)):
            raise Exception("Not Implemented Yet")
        users = ",".join(users)
        query = {"users":users}
        result = self.__service.makeCall("influencedBy", query)
        return result

class KloutService(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.VERSION_API = "/1/"
        self.API_URL = "api.klout.com"
       
    def getCallUrl(self, callName):
        servicePath = ""
        if callName == "score":
            servicePath = "klout.json"
        elif callName == "user":
            servicePath = "users/show.json"
        elif callName == "topics":
            servicePath = "users/topics.json"
        elif callName == "influencedBy":
            servicePath = "soi/influenced_by.json"
        elif callName == "influencerOf":
            servicePath = "soi/influencer_of.json"
        else:
            raise Exception("Url not available")
        return self.VERSION_API + servicePath
    
    def _remove_empty_params(self, query):
        if not isinstance(query, type({})):
            raise Exception("Wrong query in input")
        returnedQuery = {}
        for key in query:
            if not query[key] == None:
                returnedQuery[key] = query[key]
        return returnedQuery

    def makeCall(self, callName, query):
        import urllib, httplib, json
        url = self.getCallUrl(callName)
        
        query = self._remove_empty_params(query)
        
        if 'key' not in query:
            query["key"] = self.apiKey
        
        queryStr = urllib.urlencode(query)
        
        if len(query) > 0:
            if url.find("?") == -1:
                url = url + "?" + queryStr
            else:
                url = url + "&" + queryStr
        try:
            conn = httplib.HTTPConnection(self.API_URL)
            conn.request('GET', url)
            response = conn.getresponse()
            data = response.read()
            data = json.loads(data)
        except httplib.HTTPException as err:
            msg = err.read() or RESPONSE_CODES.get(err.code, err.message)
            raise KloutError(err.code, msg)
        except ValueError:
            msg = "Invalid data: %s" % data
            raise KloutError(0, msg)
        return data
class TestKloutService(KloutService):
    def makeCall(self, callName, query):
        if callName == "score":
            return {"users":[{"twitter_screen_name":"user1","kscore":23.02}]}
        elif callName == "user":
            return {"users":[{
                "twitter_id": "111111",
                "twitter_screen_name":"name",
                "score":{
                    "kscore":10,
                    "slope":1,
                    "description":"description",
                    "kclass_id":1,
                    "kclass":"Socializer",
                    "kclass_description":"kclass description",
                    "network_score":22,
                    "amplification_score":18,
                    "true_reach": 10,
                    "delta_1day": 0.2,
                    "delta_5day": 0.4
                }
            }]}
        elif callName == "topics":
            return {"users":[{"twitter_screen_name":"user1", "topics":["python"]}]}
        elif callName == "influencedBy":
            return {"users":[
                                {
                                "twitter_screen_name":"user1", 
                                "influencers":[{"twitter_screen_name":"user2",
                                                "kscore":10.00
                                                }]
                                }
                            ]
                    }
        else: 
            return {"users":[
                                {
                                "twitter_screen_name":"user1", 
                                "influencers":[{"twitter_screen_name":"user2",
                                                "kscore":10.00
                                                }]
                                }
                            ]
                    }
   
