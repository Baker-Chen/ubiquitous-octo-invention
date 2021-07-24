![image](https://user-images.githubusercontent.com/85024328/120073598-9e337a80-c0cb-11eb-91b6-afecf940a960.png)
# 2021 Synopsys ARC AIoT Design Contest
# NCHU WE-I Goose．Smith


* <a href="#Introduction">Introduction</a>
* <a href="#Innovation-amp-Difficulties">Innovation & Difficulties</a>
    * <a href="#Innovation">Innovation</a>
    * <a href="#Difficulties">Difficulties</a>
* <a href="#Demo-Video">Demo Video</a>
* <a href="#System-architecture">System architecture</a>
* <a href="#Physical-Design">Physical Design</a>
* <a href="#Flow Chart">Flow Chart</a>
* <a href="#Tools">Tools</a>
* <a href="#Required-Hardware">Required Hardware</a>
* <a href="#Required-Software">Required Software</a>
* <a href="#User-guide">User guide</a>
* <a href="#Elevator">Elevator</a>




## Smart elevator based on edge computing architecture combined with gesture recognition
## Introduction
In the post pandemic era, zero-contact technology has become a trend. Among them, the elevator is beneficial to the spread of the virus, because the elevator space is small, closed and crowded. It is easy to infect because people contact the elevator control panel and talk to each other in the elevator. So we wanted to achieve a smart elevator control panel that can recognize the specific gestures and always-on system through the benefits of Himax WE-I Plus ultra-low power consumption and AI acceleration, and reduce operation complexity and overall power consumption through a distributed computing architecture of edge computing.

This project combines the advantage of Himax WE-I Plus and NVIDIA Jetson Nano, which are low-power comsumptioned and high efficiency respectively.Using cygwin to transfer the pretrained model into the version of Tensorflow lite, then detecting the hand movement by Himax WE-I Plus, depend on NVIDIA Jetson Nano to process the gesture recognition, send the recognition output to the server to control the elevator. 


## Innovation & Difficulties
<b style="font-size: 18px" id="Innovation">Innovation</b>

* Control the elevator with gesture recognition
*  Always-on system
*  Use ultra-low power AI ASIC (Himax WE-I Plus) as the trigger unit
*  Low latency, real-time hand detection and gesture recognition
*  Support continuous floors input
*  Simulate elevator flow control through JavaScript
*  Use gesture recognition to remotely control server
*  Combination of high OPS unit and low power edge sensor

<b style="font-size: 18px" id="Difficulties">Difficulties</b>

* Privacy
*  Multi-gesture recognition
*  Scenes variation
*  Different skin color
*  Different type of gestures 
*  Handicapped unfriendly
*  Recognition speed leads to errors





## Demo Video
## System architecture
<img src="https://user-images.githubusercontent.com/51142934/126688700-0d2efc21-179b-4a5f-b32e-562f179e645f.png" width="800" height="300">

## Physical Design
![](https://i.imgur.com/GAjMDkY.jpg)


## Flow Chart

<img src="https://i.imgur.com/l8BaPu6.png" width="500">


## Tools
<b style="font-size: 18px">Gesture Detection</b>

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
    <td>Himax We-I Plus</td>
  </tr>
    <td>HDMI screen</td>
  </tr>
  <tr>
    <td>NVIDIA Jatson Nano</td>
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



## Elevator
<img src="https://i.imgur.com/C3cTFHO.png" width="500">



<style>
b {
font-size:20px,
}
#function {
color:
}
</style>
