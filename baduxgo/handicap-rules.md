---
layout: default
title: Badux Go Handicap Rules
description: How handicap games work in Badux. Black takes extra opening stones, White's komi is adjusted to match, and the game is scored as an even game would be.
---

# Badux Go Handicap Rules

A handicap lets two players of different strength play an interesting game. The weaker player takes
Black and starts with extra stones on the board, and White's komi is adjusted to match. Badux uses
the traditional Go handicap system, adapted only where the hexagonal board or area scoring calls for
it. The rules come first; the reasons behind them, and which classic Go rule sets they are drawn
from, follow.

## The Rules

### The Handicap Ladder

A handicap is one of the following, in increasing order of advantage:

<div style="text-align: center;">
  <table style="border-collapse: collapse; margin: 1rem auto;">
    <thead>
      <tr>
        <th style="background: #2c3e50; color: white; padding: 0.75rem 1.5rem; text-align: left;">Handicap</th>
        <th style="background: #34495e; color: white; padding: 0.75rem 1.5rem; text-align: left;">What Black gets</th>
        <th style="background: #2c3e50; color: white; padding: 0.75rem 1.5rem; text-align: center;">Komi</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: left;">No komi</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: left;">The first move, and almost no komi</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">0.5</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: left;">Two stones</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: left;">Two stones on the board before White moves</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">1.5</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: left;">Three stones</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: left;">Three stones before White moves</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">2.5</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: left;">Four stones</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: left;">Four stones before White moves</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">3.5</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: left;">Five stones</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: left;">Five stones before White moves</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">4.5</td>
      </tr>
    </tbody>
  </table>
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">The handicap ladder</p>
</div>

For comparison, an even game is Black's first move against 6.5 points of komi.

### The Receiver Plays Black

The player receiving the handicap always plays Black. Whoever gives the handicap plays White.

### Opening Stones

In a stone handicap, Black's opening stones are the first moves of the game: Black takes that many
turns in a row, placing one stone per turn, before White's first move. After the last opening stone,
White plays, and the game alternates normally from there.

- Opening stones may be placed on any empty cells. The board's star points carry no special meaning
  for them.
- Each opening stone is a full turn. It is played on the clock like any other move.
- Black may not pass while opening stones remain to be played. Black may resign at any time, as
  always.

### Komi

Komi in a handicap game is the number of opening stones minus one half. Komi always belongs to
White, and it is never negative. The half point means a handicap game cannot end in a tie, just as
an even game cannot. What would otherwise be a tie goes to White.

### Scoring

A handicap game is scored exactly like an even game: your area is your living stones, the empty
cells you surround, and any dead opponent stones on the board, and White adds komi. The opening
stones count as Black's area like any other stones. No other adjustment is made; the komi already
accounts for them.

### Summary

1. The receiver of a handicap plays Black.
2. The handicaps are no komi, two, three, four, and five stones.
3. Black plays the opening stones as consecutive first turns, anywhere on the board, one per turn,
   on the clock.
4. Black may not pass until the opening stones are all played.
5. Komi is the number of opening stones minus one half: 0.5, 1.5, 2.5, 3.5, or 4.5.
6. The game is then scored as an even game would be, with White adding komi.

## Why These Rules

Go has handicapped games for as long as it has had players of different strength, and its handicap
system is one of the most uniform things about the game across countries and rule sets. Where the
classic rule sets agree, we follow them. Where they differ, we say which one we follow and why.
Where the hexagonal board or our scoring changes the picture, we say what changed.

### The Traditional Ladder

Counting a handicap in stones is universal. A two-stone handicap means two Black stones on the board
before White moves, in English, Japanese, Chinese, and Korean alike, and every major Go server
offers handicaps as a whole number of stones. We use those rungs and those names so that a handicap
in Badux means what it means everywhere else.

The bottom rung is the one exception in Go itself. Playing Black with no komi is a real handicap,
worth about one stone, but nothing extra goes on the board for it. Servers commonly file it as "one
stone"; players call it "no komi" or, in Japanese, jōsen. We use the plain name.

The ceiling of five stones is a starting guess suited to the board sizes Badux is played on. It may
grow.

### The Receiver Plays Black

This is the universal convention: the weaker player takes Black and the stones. We adopt it as it
stands.

### Free Placement

The Chinese, AGA, and Ing rule sets let Black place handicap stones on any points. The Japanese and
Korean rule sets fix them on the star points, in a prescribed order. We follow the free-placement
rule sets.

The stronger reason is that fixed placement is a tradition of the square board. Its star points have
a long history as the natural handicap points, and the prescribed arrangements for each number of
stones grew out of centuries of play on that board. The hexagonal board has star points too, but no
one has yet played enough handicap Go on it to know where the stones belong. Free placement is also
the more interesting game to begin with: choosing where to put your advantage is part of the
advantage.

### Opening Stones as Moves

Under the free-placement rule sets the handicap stones are placed before White's first move, and on
servers that offer free placement Black simply plays them as consecutive turns. We do the same. This
keeps the opening stones inside the normal rules of a move: they are played on the board, one at a
time, on the clock, and Black can be timed out while placing them just as on any other turn.

Black may not pass during the opening stones because a pass would leave the handicap incomplete by
choice, and the simplest rule is that a player who asked for stones plays them.

### Komi and Area Scoring

Modern practice in every rule set gives White a half-point komi in handicap games, so that a tie is
impossible. We keep that. Classical Japanese play gave no komi at all and allowed a drawn game, but
the half point has been standard for decades.

The rest of the komi comes from how Badux scores. Badux uses area scoring, the Chinese system, in
which every stone on the board at the end counts as a point. Under territory scoring, the Japanese
system, an opening stone never scores by itself. So in an area-scored game, each opening stone is
worth a point more than the same stone would be under territory scoring, and a two-stone handicap
would be a slightly bigger handicap here than in Japan. The area-scoring rule sets correct for this,
and we follow the AGA correction: White receives one point for each opening stone beyond the first.
The first opening stone is Black's ordinary first move, which an even game has as well and the
normal end of the game accounts for. Each further stone is a move Black made without a reply from
White, and the point it scores is handed back.

With the half point added, that gives komi of one half less than the number of opening stones: 1.5
for two stones, 2.5 for three, and so on. The no-komi rung has one opening stone, Black's first
move, and so needs no correction: its komi is the half point alone.

The Chinese rules make the same correction by a different route, having Black return half a stone
per handicap stone at the count, which works out to one point per opening stone rather than one per
stone beyond the first. We chose the AGA figure because its reasoning is stated plainly in its own
rules, and because it keeps the no-komi rung an honest name.

## Handicap Games in Badux Go

A handicap game is arranged through an invitation to a specific opponent, which names who receives
the handicap and how much. The receiver plays Black, so the invitation carries no separate choice of
colour. Handicap games are not rated: the rating system has no correction for a handicap, so a
handicap game changes no one's rating. A rematch of a handicap game keeps the same handicap for the
same player, and so keeps the same colours.

---

**Ready to play?** Visit [BaduxGo.com](https://baduxgo.com) to start a game, or read the
[Rules of Badux](/baduxgo/rules.html) for the full rules of an even game.
