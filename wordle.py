#!/usr/bin/env python3
import sys
from datetime import date, timedelta
from collections import defaultdict
from wordlist import valid_answers
from state import state
from pathlib import Path

if __name__ == "__main__":
    # checks if script is ran for today, exits if ran
    today = date.today().isoformat()
    if state["date"] == today:
        sys.exit(0)

    # now_date -> date when i made this script
    # end_date -> date when this wordle wordlist was supposed to "end" iirc? correct me pls.
    now_date = date(year=2022, month=2, day=3)
    end_date = date(year=2022, month=6, day=20)

    # init dict
    answers = defaultdict(str)

    # build the dict
    # with "shard" as the answer for feb 3, 2022
    idx = valid_answers.index("shard")
    date = now_date
    diff = timedelta(days=1)
    while date != end_date:
        answers[date.isoformat()] = valid_answers[idx]
        date += diff
        idx += 1

    # display the word of the day
    print("The word of the day is", answers[today].upper())

    updated_state = {"date": today}
    with open('state.py', 'w') as f:
        f.write(f"state = {str(updated_state)}")
