from lib.action import TeamCityAction


class GetBuildQueue(TeamCityAction):

    def run(self):
        response = self._api_get('/buildQueue')
        return response
