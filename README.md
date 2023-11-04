# GRABINATOR PROJECT

## This project was done for BE1200

## This project required a few things before getting started

#### 1.) A functional Raspberry pi 4 Model b 

#### 2.) A working laptop or pc.
#### 3.) VS Code
#### 4.) Servo Motors 
#### 5.) Jumper Wires(Male-to-Female and Male-to-Male)


## Getting Started

#### First you need to have a Raspberry Pi and a micro-sd card ready to be formatted.

#### Using an sd card reader, plug the sd card into your computer and naavigate to the following website.

[Rasbian](https://www.raspberrypi.com/software/)

This is where you download the Raspberry pi imager for your specific operating system. This process is quite short and once
downloaded, open up the imager on your current computer.


#### Once opened you will see the following:
![picture](https://github.com/AlessandroB1298/BE1200/blob/main/Screenshot%202023-10-31%20at%203.06.01%20PM.png )


#### Here you need to write to the raspberry pi, but first go into the settings and edit the username and password to ensure security.

#### Once you write to the pi, it will auto-eject, next, connect your pi to a power source and make sure it is blinking both green and holding a steady red light.

#### Next, open a terminal and type the following:
`sudo ssh <NAME_OF_PIE>@<PI'S IP ADDRESS`

This code essentially allows you to access your pi from your computer, creating a tunnel that only you, the root user has access to.

This is a safe and secure way to connect to your pi without using a mouse, keyboard, and monitor.

### Setting up on VS Code


#### Once you are logged into your pi, you will need to open it in vs code, do this by downloading VS Code on both your machine and the raspberry pi.

Once that is completed you will need to download the remote ssh extension on both OSs.

Next you will click on the extensioon by using the command shift+cmd+p this will bring up your pallete, which ypu will use to select the remote ssh connection option.

Then type in your password once again and you will be logged in!

Once all of that is done, bring up a terminal in VS code and copy this repository using:

`git clone <URL`

### Installing Dependencies

#### Next you will need to install all of the dependencies.
Do this by running the command:
`python install requirenments.txt`

#### Now we are done with the setup!

# Configuring wiring and servo motors

## This section is dedicated to the setup of the servo motors and connecting them with our raspberry pi 4
#### This is also very similar for Arduinos.


#### Our Servo Motors come with three wrires attached to them: Live,Ground, and Signal.

#### Our Raspberry Pi comes with many different pins and reading them is near impossible, however we can look at a gpio board.

![picture](https://github.com/AlessandroB1298/BE1200/blob/main/Screenshot%202023-11-04%20at%2012.58.17%20AM.jpeg)



#### The pins that say GPIO are very important, this is where our signal wire goes to from our servo motor.

#### You will also see a 5v pin and a ground pin when looking at a GPIO board.

### Reminder, make sure nothing is live when you are connecting wires, you could short circuit your pi and there is no way to fix it!

#### Simply you must connect the corresponding wires.


# Running The Program!

## This section is all about the exexution of our program.
#### Make sure that these lines represent your setup:

``` 
servo1 = Servo(<GPIO_NUMB>, pin_factory=factory)
servo2 = Servo(<GPIO_NUMB>, pin_factory=factory)
servo3 = Servo(<GPIO_NUMB>, pin_factory=factory)
```
#### Besides these adjustments, the rest of the code will work perfectlly, you will be prompted to open the app in a browser.

### Have Fun


