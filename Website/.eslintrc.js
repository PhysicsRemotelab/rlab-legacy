module.exports = {
    parserOptions: {
      parser: 'babel-eslint'
    },
    extends: [
      'plugin:vue/recommended',
      'standard'
    ],
    plugins: [
      'vue'
    ],
    "rules":{
      "indent": "off",
      "vue/html-indent": "off",
      "vue/html-quotes": "off",
      "no-trailing-spaces": "off",
      "no-unused-vars": "off",
      "vue/singleline-html-element-content-newline": "off",
      "vue/html-self-closing": "off",
      "space-before-function-paren": ["warn", "never"],
      "vue/max-attributes-per-line": "off"
    }
}
