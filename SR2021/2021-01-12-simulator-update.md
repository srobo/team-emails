---
to: SR2021 teams
subject: Student Robotics Simulator Update SR2021.3
---

Hello there!

We've released some new versions of the simulator, which include a few
improvements we felt were important to release before the first leagues:

- Reconstructed the inner walls (again) to fix issues with distance sensors.
  Thanks to everyone in Discord who helped us track this down.
  **Note**: the inner walls may be _slightly different_ now, though hopefully
  not noticeably so.
- Fixed a bug where robot code could end up stuck waiting for the match-start
  signal when run in competition mode. Thanks to the team which reported issues
  with their code during the friendlies for helping find this one.

As usual this can be downloaded from [the docs][simulator-install-docs].
We recommend updating and testing your code with this version as soon as
possible so you can test your code with the working distance sensors.

[simulator-install-docs]: https://studentrobotics.org/docs/simulator/#installing-the-simulation

Thanks,

SR Competition Team
