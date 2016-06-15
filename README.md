# TeamCity Integration Pack

This package creates a basic integration with TeamCity

## Configuration

* `url` - FQDN to TeamCity Server (e.x.: http://teamcity.example.com)
* `username` - (optional) TeamCity Username
* `password` - (optional) TeamCity Password
* `version` - (optional) Version of API/Teamcity.  Defaults to latest

## Actions

### Build Job
Initiates a job build within TeamCity

`build_job`

### List Build Configurations
Lists all TeamCity build configurations

`list_build_configs`

### List Running Jobs
Lists all currently running TeamCity jobs

`list_running_jobs`

## Rules

To trigger events from TeamCity, use TeamCity to send a webhook to
StackStorm.