<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gobblegoob/macgenerator">
    <img src="images/logo.png" alt="Logo" height="80">
  </a>

  <h3 align="center">Mac Generator</h3>

  <p align="center">
    Generate a list of MAC addresses in various formats.  Can also format as randomized macs in use by many mobile devices as well.
    <br />
    <a href="https://github.com/gobblegoob/macgenerator/issues">Report Bug</a>
    ·
    <a href="https://github.com/gobblegoob/macgenerator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I needed a big list of arbitrary mac addresses for testing purposes. 


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
<!--
### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```
-->

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gobblegoob/macgenerator.git
   ```
2. Install dependencies from requirements.txt
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
From your terminal/cli:
```sh
python macgenerate.py [-h] [-c COUNT] [-d DELIMITER] [-r]
```

<table>
  <tr>
    <td width = 300><b>Arguments</b></td><td width=500><b>Description</b></td>
  </tr>
  <tr><td>-h, --help</td><td>show this help message and exit</td></tr>
  <tr><td>-c COUNT, --count COUNT</td><td>How many MAC addresses to generate. Will print 10 if not specified</td></tr>
  <tr><td>-d DELIMITER, --delimiter DELIMITER</td><td> MAC Address delimiter. Will use None if not specified. Supported delimiters: ":", "-"</td></tr>
  <tr><td>-r, --randomized  </td><td>Add if you want randomized IP addresses</td></tr>
</table>


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/gobblegoob/macgenerator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you wish to contribute or have feature or usage suggestions, leave me a message.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/gobblegoob/gmacgenerator](https://github.com/gobblegoob/macgenerator)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


Thank yous

* [othneildrew Best README Template](https://github.com/gobblegoob/macgenerator)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/gobblegoob/macgenerator.svg?style=for-the-badge
[contributors-url]: https://github.com/gobblegoob/macgenerator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/gobblegoob/macgenerator.svg?style=for-the-badge
[forks-url]: https://github.com/gobblegoob/macgenerator/network/members
[stars-shield]: https://img.shields.io/github/stars/gobblegoob/macgenerator.svg?style=for-the-badge
[stars-url]: https://github.com/gobblegoob/macgenerator/stargazers
[issues-shield]: https://img.shields.io/github/issues/gobblegoob/macgenerator.svg?style=for-the-badge
[issues-url]: https://github.com/gobblegoob/macgenerator/issues
[license-shield]: https://img.shields.io/github/license/gobblegoob/macgenerator.svg?style=for-the-badge
[license-url]: https://github.com/gobblegoob/macgenerator/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/
[product-screenshot]: images/screenshot.png
