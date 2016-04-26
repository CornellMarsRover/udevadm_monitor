# udevadm_monitor

A ROS package which publishes the output of
`udevadm monitor --subsystem-match=usb --property` to a ROS topic.

This can be used to detect addition or removal of USB devices to the system.

## Usage

This package depends on `expect-dev`, which is not currently in the `rosdep`
listings. Install it using `sudo apt-get install expect-dev`.

After building, run `rosrun udevadm_monitor monitor_usb.py`, then run
`rostopic echo /event`. Add or remove USB devices to your system to see the
kinds of messages that are printed.
