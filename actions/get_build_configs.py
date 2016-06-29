from lib.action import TeamCityAction


class GetBuildConfigs(TeamCityAction):

    def run(self,):
        response = self._api_get('/buildTypes')

        return response
