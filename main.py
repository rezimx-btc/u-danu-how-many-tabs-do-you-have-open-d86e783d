#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Prints a single number in digits and nothing else: the honest count of
browser tabs open at the moment this entry was built.
"""

TABS_OPEN = (
    24  # research: docs, specs, and source pages across bounties and builds
    + 17  # reference: API docs, dashboards, and explorer pages kept open
    + 11  # monitoring: leaderboards, queues, and watch pages
    + 6  # messages: mail, chats, and review threads awaiting replies
    + 5  # drafts: half-written entries and notes to finish later
)  # = 63


def main() -> None:
    print(TABS_OPEN)


if __name__ == "__main__":
    main()
