---
layout: default
title: Hexagonal Thinking - The Philosophy Behind Badux Go
---

# Hexagonal Thinking: The Philosophy Behind Badux Go

## Baduk, Or Go

<div style="float: left; max-width: 30%; margin: 0 1.5rem 1rem 0;">
  <img src="/img/go-painting.png" alt="Historical painting of people playing Go" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
  <p style="font-size: 0.75rem; color: #7f8c8d; margin-top: 0.3rem; text-align: center;"><a href="https://commons.wikimedia.org/wiki/File:Emperor_Minghuang_and_Consort_Yang_Playing_Weiqi_1.png" target="_blank" style="color: #7f8c8d;">Wikimedia Commons</a> (public domain)</p>
</div>

The ancient game of [Go](https://senseis.xmp.net/) (known as Baduk in Korea and
Weiqi in China) is considered one of the most sublime, elegant, and inherently
complex games created by humankind. Two players take turns, placing black and
white game pieces of stone or glass onto a wooden board. The aim is to control
more territory than your opponent, but what kinds of configurations of pieces
actually control territory is an extremely nuanced and complex calculation. This
makes mastery of the game a lifelong journey, and every game played by two
players, an intricate conversation.

<div style="clear: both;"></div>

## Board Topology

The Go board is square. The full-sized, 19 by 19 point board, can seem imposing.
People often play on smaller boards, and historically, games are played almost
exclusively on square boards of one of the three traditional sizes:

- 9 by 9
- 13 by 13
- 19 by 19

Other board sizes are indeed possible, and are available to play on some Go
servers, but as far as I know, Go has been played almost exclusively on square
boards of these three sizes.

Other board topologies — where the points on the board are not arranged in a
square grid — are also possible. For instance, the board of Badux, which is hex
or honeycomb.

Not just any board topology will work well. But exploring what is possible, and
plays well, has been historically difficult. For one thing, variant boards would
have had to be individually crafted. Perhaps more importantly, finding opponents
to play on a variant board would have presented serious obstacles.

## A Simpler Game of Go

<div style="float: right; max-width: 25%; margin: 0 0 1rem 1.5rem;">
  <img src="/img/7-board.png" alt="Badux Go hexagonal board" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
</div>

Interestingly, some of the most complex aspects of strategy in the game of Go
depend on the square board topology: [hanes](https://senseis.xmp.net/?Hane),
[cuts](https://senseis.xmp.net/?Cut), and [kos](https://senseis.xmp.net/?Ko).
None of these are possible on a hex board, making Badux a simpler game.
Connectivity is easier to calculate. Perhaps the most daunting aspect of
learning to play Go is trying to understand if stones are actually connected,
and if they actually control territory.

**Badux provides an entry point into the game of Go that makes it easier to
understand and work with the basic principles of the game.** The hexagonal
topology reduces ambiguity in connections. Because of the density of the edges
connecting the points you play on, it's easier to reason about whether your
opponent can separate with an intervening stone. This clarity makes Badux an
excellent teaching tool for Go fundamentals, while still preserving the deep
strategic thinking that makes Go fascinating.

## Other Rule Variants

Because the rules of Go are so simple and elegant, it is hard to come up with
game variations that respect this elegance, and work. Go itself has different
rule sets, but most of the differences are logistical: How best to bring a game
to a close. These differences do not really affect game strategy. But perhaps
there are game variants other than board topology that are worth exploring.

Could we play a game of Go with three or four players? Three players on a square
board would not work well, because whoever played first would end up with one
more corner than the other two players. A Go variant called
[Rengo](https://senseis.xmp.net/?Rengo) allows for four-player game play, but it
is essentially the same game as Go, where you and your teammate take turns
playing moves for your team. It's not four players playing independently.

Four players would not work well on a hex board, because two of the players
would end up with an extra corner. But three would work, or even six.

## Variational Games

<div style="float: left; max-width: 20%; margin: 0 1.5rem 1rem 0;">
  <img src="/img/six-aces.jpg" alt="Six aces playing cards" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
  <p style="font-size: 0.75rem; color: #7f8c8d; margin-top: 0.3rem; text-align: center;">Deck6 from <a href="https://www.thegamecrafter.com/designers/shp-games" target="_blank" style="color: #7f8c8d;">SHP Games</a></p>
</div>

Online game play opens up a whole range of possibilities in strategic games that
were never possible before. Want to experiment with a new board shape? We can
accommodate that in software. Having trouble finding opponents to play the
variant you want to play? Online gaming platforms are open to the whole world.

Game variants are great. They bring new life to well-established patterns of
play. They open up your mind to new aspects of the game you've been playing for
years. One variant might be well suited for introducing a game to new players.
Another might be geared towards expert players, to stretch their skills in new
directions.

### The Technical Challenge

<div style="float: right; max-width: 35%; margin: 0 0 1rem 1.5rem;">
  <img src="/img/SelfCaptureSpec.png" alt="Self capture test specification" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
</div>

Software is often brittle, hard-coding assumptions about the game into the code
so deeply, that you would probably rather just start all over again if you
wanted to handle anything but the most trivial variants.
[OGS](https://online-go.com/) (Online Go Server) supports unusually-shaped, yet
still-square, boards, and Rengo. But more likely than not, no existing Go server
could support a non-trivial variant, such as four-player Go, or Go on a
hexagonal board. Even a rectangular board could be hard to support.

With Badux Go, I am applying my decades of experience in software engineering to
build a platform where new variants are anticipated, and easy to implement. This
strategy depends on a lot of fundamental aspects of software engineering that
are often overlooked, such as:

- **Automated testing** - Ensuring that new rule variants don't break existing functionality
- **Effectful programming** - Separating game logic from side effects to make the code more maintainable and testable
- **Modular design** - Building components that can be recombined in new ways

The hex board is just the start. But before I explore other variants, I have to
bring the server up to parity with features offered by other Go servers, such as
supporting different clocks and rulesets, player rankings, and tournaments.

### The Vision

The ultimate goal of Variational Games is to create a platform where the Go
community can experiment with variations that might have taken decades to
explore in the physical world. Some variants will be pedagogical tools. Some
will be aesthetic experiments. Some might reveal new strategic depths we never
imagined.

By making it easy to implement and play variants, we can accelerate the
exploration of this ancient game's possibility space. Hexagonal thinking is just
the beginning—it's a different way of seeing the same fundamental truths about
territory, influence, and connection that have captivated players for millennia.

---

**Ready to try it?** [Play Badux Go](http://baduxgo.com) or [learn more about the game](/baduxgo/).
