#!/usr/bin/env python

import subprocess

import rospy

from udevadm_monitor.msg import Event


def _event_output_to_msg(event_output):
    lines = event_output.strip().split('\n')
    return Event(**dict((line.split('=') for line in lines[1:])))


def monitor():
    """Listens to changes in USB devices and publishes Event messages to the
    'event' topic on each change.
    """

    rospy.init_node('monitor_usb', anonymous=True)
    publisher = rospy.Publisher('event', Event, queue_size=10)

    process = subprocess.Popen(
        ['unbuffer', 'udevadm', 'monitor', '--subsystem-match=usb',
        '--property'], stdout=subprocess.PIPE, bufsize=0)

    output_buffer = ''

    for line in iter(process.stdout.readline, ''):
        output_buffer += line
        
        if line != '\n':
            continue

        event_output = output_buffer
        output_buffer = ''

        if event_output.startswith('monitor will print'):
            # Discard program preamble
            continue

        lines = event_output.strip().split('\n')

        msg = _event_output_to_msg(event_output)
        publisher.publish(msg)


if __name__ == '__main__':
    monitor()
