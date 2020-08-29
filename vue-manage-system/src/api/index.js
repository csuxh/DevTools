import request from '../utils/request';
// import Qs from 'qs';

export const fetchCMDB = query => {
  return request({
    url: '/cmdb/servers/',
    method: 'get',
    params: query
  });
};

export const queryCMDB = data => {
  return request({
    url: '/cmdb/servers/',
    method: 'get',
    params: data,
    header: {
      'Content-Type': 'application/json'  //如果写成contentType会报错
    }
  });
};

export const menueList = query => {
  return request({
    url: '/dashboard/menues/',
    method: 'get',
    params: query
  });
};


// 登录
export const loginAPI = data => {
  return request({
    url: '/login',
    method: 'post',
    data: data,
    header: {
      'Content-Type': 'application/json'  //如果写成contentType会报错
    }
  });
};

// 登出
export const logout = () => {
  return request({
    url: '/logout',
    method: 'get'
  });
};