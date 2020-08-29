module.exports = {
  publicPath: './',
  assetsDir: 'static',
  productionSourceMap: false,
  devServer: {
    proxy: 'http://10.25.38.42:8888/'
  }
  // devServer: {
  //   // headers: {
  //   //   'Access-Control-Allow-Origin': '*',
  //   //   'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
  //   // },
  //   proxyTable: {
  //     '/api': {
  //       target: 'http://10.25.38.42:8888/api/',
  //       changeOrigin: true,
  //       pathRewrite: {
  //         '^/api': ''
  //       }
  //     }
  //   }
  // }
}


// module.exports = {
//   dev: {
//     // proxyTable: proxyConfig.proxyList, // 无效，不使用，20190422
//     proxyTable: {
//       '/api': {
//         target: 'http://192.168.1.6:8888',//后端接口地址
//         changeOrigin: true,//是否允许跨越
//         pathRewrite: {
//           '^/api': '/api',//重写,
//         }
//       }
//     },
//   }
// };