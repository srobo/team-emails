---
to: Student Robotics 2023
subject: Submit your robot for the SR2023 Virtual Competition
---

Hi

You can now submit your robot code through our website for the [virtual competition](https://studentrobotics.org/events/sr2023/virtual-competition/).

[Submit your robot code](https://studentrobotics.org/code-submitter/).

You have until 8pm (UK time) Friday 24th February to submit your team's latest code. You can upload early, but at that time we'll capture all the uploads. If you fail to upload any code, you will be marked as absent from all the matches and score 0 points. This will not affect your ability to compete in the [final competition](https://studentrobotics.org/events/sr2023/competition/).

Simply log in with your TLA (you can find this from your channel name in Discord, removing `team-`, in upper-case) and the password for your team's Discord channel we sent at the start of the competition year. If you need a refresher, please let us know in your team channel.

Once in, you can upload a `.zip` of your code. This zip must contain a `robot.py` file, and any other supporting code or data files your robot may need:

```
  robot.zip
  ├── secret_magic.py
  └── robot.py
```

You won't be able to re-submit between matches in the virtual competition, so it's important your code is as well-tested and reliable as possible come the submission deadline. Because of this, we have a few suggestions for things to keep in mind:

- Remember to use [`R.zone`](https://studentrobotics.org/docs/programming/sr/#OtherRobotAttributes) - as your robot could start in any of the four corners, not just corner 0.
- Make sure you're using [available libraries](https://studentrobotics.org/docs/programming/python/libraries#simulator).
- Make sure to use [`R.sleep`](https://studentrobotics.org/docs/simulator/programming/#simulated-time) rather than `time.sleep`.
- Try running your simulation in ["competition mode"](https://github.com/srobo/competition-simulator#competition-mode), in case there are any discrepancies.
- You can use [`R.is_simulated`](https://studentrobotics.org/docs/programming/sr/#OtherRobotAttributes) to determine whether your code is running in the simulator or not.

As a bonus, if a version of your code is uploaded by _this_ Friday at 8pm, we will run the matches for you in a competition setting, and let you know of any issues with your code, before the actual submission deadline!

You can see your team's previous uploads on that same page.

Good luck!
