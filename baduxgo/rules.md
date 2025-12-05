---
layout: default
title: Rules of Badux
---

# Rules of Badux

## Introduction

Badux follows the exact same rules as the traditional game of Go (also known as Baduk or Weiqi),
just played on a hexagonal board instead of a square one. If you already know how to play Go, you
already know how to play Badux.

Interestingly, the hexagonal topology actually makes Badux a *simpler* game than regular Go. There
are no cuts, no hanes, and no simple kos—concepts that can be challenging for beginners. This makes
Badux an excellent stepping stone for learning Go. Once you're comfortable with the fundamental
mechanics on a hex board, transitioning to the square board is straightforward.

This document provides a complete explanation of the rules, assuming no prior knowledge of Go. If
you're already familiar with Go and just want to understand what's different about Badux, skip
ahead to [Differences from Regular Go](#differences-from-regular-go) at the end.

**Note:** Badux is the name of the game. [BaduxGo.com](https://baduxgo.com) is the online server
where you can play.

## Equipment

Badux is played with:

- A hexagonal board of connected hexagonal cells
- Black stones and white stones

<div style="text-align: center;">
  <img src="/img/rules/rules-empty-board.png" alt="Empty Badux board">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">An empty 6×6×6 Badux board</p>
</div>

The darker points are *star points*. They behave the same as any other point on the board, but help
you find your way around.

While any board size is possible, Badux standardizes on three sizes, roughly matching the
traditional Go board sizes:

<div style="text-align: center;">
  <table style="border-collapse: collapse; margin: 1rem auto;">
    <thead>
      <tr>
        <th style="background: #2c3e50; color: white; padding: 0.75rem 1.5rem; text-align: center;">Go board</th>
        <th style="background: #34495e; color: white; padding: 0.75rem 1.5rem; text-align: center;">Points</th>
        <th style="background: #2c3e50; color: white; padding: 0.75rem 1.5rem; text-align: center;">Badux board</th>
        <th style="background: #34495e; color: white; padding: 0.75rem 1.5rem; text-align: center;">Points</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">9×9</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">81</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">6×6×6</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">91</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">13×13</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">169</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">8×8×8</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">169</td>
      </tr>
      <tr>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">19×19</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">361</td>
        <td style="background: #ecf0f1; padding: 0.5rem 1.5rem; text-align: center;">12×12×12</td>
        <td style="background: #f8f9fa; padding: 0.5rem 1.5rem; text-align: center;">397</td>
      </tr>
    </tbody>
  </table>
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">Comparing Go and Badux board sizes</p>
</div>

## Objective

The goal of Badux is to control more *area* than your opponent. Area consists of empty cells that
your stones surround, plus your living stones on the board.

## Basic Play

### Taking Turns

Black plays first, then players alternate placing one stone at a time on any empty cell of the
board. Once placed, stones do not move. A player may also choose to pass instead of placing a
stone.

<div style="text-align: center;">
  <img src="/img/rules/rules-opening-moves.png" alt="Opening moves">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">First seven moves of a game. It's White's turn.</p>
</div>

Early moves typically establish positions in the corners, since these are the easiest places to
control area.

### Groups and Connections

On a hex board, each cell has up to six neighbors.

<div style="text-align: center;">
  <img src="/img/rules/rules-single-stone-neighbors.png" alt="Single stone neighbors">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A single-stone group with six neighbors</p>
</div>

Stones of the same color that occupy adjacent cells are connected and form a *group*. This group
has fifteen neighbors:

<div style="text-align: center;">
  <img src="/img/rules/rules-connected-group.png" alt="Connected group">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A six-stone group with fifteen neighbors</p>
</div>

### Liberties

A *liberty* is an empty cell adjacent to a stone or group. Liberties represent the "breathing room"
for your stones. Every neighboring point that is unoccupied is a liberty. So the groups in the
previous section have 6 and 15 liberties, respectively. If we begin to surround the groups with
White stones, they now have 2 and 3 liberties, respectively:

<div style="text-align: center;">
  <img src="/img/rules/rules-single-stone-liberties.png" alt="Single stone liberties">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A single-stone group with two remaining liberties</p>
</div>

<div style="text-align: center;">
  <img src="/img/rules/rules-liberties.png" alt="Liberties">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A six-stone group with three remaining liberties</p>
</div>

### Capture

When a stone or group has no liberties remaining (all adjacent cells are occupied by enemy stones),
it is *captured* and removed from the board. The captured stones become prisoners.

When the Black group has one remaining liberty, it is said to be in *atari*, and can be captured on
the next turn if Black doesn't respond.

<div style="text-align: center;">
  <img src="/img/rules/rules-capture-atari.png" alt="Capture atari">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A six-stone group in atari</p>
</div>

White plays another stone, removing the group's last liberty:

<div style="text-align: center;">
  <img src="/img/rules/rules-capture-play.png" alt="Capture play">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White removes the group's last liberty</p>
</div>

The Black group is removed from the board as part of White's turn:

<div style="text-align: center;">
  <img src="/img/rules/rules-capture-after.png" alt="Capture after">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">The six-stone Black group is captured</p>
</div>

### Self-Capture (Suicide)

You may not place a stone in a cell where it would have no liberties, unless doing so captures
enemy stones. In other words, suicide is not allowed—you cannot remove your own stones by playing
into a position with no liberties.

<div style="text-align: center;">
  <img src="/img/rules/rules-suicide-illegal.png" alt="Suicide illegal">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White plays an illegal self-capture move</p>
</div>

However, if placing a stone would capture enemy stones and thereby create liberties for your stone,
the move is legal. The enemy stones are removed first.

<div style="text-align: center;">
  <img src="/img/rules/rules-capture-not-suicide-before.png" alt="Capture not suicide before">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">Here, White's move is legal, because it takes away the Black group's last liberty</p>
</div>

<div style="text-align: center;">
  <img src="/img/rules/rules-capture-not-suicide-after.png" alt="Capture not suicide after">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">The Black group is captured</p>
</div>

## Life and Death

### Two Eyes

A group is *alive* (cannot be captured) if it contains two separate internal liberties called
*eyes*. An eye is an empty cell completely surrounded by stones of one color.

<div style="text-align: center;">
  <img src="/img/rules/rules-two-eyes.png" alt="Two eyes">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A group with two eyes is alive</p>
</div>

If a group has only one eye, the opponent can eventually fill in all external liberties and then
capture the group by playing in the eye.

<div style="text-align: center;">
  <img src="/img/rules/rules-one-eye-dead.png" alt="One eye dead">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White can play in the middle to capture the one-eyed group</p>
</div>

### Seki (Mutual Life)

Sometimes two opposing groups share liberties in such a way that neither player can capture the
other without losing their own group. This situation is called *seki* (mutual life). Both groups
are considered alive, and the shared liberties score for neither player.

There are two common types of seki:

**One-eye seki:** Each group has one eye, and they share one dame point between them. Neither
player can fill the dame without reducing their group to one liberty, allowing the opponent to
capture.

<div style="text-align: center;">
  <img src="/img/rules/rules-seki-one-eye.png" alt="Seki one eye">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">If either player plays at A, they will be captured</p>
</div>

**No-eye seki:** Neither group has eyes, but they share two dame points between them. If either
player fills one of the dame, the opponent fills the other and captures.

<div style="text-align: center;">
  <img src="/img/rules/rules-seki-no-eyes.png" alt="Seki no eyes">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">If either player plays at A or B, they will be captured</p>
</div>

### Living Shapes

A living shape is a shape where the player will be able to form two eyes, even if their opponent
gets to play first. Identifying living shapes takes some skill and experience. Here are some
examples:

<div style="text-align: center;">
  <img src="/img/rules/rules-living-shape-1.png" alt="Living shape 1">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">If White plays A, Black plays B to live. And vice-versa.</p>
</div>

<div style="text-align: center;">
  <img src="/img/rules/rules-living-shape-2.png" alt="Living shape 2">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">If White plays A, Black must play B to live. And vice-versa.</p>
</div>

<div style="text-align: center;">
  <img src="/img/rules/rules-living-shape-3.png" alt="Living shape 3">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">Black can play at A, B, C, or D at any time to live.</p>
</div>

## End of the Game

The game ends when both players pass consecutively. This typically happens when neither player
believes they can gain more territory or capture more stones.

### Scoring (Chinese Rules)

Badux Go uses area scoring (Chinese rules). Your score is your *area*: your living stones,
plus the empty cells you surround, plus any dead opponent stones still on the board. The player with
the higher score wins.

<div style="text-align: center;">
  <img src="/img/rules/rules-scoring-example.png" alt="Scoring example">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White has 98 points of area, and Black has 71</p>
</div>

### Komi

To compensate for Black's first-move advantage, White receives extra points called *komi*. Badux Go
uses 6.5 points of komi, adopted from traditional Go. This seems to work well so far, but may be
adjusted as more games are played.

The half point is to avoid ties. In the above example, White has 98 points of area + 6.5 points
komi = 104.5 points, and Black has 71 points. White wins by 33.5 points.

### Dame

*Dame* (neutral points) are empty cells that border both Black and White territory. These cells
score for neither player and are typically filled in at the end of the game before final scoring.

## Summary of Rules

1. Black plays first; players alternate turns
2. On your turn, place one stone on any empty cell, or pass
3. Stones of the same color in adjacent cells are connected
4. A stone or group with no liberties is captured and removed
5. You may not play a stone that would have no liberties (unless it captures)
6. The game ends when both players pass
7. Score = your area (stones on board + empty cells you surround)
8. Highest score wins (White adds komi)

---

## Differences from Regular Go

If you're already familiar with Go, here's what's different about Badux:

### No Hanes

Perhaps the biggest difference between Badux and traditional Go is that there are no hanes. On a
square board, players can hane or sometimes make a one-space jump to get ahead of their opponent,
or cut them off, in a crawling race.

On a square board, a 3-3 invasion of a 4-4 corner typically leads to an even result. If Black opens
4-4, White can easily invade at the 3-3 and live. But White only has so much territory, and Black
gains a lot of influence towards the center.

<div style="text-align: center;">
  <img src="/img/rules/rules-no-hanes-1.png" alt="No hanes 1">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White lives in the corner after a 3-3 invasion</p>
</div>

On a hex board, the 3-3 invasion can live a lot larger, since Black cannot hane to contain the
group in the corner.

<div style="text-align: center;">
  <img src="/img/rules/rules-no-hanes-2.png" alt="No hanes 2">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White's 3-3 invasion is already alive after playing 4 stones.</p>
</div>

<div style="text-align: center;">
  <img src="/img/rules/rules-no-hanes-2b.png" alt="No hanes 2b">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">White gets to play away once and still survive</p>
</div>

On a square board, a 2-2 invasion of a 3-3 opening cannot live. A 2-2 invasion can live on a hex
board, but is probably ill advised, because it gives away too much influence:

<div style="text-align: center;">
  <img src="/img/rules/rules-no-hanes-3.png" alt="No hanes 3">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">A 2-2 invasion lives with five stones, but gives away too much influence</p>
</div>

This suggests that a 4-4 opening on a hex board is sub-optimal, and a 3-3 opening is probably
stronger on a hex board than on a square one.

### No Cuts

On a square Go board, a diagonal relationship between two stones can be "cut" by an opponent's
stone. On the hex board, there are no diagonals—connectivity is unambiguous. Two stones are either
adjacent (connected) or they're not.

<div style="text-align: center;">
  <img src="/img/rules/rules-no-cuts.png" alt="No cuts">
  <p style="font-size: 0.75rem; color: #666; margin-top: 0.25rem;">Cutting fights like this are not possible on a hex board</p>
</div>

### No Simple Kos

The ko rule exists in Go to prevent infinite loops: you cannot immediately recapture a single stone
that was just captured. In Badux, the geometry of the hex board means that simple ko situations
(single-stone back-and-forth captures) cannot occur. The superko rule (no repeating any previous
board position) still applies for theoretical edge cases, but in practice, you won't encounter ko
fights in Badux.

---

**Ready to play?** Visit [BaduxGo.com](https://baduxgo.com) to start a game, or
[watch the tutorial video](https://www.youtube.com/watch?v=oiq48v0W3WY) for a visual introduction.
