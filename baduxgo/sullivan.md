---
layout: default
title: Meet John Sullivan, the Creator of Badux
---

<img src="/img/sullivan.jpg" alt="John Sullivan" style="float: right; max-width: 35%; height: auto; margin: 0 0 1rem 1.5rem; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />

# Meet John Sullivan, the Creator of Badux

When I was a kid, the first job I ever wanted was to make computer games. I
remember designing games in detail on a pad of graph paper. One game idea that I
was most passionate about, I called _Roscoe's Games_, which was to offer a
variety of novel card games and puzzles for the user to work through.

I did end up writing software for a living, but I wasn't writing games. I spent
time coding for genomics researchers, medical researchers, marketing, retail,
and insurance companies, among others. Because I was never terribly passionate
about the _what_ I was coding about, I focused in on something that I _was_
passionate about: software engineering. I voraciously taught myself about good
software engineering process and practices. And now that I have some freedom to
return to my passion for games, and game design and implementation, I can apply
all the software engineering knowledge I have accumulated to my new-found
passion.

## Game Variations

<div style="float: right; max-width: 20%; margin: 0 0 1rem 1.5rem;">
  <img src="/img/high-spades.jpg" alt="High spades cards" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
  <p style="font-size: 0.75rem; color: #7f8c8d; margin-top: 0.3rem; text-align: center;"><a href="https://commons.wikimedia.org/wiki/File:Black_Maria-penalty_cards-spades-IMG_6001.jpg" target="_blank" style="color: #7f8c8d;">Wikimedia Commons</a> (public domain)</p>
</div>

One game that I have always loved is the card game called Hearts. A friend of
the family taught us when I was a young teen, but it was really in college that
I started playing seriously. Hearts has a lot of variations, but one of the
rules that is almost always included is: You cannot play the Queen of Spades on
the first trick. The queen is half of the points of a hand, and you don't want
points, so dropping a queen on the first trick was a cold shot and a surprise.
Too much for the vast majority of hearts players, but for my friend circle in
college, it added an extra spice to an already volatile and unpredictable game.

I've played Hearts on a lot of game servers over the years, but I have never
found a server that supported playing the Queen on the first trick. Game
variations are typically kept to a minimum. One server might offer the option of
-10 for the Jack of Diamonds, but sometimes people play with the Jack at -11.
I've never seen a server that supported both. Time per move is hardcoded. Other
variations we played in college, such as three-person or five-person, are just
not supported.

Honestly, for decades, I've wanted to write a Hearts server that supported all
kinds of game variations, including dropping the Queen on the first trick. And
maybe I'll still get the chance!

## Why Badux?

<div style="float: right; max-width: 20%; margin: 0 0 1rem 1.5rem;">
  <img src="/img/goseigen.png" alt="Go game position" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
  <p style="font-size: 0.75rem; color: #7f8c8d; margin-top: 0.3rem; text-align: center;"><a href="https://commons.wikimedia.org/wiki/File:Iwamoto_Kaoru_vs_Go_Seigen_-_d%C3%A9cembre_1952_-_coups_1_%C3%A0_37.png" target="_blank" style="color: #7f8c8d;">Wikimedia Commons</a> (public domain)</p>
</div>

I've been playing the game of Go for over a decade now. I'm not good, but I love
to play, and I love to watch and learn. It's such an amazingly rich game. Its
rules are so simple and elegant, there simply is not a lot of room for tasteful
game variations. Unless, unless... Unless maybe you started messing with the
game topology itself! As a kid, I used to love hex graph paper, and all kinds of
games that were played on a hex board, rather than a standard square board
layout. When I came up with the idea of playing Go on a hex board, it seemed
really interesting to me. But it was over a year before I decided to go ahead and
write it.

I started with a proof-of-concept (PoC) — the most basic implementation I could
have that would allow me to play games against myself. First and foremost, I
needed to know if the game play would work. Once it was written, I played many
games against myself, to see how the game play felt, and to make sure there
weren't any awkward spots. It felt right, so I started working on my MVP, or
minimum viable product. This is the minimum feature set that I would need to get
people to play.

When I released my MVP in September this year, I expected to find a lot of bugs
coming to the surface. And that did happen. But a lot of other, more subtle
usability problems came up as well. Things that I really want to fix before I
start investing in marketing or advertising. For instance, I originally
envisioned people creating an account in order to play games. Now, just a couple
weeks after my initial release, it is crystal clear that I need to lower the
barrier of entry as low as possible: There should be zero friction for a new
visitor to begin playing games. So I'm working on creating guest accounts at the
moment, which is a major undertaking.

## Software Engineering Philosophy

<div style="float: right; max-width: 20%; margin: 0 0 1rem 1.5rem;">
  <img src="/img/Agile_Project_Management_by_Planbox.png" alt="Agile development cycle" style="width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);" />
  <p style="font-size: 0.75rem; color: #7f8c8d; margin-top: 0.3rem; text-align: center;"><a href="https://commons.wikimedia.org/wiki/File:Agile_Project_Management_by_Planbox.png" target="_blank" style="color: #7f8c8d;">Wikimedia Commons</a> (CC BY-SA 3.0)</p>
</div>

Game variants are hard, because software is hard. It's easy to write that
initial version, but without proper care put into code cleanliness, testing, and
automation, every successive version becomes harder to maintain. Good
engineering practices take time and effort, and don't seem worth it in the early
days, when things are moving quickly. But development teams quickly find
themselves slowing down, and unable to go back and apply best practices without
big costs, that management is typically unwilling to pay. Until things come to a
crisis.

My software engineering philosophy is all about adopting best practices from the
very beginning, and continually throughout the life of the project. The upfront
cost, and ongoing costs, paid for establishing and maintaining best practices,
pays dividends going forward, as we are continuously able to be agile and
flexible as we add new features, and expand on existing ones.

Some key tenets of my software engineering philosophy include:

- [Agile development](https://agilemanifesto.org/)
- [Functional testing](https://www.ibm.com/think/topics/functional-testing)
- [High-coverage testing](https://en.wikipedia.org/wiki/Code_coverage)
- Automation
  - One-command builds and test suites
  - Automatic test coverage reports
  - [Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration): full build and test on every commit
  - [Cloud-native DevOps](https://www.bmc.com/blogs/cloud-native-devops/)
- [Clean code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
- [Functional and effectful programming](https://en.wikipedia.org/wiki/Functional_programming)
- [Domain Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)

Badux Go is still in its infancy, but by following these engineering principles,
we'll be building a platform that will remain flexible and robust enough to
support an ever widening variety of game variations.

---

**Want to connect?** [Join our Discord](https://discord.gg/99C5gcTcrw) or [play Badux Go](http://baduxgo.com)
