---
to: sr2020-teams
subject: SR2020 Virtual Competition Schedule and New Simulation Version
---

Hi all

## The Competition Schedule

We're pleased to announce the structure of the SR2020 virtual competition. We will be running 5 sessions over 3 weekends.

You will have until 10am on each day to make changes before your team's code is frozen. We will be in contact soon about our submission process.

**At 3pm we will be live-streaming matches** back-to-back on YouTube.

| Date           | Competition Stage                                                   |
|----------------|---------------------------------------------------------------------|
| 11th July 2020 | [League Part 1](https://studentrobotics.org/events/sr2020/virtual-competition-league-1/)       |
| 12th July 2020 | [League Part 2](https://studentrobotics.org/events/sr2020/virtual-competition-league-2/)       |
| 18th July 2020 | [League Part 3](https://studentrobotics.org/events/sr2020/virtual-competition-league-3/)       |
| 19th July 2020 | [League Part 4](https://studentrobotics.org/events/sr2020/virtual-competition-league-4/)       |
| 25th July 2020 | [Knockouts and Final](https://studentrobotics.org/events/sr2020/virtual-competition-knockouts/)|

## Version 0.3.1 of the Simulation

We have released version 0.3.1 of the competition simulation which you can download from the [Docs page](https://studentrobotics.org/docs/competition-simulator/).

Here are some of the notable changes since 0.2.0:

- Raise an error if you try to `R.sleep()` with seconds less than or equal to 0
- Fix intermittent `ValueError`s in vision code caused by floating point rounding
- Only launch one Webots thread when using custom initialisation
- Stop Python processes being left behind after running the simulation
- Fix Webots access violations (Controller exited with status -1)
- Create a log file for each robot to aid debugging

See you at the virtual competition!
