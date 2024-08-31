# PiNtuitive

**What if...**  
What if you could decide what software your assistant or tablet runs?  
What if your assistant or tablet didn't become obsolete just because its manufacturer decided to stop providing updates one or two years after its release?
What if your digital assistant didn't report your conversations to a large corporation?  

You might find yourself back in a time when devices were designed so that users could decide, to a greater extent, what software they ran. A time when most business models related to software focused on licensing and sales, rather than deploying a suite of subscription-based services. A time when business models didn't hijack the user's ability to decide how to use the hardware they had lawfully purchased. A time when, as a consequence, we generated less waste, made better use of our hardware, and enjoyed more freedom in choosing what compatible software should run on the hardware we just acquired.

## PiNtuitive: Freedom at Your Fingertips

PiNtuitive is an application designed with a clear vision and purpose: to provide users with a simple, intuitive, and touchscreen-friendly interface for their RaspberryPi. It also offers a development environment for creating widgets and simple applications, allowing users to customize their RaspberryPi to their liking.

1. **Touchscreen Adaptability for RaspberryPi:**  
   PiNtuitive allows any RaspberryPi with a touchscreen to become an intuitive and easy-to-use device. It automatically resizes all windows make them full-screen, and removing the close, minimize, and maximize buttons. This way, users can navigate through the interface with ease, without the need for a mouse or keyboard. Additionally, PiNtuitive displays a bottom bar, to allow users interact with open applications (for example, to close them), and to display a virtual keyboard.

2. **A digital assistant, that can be easily iterated:**  
   PiNtuitive also provides a basic GUI to enable users to easily develop small applications or widgets with basic logic. Whether you want to create a clock, check the weather, search for and play music, or even implement a virtual assistant, PiNtuitive gives you the tools to do it effortlessly by using tools such as ReactJS, Electron, and NodeJS.

## Key Features

- **Optimized Touchscreen Interface:** Navigate, select, and control with ease, thanks to always full-screen windows and a bottom bar for easy access to applications.
- **Intuitive Development Environment:** Create and customize widgets and simple applications for your RaspberryPi to create your ideal digital assistant.
- **Complete Control:** Decide what software runs on your device and retain full control over your data.
- **Sustainability:** Use the RaspberryPi that fits your use case needs. Why upgrading to the latest Pi 5 model, if maybe 1GB of RAM is enough for the cool features you want to create?

## Installation

To install PiNtuitive, follow these steps:

1. Clone this repository to your RaspberryPi:

```bash
git clone https://github.com/oegea/PiNtuitive.git
```

2. Enable X11 Server on your RaspberryPi:

PiNtuitive only works with X11, so if you are using Wayland, switch back to X11 by running the following command.

```bash
sudo raspi-config
```

3. Install the required dependencies:

```bash
cd PiNtuitive
./install.sh
```

4. Start PiNtuitive:

```bash
./run.sh
```

## Development status

Currently PiNtuitive is in a very early stage of development. We are working on an MVP to test the concept and gather feedback from the community.
These are the main features that are actually working:

- [x] Automatically resize windows to full-screen and remove window controls. (Kiosk mode for all applications)
- [x] Display a bottom bar to interact with open applications, in order to close them and display a virtual keyboard.
- [x] Basic keyboard to input text, numbers and special characters.

The following features are still in progress:

- [ ] Create a basic GUI based on ReactJS to display widgets and basic applications, in order to use PiNtuitive as a digital assistant.
- [ ] Create a basic web app, from which users can add custom widgets and applications to their PiNtuitive interface.
- [ ] Create a repository system to allow users to share their widgets and applications with the community.
- [ ] Improve the keyboard to support more languages and layouts.
- [ ] Improve the installation process, to check if X11 is currently running.
- [ ] Improve the installation process, to set PiNtuitive to automatically start when the RaspberryPi boots.
 
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.