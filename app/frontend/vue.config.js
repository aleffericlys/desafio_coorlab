const webpack = require('webpack');

module.exports = {
	transpileDependencies: [
	  'vue-echarts',
	  'resize-detector'
	],
	configureWebpack: {
	  plugins: [
		new webpack.DefinePlugin({
		  __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: true
		})
	  ]
	}
  }