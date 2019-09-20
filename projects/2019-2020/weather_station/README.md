# Weather Station

## Overview

The goal for this year is to build a weather station using a raspberry PI and enviro+ module to gather various atmospheric metrics and push them to a centralised database. These metrics will be consumed by a graphing tool that will represent each metric on its respective graph.

The first semester, the focus will be on the client side. Ninjas will have to code the weather station and store the environment metrics locally into a database.  

The second semester,  We will focus on server client paradigm building the server API to process the data from the weather stations and upgrading the weather station to post data over https. 

## Material

* Raspberry PI 0 WH:  <https://www.adafruit.com/product/3708>
* Standoff + screw: <https://shop.pimoroni.com/products/brass-m2-5-standoffs-for-pi-hats-black-plated-pack-of-2>  
* Sensor:  <https://shop.pimoroni.com/products/enviro-plus>

## Week 1

* Presentation and introduction to the project.
* Why is this an interesting project?
* What can we do with it?
* Go throw the plan for the first semester.
* Send the link to GitHub page for the course.

## Week 2

* Explain how the different sensors works:
  * What metrics can be gathered from each sensor.  
* Python review (I)
* Show running python script gathering metrics from pressure and temperature sensors.
* Introducing the concept of mock testing to replace the physical sensors with a software interface

## Week 3

* Python review (II).
* Building a mock for temperature, pressure and humidity sensors.

## Week 4

* Object Oriented Programming in Python.
* Design the main structure of the application.
  * Connection with the mock.

## Week 5

* Add functionalities for gathering and printing to stdout the following environmental values:
  * Function for pressure.
  * Function for temperature
  * Function for humidity
* ByPassing the mock to test with physical hardware.

## Week 6

* Start installing the raspberry Pi:
  * Install OS.
  * Plug-in the sensors.
  * Load the code.

* Introduction to 3d printing.
  * Start designing a case for the weather station.

## Week 7

* Introduction to Databases.
* Adding unit tests for environmental functions: pressure, temperature, humidity.
* Start building interface with database.

## Week 8

* Separate data model from code.
* Python database drivers.

## Week 9

* Create a data base interface for inserting metric values into a database.
* Insert temperature, humidity and pressure into the database.
* Query database to confirm metrics are saved.

## Week 10

* Introduce new sensor: Gas sensor:
  * CO Carbon Monoxide.
  * H2 Hydrogen.
  * CH4 Methane.
  * C3H8 Propane.
* Extend mock class to support the new metrics.

## Week 11

* Add new function to the application to read gas sensor metrics.
* Add unit tests for the new functions
* Save new metrics into the DB

## Week 12

* 3D printing. Designing and printing the PI case.
* Configure the application to start up during boot time.
