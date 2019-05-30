'use strict'
const webpack = require('webpack')
const { VueLoaderPlugin } = require('vue-loader')
const CopyWebpackPlugin = require('copy-webpack-plugin')
var path = require('path')

module.exports = {
  mode: 'production',
  optimization: {
    splitChunks: {
        cacheGroups: {
            commons: {
                test: /[\\/]node_modules[\\/]/,
                name: 'vendor',
                chunks: 'all'
            }
        }
    }
  },
  entry: [
    './src/index.js'
  ],
  output: {
    path: path.resolve(__dirname, './dist'),
    publicPath: '/dist/',
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|vue)$/,
        use: [{
          loader: 'eslint-loader',
          options: {
            emitWarning: true
          }
        }],
        enforce: 'pre'
      },
      {
        test: /\.vue$/,
        use: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.js$/,
        use: 'babel-loader'
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  plugins: [
    new VueLoaderPlugin(),
    new CopyWebpackPlugin([ { from: 'public/img', to: 'img' } ])
  ]
}
