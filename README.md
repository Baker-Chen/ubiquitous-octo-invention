<a href="https://www.synopsys.com/zh-tw/taiwan/university-program/iot-initiative/2021-arc-aiot-design-contest.html
" target="_blank"><img src="https://user-images.githubusercontent.com/85024328/120073598-9e337a80-c0cb-11eb-91b6-afecf940a960.png" 
alt="Link is failed!" width="600" border="10" /></a>


# [2021 Synopsys ARC AIoT Design Contest](https://www.synopsys.com/zh-tw/taiwan/university-program/iot-initiative/2021-arc-aiot-design-contest.html)
# NCHU WE-I Goose．Smith  <img src="https://i.imgur.com/fzbaowW.png" width="60">

### Smart elevator based on edge computing architecture combined with gesture recognition 
[![Build Status](https://travis-ci.org/SpiderLabs/ModSecurity-apache.svg?branch=master)](https://travis-ci.org/SpiderLabs/ModSecurity-apache)

## Content
* <a href="#Introduction">Introduction</a>
* <a href="#implementaion">Implementation</a>
* <a href="#power-optimization">Power Optimization</a>
* <a href="#Innovation--Difficulties">Innovation & Difficulties</a>
    * <a href="#Innovation">Innovation</a>
    * <a href="#Difficulties">Difficulties</a>
* <a href="#demo-Video">Demo Video</a>
* <a href="#system-architecture">System architecture</a>
* <a href="#physical-Design">Physical Design</a>
* <a href="#flow-chart">Flow Chart</a>
* <a href="#tools">Tools</a>
* <a href="#required-hardware">Required Hardware</a>
* <a href="#required-software">Required Software</a>
* <a href="#user-guide">User guide</a>
* <a href="#elevator">Elevator</a>




## Introduction
In the post pandemic era, zero-contact technology has become a trend. Among them, elevators play a significant role in spreading the virus due to the space in elevators are commonly small, closed and crowded. It is easy to be infected because people frequently interact with the elevator button panel and talk to another person in the same elevator. So we want to achieve a smart elevator button panel that can recognize the specific gestures and an always-on system through the benefits of Himax WE-I Plus ultra-low power consumption and AI acceleration. Reduce operation complexity and overall power consumption through a distributed computing architecture of edge computing.

This project combines the advantage of Himax WE-I Plus (ultra low power AI acceleration embedded ASIC) and NVIDIA Jetson Nano. We use cygwin to transfer the pretrained model into Tensorflow Lite’s form, and detect the hand movement through Himax WE-I Plus. After the process of the gesture recognition on NVIDIA Jetson Nano, we send the output to a remote server to control the elevator.



## Implementaion

### Hand Detection

<img src="https://user-images.githubusercontent.com/85024328/126913339-c09c8a79-e4ad-41f4-9ec2-7ad82a7de196.png" width="300">

```
Training model: MobileNet
```

![image](https://user-images.githubusercontent.com/85024328/126913201-de2dbe4e-2a5a-4d5b-ae8f-ce3e7b44bfcf.png)
![image](https://user-images.githubusercontent.com/85024328/126913199-b63c0f4f-dc45-47d6-85f5-7f1be7f54592.png)
![image](https://user-images.githubusercontent.com/85024328/126913200-49a3110c-54aa-4d95-9db0-eacad8262782.png)

Results:
* training curve:<br/>
![image](https://user-images.githubusercontent.com/85024328/126913220-bc61079e-1428-49bc-b461-a07c7a0f7846.png)
* confusion matrix:<br/>
![image](https://user-images.githubusercontent.com/85024328/126913238-68d661ba-a6af-4a31-9c68-99f205116e60.png)

### Gesture Recognition
<img src="https://user-images.githubusercontent.com/85024328/126913452-4baf491b-03fb-4bfa-a407-a557239963a3.png" width="300">

```
API: Google MediaPipe
```

<img src="https://user-images.githubusercontent.com/85024328/126913480-5ca26c9f-f78d-4814-b2d6-3f87d862e806.png" width="600">

![image](https://user-images.githubusercontent.com/85024328/126913608-210f70f3-2191-473e-8d47-073d05144f7f.png)




---
Y: Hand detected <br/>
N: Hand NOT detect


<img src="https://i.imgur.com/WfL61Gv.png" width="600">


---


###
* Idle state

Enter the IDLE state when no hand or any object detected



<img src="https://i.imgur.com/HCuMy2M.png" width="600">



---

###
* Triggered state

Open camera and start gesture recognition


<img src="https://i.imgur.com/hZ7tg5h.png" width="600">



---

###
* Identified gesture

“ok” gesture as input trigger signal<br/>
“1” ~ “9” gesture as select floors signal<br/>
There are also "open" and "close" gesture that can be used to open or close the elevator<br/>
Other gesture as unknown


<img src="https://i.imgur.com/mWNiWop.png" width="600">



---

###
### Control Simulation
* Elevator Animation

<img src="https://i.imgur.com/06xGDrr.png" width="600">




## Power Optimization
<img src="https://user-images.githubusercontent.com/85024328/126913670-95650abc-ca44-4160-858a-9a29a9aef9ad.png" width="600">




## Innovation & Difficulties
<h3 id="Innovation"><b>Innovation</b></h3>


* Control the elevator with gesture recognition
*  Always-on system
*  Use ultra-low power AI ASIC (Himax WE-I Plus) as the trigger unit
*  Low latency, real-time hand detection and gesture recognition
*  Support continuous floors input
*  Simulate elevator flow control through JavaScript
*  Use gesture recognition to remotely control server
*  Combination of high OPS unit and low power edge sensor


<h3 id="Difficulties"><b>Difficulties</b></h3>

* Privacy
*  Multi-gesture recognition
*  Scenes variation
*  Different skin color
*  Different type of gestures 
*  Handicapped unfriendly
*  Recognition speed leads to errors


<!-- ![image](https://user-images.githubusercontent.com/85024328/126896501-ea881ff7-d7d1-4585-9185-4fb7fc4c156f.png) -->
<!-- ![image](https://user-images.githubusercontent.com/85024328/126896550-7e98469d-3c87-411b-b4ec-2f3f7a9c5ec8.png) -->



## Demo Video ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

<a href="https://youtu.be/XFymUaxBFEE
" target="_blank"><img src="https://user-images.githubusercontent.com/85024328/126896550-7e98469d-3c87-411b-b4ec-2f3f7a9c5ec8.png" 
alt="Link is failed!" width="800" border="10" /></a>

## System architecture
<img src="https://user-images.githubusercontent.com/51142934/126688700-0d2efc21-179b-4a5f-b32e-562f179e645f.png" width="800">

## Physical Design
![](https://i.imgur.com/h58VDno.jpg)



## Flow Chart

<img src="https://i.imgur.com/l8BaPu6.png" width="500">


## Tools
<b style="font-size: 18px">Hand Detection</b>

* Himax WE-I Plus
* TensorFlow Lite
* Keras

<b style="font-size: 18px">Gesture Recognition</b>

* NVIDIA Jetson Nano
* OpenCV
* MediaPipe API

<b style="font-size: 18px">Control Simulation</b>
* Elevator animation
* jQuery
* Express.js






## Required Hardware
<table>
  <tr>
    <td>Hardware</td>
  </tr>
 <tr>
    <td>HC-SR04</td>
  </tr>
  <tr>
    <tr>
    <td>Himax WE-I Plus</td>
  </tr>
    <td>HDMI screen</td>
  </tr>
  <tr>
    <td>NVIDIA Jetson Nano</td>
  </tr>
  <tr>
    <td>Logitech Webcam</td>
  </tr>
  <tr>
    <td>AC8265 2.4G/5G WiFi BT4.2</td>
  </tr>
 
 </table>
 
## Required Software

<table>
  <tr>
    <td>Software</td>
    <td>Version</td>
  </tr>
  <tr>
    <td>distro-info</td>
    <td>0.18ubuntu0.18.04.1</td>
   </tr>
 <tr>
    <td>Jetson.GPIO</td>
    <td>2.0.17</td>
 </tr>
 <tr>
    <td>matplotlib</td>
   <td>2.1.1</td>
   </tr>
 <tr>
   <td>mediapipe</td>
   <td>0.8.5-cuda102</td>
   </tr>
 <tr>
   <td>numpy</td>
   <td>1.19.4</td>
   </tr>
 <tr>
   <td>opencv-contrib-python</td>
   <td>4.5.3.56</td>
   </tr>
 <tr>
   <td>pip</td>
   <td>21.1.3</td>
   </tr>
 <tr>
   <td>pyserial</td>
   <td>3.5</td>
   </tr>
 <tr>
   <td>python-apt</td>
   <td>1.6.5+ubuntu0.6</td>
   </tr>
   <td>requests</td>
   <td>2.18.4</td>
   </tr>
   <tr>
   <td>requests-unixsocket</td>
   <td>0.1.5</td>
  </tr>
</table>

## User guide
dir tree <br/>

```
dir_tree.txt
├─Elvator_Animation
│  ├─Elvator_Animation
│  │  └─public
│  │      ├─css
│  │      ├─images
│  │      └─js
│  └─node_modules
│      ├─.bin
│      ├─@sindresorhus
│      │  └─is
│      │      └─dist
│      ├─@szmarczak
│      │  └─http-timer
│      │      └─source
│      ├─abbrev
│      ├─accepts
│      ├─ansi-align
│      │  └─node_modules
│      │      ├─ansi-regex
│      │      ├─emoji-regex
│      │      │  └─es2015
│      │      ├─is-fullwidth-code-point
│      │      ├─string-width
│      │      └─strip-ansi
│      ├─ansi-regex
│      ├─ansi-styles
│      ├─anymatch
│      ├─array-flatten
│      ├─balanced-match
│      │  └─.github
│      ├─binary-extensions
│      ├─body-parser
│      │  └─lib
│      │      └─types
│      ├─boxen
│      ├─brace-expansion
│      ├─braces
│      │  └─lib
│      ├─bytes
│      ├─cacheable-request
│      │  ├─node_modules
│      │  │  ├─get-stream
│      │  │  └─lowercase-keys
│      │  └─src
│      ├─camelcase
│      ├─chalk
│      │  ├─node_modules
│      │  │  ├─has-flag
│      │  │  └─supports-color
│      │  └─source
│      ├─chokidar
│      │  ├─lib
│      │  └─types
│      ├─ci-info
│      ├─cli-boxes
│      ├─clone-response
│      │  └─src
│      ├─color-convert
│      ├─color-name
│      ├─concat-map
│      │  ├─example
│      │  └─test
│      ├─configstore
│      ├─content-disposition
│      ├─content-type
│      ├─cookie
│      ├─cookie-signature
│      ├─crypto-random-string
│      ├─debug
│      │  └─src
│      ├─decompress-response
│      ├─deep-extend
│      │  └─lib
│      ├─defer-to-connect
│      │  └─dist
│      ├─depd
│      │  └─lib
│      │      ├─browser
│      │      └─compat
│      ├─destroy
│      ├─dot-prop
│      ├─duplexer3
│      ├─ee-first
│      ├─emoji-regex
│      │  └─es2015
│      ├─encodeurl
│      ├─end-of-stream
│      ├─escape-goat
│      ├─escape-html
│      ├─etag
│      ├─express
│      │  └─lib
│      │      ├─middleware
│      │      └─router
│      ├─fill-range
│      ├─finalhandler
│      ├─forwarded
│      ├─fresh
│      ├─get-stream
│      ├─glob-parent
│      ├─global-dirs
│      ├─got
│      │  └─source
│      │      └─utils
│      ├─graceful-fs
│      ├─has-flag
│      ├─has-yarn
│      ├─http-cache-semantics
│      ├─http-errors
│      ├─iconv-lite
│      │  ├─encodings
│      │  │  └─tables
│      │  └─lib
│      ├─ignore-by-default
│      ├─import-lazy
│      ├─imurmurhash
│      ├─inherits
│      ├─ini
│      ├─ipaddr.js
│      │  └─lib
│      ├─is-binary-path
│      ├─is-ci
│      ├─is-extglob
│      ├─is-fullwidth-code-point
│      ├─is-glob
│      ├─is-installed-globally
│      ├─is-npm
│      ├─is-number
│      ├─is-obj
│      ├─is-path-inside
│      ├─is-typedarray
│      ├─is-yarn-global
│      ├─json-buffer
│      │  └─test
│      ├─keyv
│      │  └─src
│      ├─latest-version
│      ├─lowercase-keys
│      ├─make-dir
│      │  └─node_modules
│      │      ├─.bin
│      │      └─semver
│      │          └─bin
│      ├─media-typer
│      ├─merge-descriptors
│      ├─methods
│      ├─mime
│      │  └─src
│      ├─mime-db
│      ├─mime-types
│      ├─mimic-response
│      ├─minimatch
│      ├─minimist
│      │  ├─example
│      │  └─test
│      ├─ms
│      ├─negotiator
│      │  └─lib
│      ├─nodemon
│      │  ├─bin
│      │  ├─doc
│      │  │  └─cli
│      │  ├─lib
│      │  │  ├─cli
│      │  │  ├─config
│      │  │  ├─help
│      │  │  ├─monitor
│      │  │  ├─rules
│      │  │  └─utils
│      │  └─node_modules
│      │      ├─debug
│      │      │  └─src
│      │      └─ms
│      ├─nopt
│      │  ├─bin
│      │  ├─examples
│      │  └─lib
│      ├─normalize-path
│      ├─normalize-url
│      ├─on-finished
│      ├─once
│      ├─p-cancelable
│      ├─package-json
│      │  └─node_modules
│      │      ├─.bin
│      │      └─semver
│      │          └─bin
│      ├─parseurl
│      ├─path-to-regexp
│      ├─picomatch
│      │  └─lib
│      ├─prepend-http
│      ├─proxy-addr
│      ├─pstree.remy
│      │  ├─lib
│      │  └─tests
│      │      └─fixtures
│      ├─pump
│      ├─pupa
│      ├─qs
│      │  ├─dist
│      │  ├─lib
│      │  └─test
│      ├─range-parser
│      ├─raw-body
│      ├─rc
│      │  ├─lib
│      │  └─test
│      ├─readdirp
│      ├─registry-auth-token
│      ├─registry-url
│      ├─responselike
│      │  └─src
│      ├─safe-buffer
│      ├─safer-buffer
│      ├─semver
│      │  └─bin
│      ├─semver-diff
│      │  └─node_modules
│      │      ├─.bin
│      │      └─semver
│      │          └─bin
│      ├─send
│      │  └─node_modules
│      │      └─ms
│      ├─serve-static
│      ├─setprototypeof
│      │  └─test
│      ├─signal-exit
│      ├─statuses
│      ├─string-width
│      ├─strip-ansi
│      ├─strip-json-comments
│      ├─supports-color
│      ├─term-size
│      │  └─vendor
│      │      ├─macos
│      │      └─windows
│      ├─to-readable-stream
│      ├─to-regex-range
│      ├─toidentifier
│      ├─touch
│      │  └─bin
│      ├─type-fest
│      │  └─source
│      ├─type-is
│      ├─typedarray-to-buffer
│      │  └─test
│      ├─undefsafe
│      │  └─lib
│      ├─unique-string
│      ├─unpipe
│      ├─update-notifier
│      ├─url-parse-lax
│      ├─utils-merge
│      ├─vary
│      ├─widest-line
│      ├─wrappy
│      ├─write-file-atomic
│      └─xdg-basedir
├─Himax_WEI_Plus
│  ├─1_tfTrain
│  ├─2_tfLite
│  │  └─generated
│  └─3_firmware
│      ├─hand_detection
│      │  └─src
│      ├─inc
│      └─src
└─NVIDIA_Jetson_Nano
    └─src
        └─__pycache__
```



<!-- ## Elevator
<img src="https://i.imgur.com/C3cTFHO.png" width="500"> -->

![image](https://user-images.githubusercontent.com/85024328/126911058-822af750-199e-4e61-a547-2033c02be03d.png)


