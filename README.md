<h1 align="center">JShoter</h1>
<h3 align="center">Extracts only JavaScript files from the given URL</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/JShoter.svg)](https://GitHub.com/DevanshRaghav75/JShoter/releases/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/JShoter.svg)](https://github.com/DevanshRaghav75/JShoter/blob/master/LICENSE.md)

## What is JShoter?

**JShoter** extracts only **JavaScript** files from the given URL, **for ex.** https://example.com/core/web_pack/js/1234567_main_.js

## Installation
```
$ git clone https://github.com/DevanshRaghav75/JShoter.git
$ cd JShoter
$ python3 setup.py install
$ jshoter -h 
```
## Usage

### Finding JS files

Command:
```
$ jshoter https://yahoo.com
```

Output:
```
https://s.yimg.com/nn/lib/metro/g/sda/sda_modern_0.0.41.js
https://s.yimg.com/aaq/fp/js/tdv2-wafer-stream.custom.e99888b4e815d9aed00adc5413239bcd.js
https://s.yimg.com/aaq/fp/js/tdv2-wafer-utils.customErrorHandler.7eca54bd34107b477282eb7a7d1b06d3.js
https://s.yimg.com/aaq/fp/js/tdv2-wafer-user-dialog.custom.6696ae78fb98b0026e813d04c0206fd3.js
https://s.yimg.com/aaq/hc/homepage-pwa-defer-1.1.4.js
https://s.yimg.com/aaq/fp/js/react-wafer-subscription.custom.default.6ba6c32ce318be3e3ca8a6d5b57b17cf.js
https://s.yimg.com/aaq/yc/js/iframe-1.0.26.js
https://s.yimg.com/aaq/cmp/version/4.1.3/cmp.js
https://s.yimg.com/rq/darla/4-6-0/js/g-r-min.js
https://edge-mcdn.secure.yahoo.com/ybar/cerebro_min.js
https://s.yimg.com/ss/rapid-3.53.28.js
https://s.yimg.com/aaq/wf/wf-core-1.46.14.js
https://s.yimg.com/aaq/hp-viewer/desktop_1.9.285.js
https://s.yimg.com/aaq/wf/wf-beacon-1.3.2.js
https://s.yimg.com/aaq/wf/wf-fetch-1.17.6.js
https://s.yimg.com/aaq/wf/wf-toggle-1.14.2.js
https://s.yimg.com/aaq/wf/wf-darla-1.0.26.js
https://s.yimg.com/aaq/wf/wf-bind-1.1.2.js
https://s.yimg.com/aaq/wf/wf-text-1.1.3.js
https://s.yimg.com/aaq/wf/wf-image-1.1.8.js
https://s.yimg.com/aaq/wf/wf-caas-1.14.13.js
https://s.yimg.com/aaq/wf/wf-video-2.16.2.js
https://s.yimg.com/aaq/wf/wf-countdown-1.2.5.js
https://s.yimg.com/aaq/wf/wf-scrollview-2.14.2.js
https://s.yimg.com/aaq/wf/wf-tooltip-1.1.2.js
https://s.yimg.com/aaq/wf/wf-form-1.28.12.js
https://s.yimg.com/aaq/wf/wf-template-1.4.1.js
https://s.yimg.com/aaq/wf/wf-action-1.2.5.js
https://s.yimg.com/aaq/wf/wf-sticky-1.0.9.js
https://s.yimg.com/aaq/wf/wf-rapid-1.5.2.js
https://s.yimg.com/aaq/wf/wf-tabs-1.11.4.js
https://s.yimg.com/aaq/wf/wf-autocomplete-1.24.9.js
https://s.yimg.com/aaq/wf/wf-geolocation-1.2.10.js
https://s.yimg.com/os/yaft/yaft-0.3.27.min.js
https://s.yimg.com/os/yaft/yaft-plugin-aftnoad-0.1.5.min.js
/lib/metro/g/myy/advertisement_0.0.20.js

[+] Total JS files found: 36

```
