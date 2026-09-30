# sphinx-mono

## About
All-in-one repository framework hosting an integrated code-base and Sphinx tree.

## Overview
This repository serves as a live, interactive reference demonstrating a unified mono-repo architecture. Instead of isolating software and documentation in separate repositories, this framework houses both components under a single roof to enable atomic commits and simplify CI pipelines.

## Features
* **Atomic Continuous Integration:** Every single commit is automatically validated by an internal GitHub Actions runner that tests the code syntax and docstring compilation simultaneously.
* **Cross-Domain Atomic Commits:** Enables simultaneous tracking of source code adjustments and document updates under a single Git hash, preventing out-of-sync states.
* **Native Path Resolution:** The configuration uses simple relative parent look-ups to discover the application modules natively without complex path environmental requirements.

## Layout
```text
sphinx-mono/                      # Combined repository (unified monorepo).
├── .github/                      # Hidden GitHub directory
│   └── workflows/                # Directory for repository workflows
│       └── ci.yml                # Flat internal CI pipeline
├── codebase/                     # Directory for a demonstration code-base
│   └── example.py                # Python module with reST docstrings
├── sphinx/                       # Directory for Sphinx
│   ├── resources/                # Directory for engine assets and data drawers
│   │   ├── images/               # Directory for images and visual assets
│   │   ├── rst/                  # Directory for all other reST files
│   │   │   ├── installation.rst  # Documentation
│   │   │   └── usage.rst         # Documentation
│   │   ├── scripts/              # Directory for scripts (build, cleanup, linting, or automation)
│   │   ├── static/               # Directory for custom CSS or fonts        
│   │   └── templates/            # Directory for custom HTML structural layouts
│   ├── conf.py                   # Sphinx configuration matrix
│   └── index.rst                 # Sphinx documentation master layout file (entry-page/gatekeeper)
├── .gitignore                    # Defensive tracking shield (ignores build artifacts)
├── LICENSE                       # License
└── README.md                     # Main document for the repository
```

---

*Feel free to explore the files and adapt this framework to your project.*
