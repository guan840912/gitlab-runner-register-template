#!/bin/bash

# EXAMPLE
# ./curl_register.sh $GITLAB_RUNNER_TOKEN runner,curl,sh

GITLAB_RUNNER_TOKEN=$1
TAGS=$2

#curl --request POST "https://gitlab.com/api/v4/runners" --form "token=<GITLAB_RUNNER_TOKEN>" --form "description=curl_register_runner" --form "tag_list=runner,curl"
curl --request POST "https://gitlab.com/api/v4/runners" --form "token=$GITLAB_RUNNER_TOKEN" --form "description=curl_register_runner" --form "tag_list=$TAGS"
