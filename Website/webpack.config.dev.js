'use strict'
const webpack = require('webpack')
const { VueLoaderPlugin } = require('vue-loader')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CopyWebpackPlugin = require('copy-webpack-plugin')

module.exports = {
  mode: 'development',
  entry: [
    './src/index.js'
  ],
  output: {
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
  devServer: {
    port: 80,
    host: '127.0.0.1',
    historyApiFallback: true,
    noInfo: true,
    hot: true,
    watchOptions: {
      poll: true
    }
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'public/index.html',
      inject: true
    }),
    new VueLoaderPlugin(),
    new CopyWebpackPlugin([ { from: 'public/img', to: 'img' } ])
  ]
}
