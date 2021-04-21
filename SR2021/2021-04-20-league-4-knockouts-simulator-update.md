---
to: All SR2021 teams
subject: Student Robotics League 4, Finals & Simulator Update
---

Hi,

With the final round of league matches coming up this weekend and the finals the
week after, we wanted to give you some quick reminders about the schedule. We've
also fixed a small bug in the compass which should make it more accurate.

## Simulator Update

We've released a new version of the simulator, which includes a fix to the way
that noise is treated within the compass. Previously the compass readings could
sometimes have excessive noise or noise which was was biased towards one side.
The noise is now a consistent, balanced level and we have slightly reduced the
level of noise to reflect real hardware.

The update can be downloaded from the normal place in [the docs][simulator-install-docs].
We recommend updating and testing your code with this version as soon as
possible as this version will be used in this weekend's league matches.

[simulator-install-docs]: https://studentrobotics.org/docs/simulator/#installing-the-simulation

## Code Submission Deadlines

The deadline for [code submission][code-submitter] for league 4 and for the
finals is 8pm BST (UK time) on the respective Friday beforehand. If your team is
going to have any difficulty uploading your code by this time let us know before
the deadline and we'll try to sort something out.

*Note*: if you don't submit code for league 4 you will be unable to enter the
knockouts. Code you submit for league 4 will be carried over into the  knockouts
unless you submit code again before the knockouts deadline. This is to simplify
scheduling of the knockouts. Of course we're expecting that many teams will want
to improve their code between the league and the knockouts and then resubmit,
that's completely fine.

*Tip*: do check that you have tried running the code archive you're going to
upload by running a competition match using it. There are instructions for the
`run-comp-match` script within the README of the simulator.

## Match Livestreams

As before we'll be kicking off our live streams of the matches at noon BST
for around a couple of hours of matches.

* [League 4 Livestream][league-4-stream]
* [Knockouts Livestream][knockouts-stream]


We look forward to seeing your robots this weekend and next.


[code-submitter]: https://studentrobotics.org/code-submitter/
[league-4-stream]: https://www.youtube.com/watch?v=E9gF-GZbf5M
[knockouts-stream]: https://www.youtube.com/watch?v=gxJM6ernMqo
