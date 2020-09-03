const axios = require('axios');

const url = 'https://gitlab.com/api/v4/runners'

const params = {
  description: 'typescript_register_runner',
  tag_list: 'typescript, axios',
  token: '<GITLAB_RUNNER_TOKEN>'}
  
axios.post(url, params).then(
  res => {
    console.log(res.data);
  }
)
