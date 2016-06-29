from lib.action import TeamCityAction


class BuildJob(TeamCityAction):

    def run(self, build_config_id, vcs_branch_name="develop"):
        request = '''<build branchName="%s">
                            <buildType id="%s"/>
                            </build>''' % (vcs_branch_name, build_config_id)

        response = self._api_post('/buildQueue', request)
        return response
