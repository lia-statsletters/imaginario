import urllib
import facebook
import requests


# facebook.VALID_SEARCH_TYPES

class imaginariopage():
    def __init__(self, startinfo):
        self.graph = self.authentication(startinfo)

    def authentication(self, startinfo):
        app_token = facebook.GraphAPI().get_app_access_token(startinfo['appid'],
                                                             startinfo['appsecret'],
                                                             True)
        firstg = facebook.GraphAPI(access_token=app_token, version='2.8')
        resp = firstg.get_object('me')
        for page in resp['data']:
            if page['id'] == startinfo['pageid']:
                return facebook.GraphAPI(page['access_token'])

    def run(self):
        # Lets see if we can post hi.

        try:
            self.graph.put_wall_post('blip blip hi!')
        except Exception as bummer:
            print('oh no! cant post because {}'.format(bummer.args))


if __name__ == "__main__":
    # imaginario sandbox ID: 1781737371858167
    app = imaginariopage({'appid': '985317034950101',
                          'appsecret': '02bc46c89fa136dafe54a1481bc701ca',
                          'pageid': '1781737371858167'})
    app.run()
