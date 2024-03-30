<p align="center">
<img src="https://i.imgur.com/an4hEwO.png" alt="Logo" width="250" height="250"/>
</p>
<h1 align="center">Formative</h1>
<p align="center">
<b>Form·ative</b> / <i>noun</i><br>
Serving to form something
</p>

---

<p align="center">
<a href="https://opensource.org/licenses/MIT"><img alt="GitHub License" src="https://img.shields.io/github/license/JamesFlanders/formative"></a>
<a href="https://github.com/JamesFlanders/formative/releases"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/JamesFlanders/formative"></a>
<a href="https://github.com/JamesFlanders/formative/actions/workflows/build_and_release_frontend.yml"><img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/JamesFlanders/formative/build_and_release_frontend.yml"></a>
<a href="https://paypal.me/JensCaenen"><img alt="Static Badge" src="https://img.shields.io/badge/Donate-PayPal-blue"></a>
</p>

---

# :question: What is Formative ?

Formative is an out-of-the-box frontend for backend services that do not have a frontend on their own. Some examples of
use-cases for Formative:

- You have a cool API, but do not have the frontend skills to provide an interface for the users of your API.
- You want to manage information in a database without directly querying through SQL-queries.

<sup>Disclaimer: These above-mentioned use-cases might not be supported yet as Formative is still in an early (alpha)
phase.</sup>

# :closed_book: Documentation

In the future, more documentation will be provided in a GitHub wiki. As of now, you can execute the following Docker run
command:

```shell
docker run --name formative-frontend -t \
      -p 8080:80 \
      -v volume_formative_images:/usr/share/nginx/html/images \
      -v volume_formative_config:/usr/share/nginx/html/config \
      --restart unless-stopped \
      -d ghcr.io/jamesflanders/formative-frontend:latest
```

<sup>Note: Only amd64 and arm64 architectures are currently supported.</sup>

This will start Formative and serve it on http://localhost:8080.

# :calendar: Roadmap

## Stages of development

### :a: Alpha

**The MVP Phase**\
Within the alpha of Formative, it is the goal to achieve a minimal viable product (MVP) that has a rich set of basic
features that makes Formative useful for many use-cases.

#### Minimal conditions for Beta

- [ ] Add additional action types (e.g 'SQL')
- [ ] Add additional field types (e.g. 'Email', 'Radio', 'Range selector',...)
- [ ] Add easy custom theme options
- [ ] Add (sufficient) documentation on the usage of Formative
- [ ] Add usage of users within Formative
- [ ] Add Role Base Access Control (permissions) within Formative
- [ ] Provide an easy-to-use form editor for it within Formative.
- [ ] Add architecture support for arm/v6 and arm/v7 (Raspberry Pi)

### :b: Beta

**The Stabilisation Phase**\
Within the beta of Formative, it is the goal to achieve a stable platform that can be safely used in even '
enterprise' environments.

#### Minimal conditions for Release

To be defined once the Alpha phase has surpassed.

### :registered: Release

**The Release Phase**\
Within this release phase, all mentioned goals in the other 2 phases have been completed, and the idea is now to keep
the Formative 'fresh' with features and regular updates and patches.

# :handshake: Contributing

Contact me directly on GitHub if you are interested in contributing. No proper process for contributors has been
developed yet.

# :copyright: License

[MIT License](https://opensource.org/licenses/MIT)\
Copyright (c) 2024 [James Flanders](https://github.com/JamesFlanders)

