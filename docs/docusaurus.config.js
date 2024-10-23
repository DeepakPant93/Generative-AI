import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AskDocsGPT',
  tagline: 'Your Documentation Assistant',
  favicon: 'img/favicon.ico',

  url: 'https://DeepakPant93.github.io',
  baseUrl: '/Generative-AI/',

  organizationName: 'DeepakPant93',
  projectName: 'Generative-AI',

  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'ignore',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
      colorMode: {
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      image: 'img/docusaurus-social-card.jpg',
      navbar: {
        title: 'AskDocsGPT',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'https://github.com/DeepakPant93/Generative-AI',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} Deepak, Inc. Built with Docusaurus.`,
      },
//      algolia: {
//        appId: 'VAU016LAWS',
//        apiKey: '6c01842d6a88772ed2236b9c85806441', // Search-only API key
//        indexName: 'askdocsgpt',
//        contextualSearch: true,
//        searchParameters: {
//          facetFilters: ['language:en'],
//        },
//        // Optional: Replace with 'false' if you don't want the search page
//        searchPagePath: 'search',
//      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),

  markdown: {
    mermaid: true,
  },

  themes: [
    '@docusaurus/theme-mermaid',
//    '@docusaurus/theme-search-algolia'
  ],
};

export default config;