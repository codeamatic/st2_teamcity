from lib.action import TeamCityAction


class BuildJob(TeamCityAction):

    def run(self, build_config_id, branch_name=None):
        request = '''<build branchName="%s">
                            <buildType id="%s"/>
                            </build>''' % (branch_name, build_config_id)

        response = self._api_post('/buildQueue', request)
        return response
