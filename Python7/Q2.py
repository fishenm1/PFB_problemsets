#!/usr/bin/env python3 

import re

poem =""" Nobody by Shel Silverstein

Nobody loves me,
Nobody cares,
Nobody picks me peaches and pears.
Nobody offers me candy and Cokes,
Nobody listens and laughs at me jokes.
Nobody helps when I get in a fight,
Nobody does all my homework at night.
Nobody misses me,
Nobody cries,
Nobody thinks I'm a wonderful guy.
So if you ask me who's my best friend, in a whiz,
I'll stand up and tell you that Nobody is."""

new_poem = re.sub (r"Nobody", "Nicole", poem)
