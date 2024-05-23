module.exports = {
    parserOptions: {
      sourceType: 'module',
      ecmaVersion: 2019, // Adjust this based on your project's JS version
    },
    env: {
      browser: true,
      es6: true,
      // Add other relevant environments (e.g., node)
    },
    extends: ['eslint:recommended'],
    plugins: ['svelte'],
    overrides: [
      {
        files: ['*.svelte'],
        processor: 'svelte/svelte',
        rules: {
          // Add specific linting rules here
        },
      },
    ],
  };
  