import axios from 'axios';

axios.defaults.withCredentials = true;
const service = axios.create({
  // process.env.NODE_ENV === 'development' 来判断是否开发环境
  baseURL: 'http://127.0.0.1:8888/api',
  timeout: 9000,
});

service.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    console.log(config);
    console.log(error);
    return Promise.reject();
  }
);

service.interceptors.response.use(
  response => {
    if (response.status === 200) {
      return response.data;
    } else {
      Promise.reject();
    }
  },
  error => {
    console.log(error);
    return Promise.reject();
  }
);

export default service;
