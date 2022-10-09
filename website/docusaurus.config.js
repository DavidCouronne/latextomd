const remarkMath = require("remark-math");
const rehypeKatex = require("rehype-katex");
const math = require('remark-math')
const katex = require('rehype-katex')

module.exports = {
  stylesheets: [
    {
      href: "https://cdn.jsdelivr.net/npm/katex@0.11.1/dist/katex.min.css",
      integrity:
        "sha384-zB1R0rpPzHqg7Kpt0Aljp8JPLqbXI3bhnPWROx27a9N0Ll6ZP/+DiW/UqRcLbRjq",
      crossorigin: "anonymous"
    }
  ],

  title: "latextomd",
  tagline: "latextomd Documentation",
  url: "https://latextomd.netlify.com/",
  baseUrl: "/",
  favicon: "img/favicon.ico",

  organizationName: "David Couronné", // Usually your GitHub org/user name.
  projectName: "latextomd", // Usually your repo name.

  themeConfig: {
    image: "img/open-graph.png",


    prism: {
      theme: require("prism-react-renderer/themes/nightOwl")
    },

    navbar: {
      title: "latextomd",
      logo: {
        alt: "My Site Logo",
        src: "img/android-chrome-512x512.png"
      },
      items: [
        { to: "docs/installation", label: "Docs", position: "left" },

        {
          href: "https://github.com/DavidCouronne/latextomd",
          label: "GitHub",
          position: "right"
        }
      ]
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Installation",
              to: "docs/installation"
            },
            {
              label: "Basic Examples",
              to: "docs/basic-examples"
            }
          ]
        },
        /* {
          title: "Community",
          items: [
            {
              label: "Stack Overflow",
              href: "https://stackoverflow.com/questions/tagged/docusaurus"
            },
            {
              label: "Discord",
              href: "https://discordapp.com/invite/docusaurus"
            }
          ]
        }, */
        {
          title: "Social",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/DavidCouronne"
            },
            {
              label: "Twitter",
              href: "https://twitter.com/nollan94"
            }
          ]
        }
      ],
      copyright: `Copyright © ${new Date().getFullYear()} David Couronné. Built with Docusaurus.`
    }
  },

  presets: [
    [
      "@docusaurus/preset-classic",
      {
        blog: false,
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl:
            "https://github.com/DavidCouronne/latextomd/edit/master/website/",
          admonitions: false,

          remarkPlugins: [math],
          rehypePlugins: [katex],
          showLastUpdateTime: true,


        },
        theme: {
          customCss: require.resolve("./src/css/custom.css")
        }
      }
    ]
  ]
};
