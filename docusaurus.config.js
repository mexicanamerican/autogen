// docusaurus.config.js

const { join } = require('path');

module.exports = {
  title: 'AutoGen Documentation',
  tagline: 'Enable Next-Gen Large Language Model Applications',
  url: 'https://autogen-docs.example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'microsoft',
  projectName: 'autogen',
  themeConfig: {
    navbar: {
      title: 'AutoGen',
      logo: {
        alt: 'AutoGen Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          to: 'docs/getting-started',
          activeBasePath: 'docs',
          label: 'Docs',
          position: 'left',
        },
        // Add more navigation items as needed
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: 'docs/getting-started',
            },
            // Add more documentation links as needed
          ],
        },
        // Add more footer links as needed
      ],
      logo: {
        alt: 'AutoGen Logo',
        src: 'img/logo.svg',
        href: 'https://autogen.example.com',
      },
    },
  },
  plugins: [
    // Add any required plugins here
  ],
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Add any additional documentation configuration as needed
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
  // Add any additional configuration as needed
};
