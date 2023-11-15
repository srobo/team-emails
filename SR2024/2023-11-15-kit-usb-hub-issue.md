---
to: Student Robotics 2024
subject: SR2024 Power board connectivity issues
---

Hello all,

We've seen reports in Discord from a few teams about issues around board connectivity where a "No boards of this type found" error is thrown for the power board, whilst the wiring and connections are seemingly correct.

We've been able to track this down to a bug in Raspberry Pi OS (which our custom kit OS is based on), where plugging the motor board into certain ports on the USB hub causes all boards to be undetectable. If you're interested in the intricate details, see [here](https://github.com/raspberrypi/linux/issues/3779#issuecomment-709481662) and [here](https://groups.google.com/g/linux.debian.bugs.dist/c/5jI9dDZgfUU).

To mitigate this issue, please plug your motor board either directly into the Raspberry Pi or into the 3 ports closest to the input of the USB hub, as shown below. Other devices can be connected as normal.

![]()

This issue is not isolated to our motor board - if you are using any custom USB devices with an FTDI chip, it can cause similar issues, so please plug them into the same ports listed above. Of the kit provided by Student Robotics, only the motor board is impacted.

If you have any questions or concerns, please let us know either in Discord or by replying to this email.
