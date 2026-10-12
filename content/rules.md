+++
title = "Rules of war"
description = "How a battle works, in full: turns, funds, movement, combat, capturing, supply, fog, weather and commander powers."
template = "wiki-page.html"
+++

Paw & Claw follows the rules of *Advance Wars 2: Black Hole Rising* and *Advance Wars: Dual
Strike*. If a rule isn't covered here, it works the way it does there. The numbers below come
straight from the game's data files and code.

## Winning

A battle ends when one army is left. You beat an enemy army by **capturing its headquarters**
(the [Base](/terrain/#base)) or by **destroying every one of its units**.

## A day of battle

Armies take turns, and a full round of turns is a **day**. Each turn opens with a banner
showing the day and the commander, and then, in this order:

1. **Income.** You get the funds of every property you own.
2. **Repair and resupply.** Units on your own properties heal and refill (see
   [supply](#repair-and-resupply)).
3. **Upkeep.** Fliers and boats burn their daily stamina and are lost at zero.
4. **Weather** may change (see [weather](#weather)).

Then you give orders: every unit can act once. Turns end only when you choose **End turn**
in the map menu.

## Funds and building

Every property pays **1,000 funds a day** to its owner; some commanders change that. Spend
funds at the properties that build:

| Property | Builds |
|---|---|
| [Workshop](/terrain/#workshop) | Ground units: foot soldiers, vehicles and caravans |
| [Dock](/terrain/#dock) | Boats |
| [Roost](/terrain/#roost) | Fliers |

As in Advance Wars, the HQ doesn't build anything. A unit built this turn can't move until
your next turn, and a building can't produce while a unit stands on it. Prices are on each
[unit's page](/units/).

## Movement

Each unit has **movement points** and each tile costs some of them to enter, depending on the
unit's movement class (the full table is on the [terrain](/terrain/#movement) page). Trails
cost 1 for everything that walks or rolls; thickets slow vehicles; brambles and boulders let
only foot soldiers through; water is for boats.

- Units can pass through friendly units but not stop on them, with two exceptions:
  - **Joining.** Move onto a unit of the same type when at least one of the two is wounded,
    and they merge into one. Health over 10 is refunded as funds.
  - **Boarding.** Move a unit onto a friendly transport that can carry it.
- Units can't pass through enemies.
- Moving uses **stamina**, one point per movement point spent.

## Combat

A unit can attack after moving if it's a **direct** unit (range 1, it hits neighbours), or
instead of moving if it's an **indirect** unit (range 2 or more, like the Catapult or
Trebuchet). Indirect units can never move and fire in the same turn.

### Damage

Damage follows the Advance Wars 2 formula, in percent of the target's health, rounded down:

<div class="formula">Damage = (B × ACO / 100 + L) × AHP / 10 × (200 − (DCO + DTR × DHP)) / 100</div>

| Term | Meaning |
|---|---|
| **B** | Base damage of the attacker's weapon against that target (see the [damage chart](/damage/)) |
| **ACO** | Attacker's firepower: 100, plus commander and power bonuses |
| **L** | Luck: a random 0 to 9 by default; some commanders roll more, or roll bad luck too |
| **AHP** | Attacker's displayed health, 1 to 10 |
| **DCO** | Defender's defense: 100, plus commander and power bonuses |
| **DTR** | Defense stars of the defender's tile (0 for fliers) |
| **DHP** | Defender's displayed health, 1 to 10 |

**Example.** A full-health Militia attacks a full-health Militia on grass (1 star):
B = 55, so (55 + L) × 10/10 × (200 − (100 + 1 × 10)) / 100 = (55 + L) × 0.9. That is **49%
to 57%** depending on luck: the target drops to 5 or 6 health. Hurt attackers hit softer, and
cover protects a healthy defender more than a wounded one.

Weather never changes damage.

### Counterattacks

If the defender survives and the attacker is within its range, it strikes back at once, with
its reduced health. Indirect units can't fire at neighbours, so they never answer a direct
attack, and an indirect attacker is usually out of reach of what it hits: that's what makes
catapults and trebuchets so strong.

### Weapons and ammo

Many units carry two weapons. The **primary** weapon (bows, lances, catapult stones) uses
ammo; the **secondary** (blades and the like) never runs out. A unit out of ammo falls back on
its secondary weapon, or can't attack at all if it has none. Each unit's page lists both.

## Terrain cover

Every tile has **defense stars**, from 0 (trails, water, shores) to 4 (brambles, boulders and
the HQ). In the formula each star takes off 1% per point of the defender's health, so a
full-health unit on four stars takes 40% less damage. Fliers never get cover. See
[terrain](/terrain/) for every tile.

## Capturing

Only foot soldiers ([Militia](/units/scout/) and [Halberdiers](/units/shocktrooper/)) can
capture. Every property has **20 capture points**; each turn a capturing unit removes as many
as its displayed health (a full-health unit takes two turns). If it leaves the tile or is
destroyed, the capture resets. Capturing the enemy HQ wins the battle.

## Repair and resupply

At the start of your turn, after income, each unit on one of your properties that serves its
kind (workshops, outposts, storehouses and the HQ serve ground units; docks serve boats;
roosts serve fliers):

- heals **2 health**, paying **10% of the unit's price per health point**, as far as your funds
  go, and
- refills its ammo and stamina for free.

A [Supply Cart](/units/supplier/) refills the ammo and stamina of the units next to it at the
start of your turn.

## Stamina

Stamina is Advance Wars' fuel. Moving spends it, and a unit can never move further than its
stamina allows. **Fliers and boats also burn some every day**, even standing still; when it
reaches zero they crash or sink. Daily burn is on each unit's page.

## Transports

[Caravans](/units/carrier/), [Skyferries](/units/ferrier/) and [Rafts](/units/barge/) carry
other units. Move a unit onto a friendly transport to board it, move the transport, then unload
onto a neighbouring tile. A transport that is destroyed takes its passengers with it.

## Fog of war

With fog of war on, you only see the tiles your units can see (each unit's **vision** is on its
page). **Thickets** and **lily pads** hide the units in them from everything but their direct
neighbours. If you move into a hidden enemy, your unit stops short in front of it: a **trap**,
and its turn is over.

## Weather

Weather can change at the start of a turn (a 20% chance each day). Its effects:

| Weather | How often | Effect |
|---|---|---|
| Clear | 50% | None |
| Rain | 15% | −1 vision |
| Snow | 10% | −1 movement |
| Sandstorm | 10% | −2 vision |
| Dense fog | 15% | Vision at most 1 |

Some commanders ignore weather, and some powers call it in. Weather never changes damage.

## Commanders and powers

Each army is led by one of 28 [commanders](/commanders/). A commander's **always-on
abilities** apply all battle. Two powers wait in the **power meter**:

- The meter fills when units lose health: the army that took the hit gets the full funds value
  of the health lost, the army that dealt it half.
- A **star** of the meter costs 9,000 funds of damage. Each time a commander uses a power,
  their stars cost 20% more, up to three times the price.
- A **CO Power** needs its stars (usually 3 or 4); the **Super CO Power** needs more (usually 6
  to 9) and is stronger. The meter holds up to the Super CO Power, and stops filling while a
  power runs.
- A power lasts until your next turn. On top of its own effect, **either power gives every unit
  +10% attack and +10% defense**.
