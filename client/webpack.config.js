const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
  entry: path.join(__dirname, 'src/javascript/main.js'),
  output: {
    publicPath: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin()
  ],
  devServer: {
    contentBase: path.join(__dirname, 'src/layouts'),
    port: 3000, 
    publicPath: 'http://localhost:3000/dist'
  }
}