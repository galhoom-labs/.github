# Galhoom Labs — agent rules

This repository owns the **organization profile**, **labs registry**, and **surface rules** for **real products**.

## Read first

1. **[`GITHUB_SURFACES.md`](./GITHUB_SURFACES.md)** — org + personal faces (do not break).
2. **`labs-registry.json`** — product categories and repo IDs.
3. This file — placement and CI.
4. For learning / practice work, obey **[galhoom-path/.github AGENTS.md](https://github.com/galhoom-path/.github/blob/main/AGENTS.md)** instead — do **not** put Path work here.

## Profile surface rule (org + personal)

| Surface | Job | Keep out |
|:---|:---|:---|
| **Labs org homepage** (`profile/README.md`) | Promise + product map + links | Curricula, DSA drills, interview banks, practice-only builds |
| **Personal profile** (`Galhoom22/Galhoom22`) | Two homes: Path (learn) + Labs (products) | Student dashboards; treating Labs as a study track |
| **Each product repo** | Full product detail (README, install, usage) | Nothing required on the org face beyond the map |

**Rule:** org and personal profiles answer *what is this / can I use it / where do I go?* Full product docs live **inside each repo**. Prefer cutting copy over adding sections. When in doubt, link to the repo.

## Before you create or place any `galhoom-labs` repo

1. Read **`labs-registry.json`** (source of truth).
2. Confirm the pitch is **“use this”** (real product) — not **“study this / get your hands dirty”**.
3. Follow **`placement_algorithm`** and never violate **`forbidden`**.
4. Update **`labs-registry.json` first**, then **`profile/README.md`** (keep it short), then CI must pass (`python scripts/validate_labs.py`).
5. Mirror the Labs diagram / product wording on **`Galhoom22/Galhoom22`** when the personal profile would otherwise lie — still obey `GITHUB_SURFACES.md`.

## What belongs here (products)

A Labs repo is a **real product** someone can open, install, run, or otherwise use and get value from. Form examples:

- Websites / web apps
- Mobile apps
- Desktop applications
- Chrome (or other browser) extensions
- CLIs and helper tools people run
- Games
- Any other **usable** product form

Libraries and templates are **out of scope for now** unless the human explicitly expands the registry.

## What does NOT belong here

- Study curricula / lecture series
- Foundations notes as a learning track
- DSA gyms / LeetCode practice sets
- Interview answer banks
- **Practice / applied learning projects** whose goal is only growth (“get your hands dirty”)
- Anything whose primary pitch is *follow Galhoom Path*

Those stay in **[galhoom-path](https://github.com/galhoom-path)**.

## Categories (do not reorder casually)

```text
1 Apps → 2 Tools & extensions → 3 More products
```

IDs look like **`Category.Repo`** (example: **1.1** = first Apps product).

## Quick placement map

| If the new repo is… | Category | Next ID pattern |
|:---|:---:|:---|
| Web / mobile / desktop app people use | **1** Apps | `1.(N+1)` |
| CLI, browser extension, generator, bot, helper people run | **2** Tools & extensions | `2.(N+1)` |
| Game or other usable product that is not a clear App/Tool | **3** More products | `3.(N+1)` |

## Project vs Path practice (hard rule)

| | Path | Labs |
|:---|:---|:---|
| Project type | Practice / applied learning | Real product |
| Goal | Grow skills — hands dirty | Users get value |
| Mindset | *“I built this to learn.”* | *“I built this for people to use.”* |

A Path practice build may later graduate to Labs **only** when it becomes a real product people rely on. Do not duplicate the same canonical product repo in both orgs — one home, link from the other.

## Never

- **Refuse wrong-org placement** — if the human asks for Path work in Labs (or Labs work in Path), say no, explain the correct org, and offer to continue there.
- Put a learning / practice-only repo in Labs “because the org is empty”.
- Put a real public product in Path Track 5 — Track 5 is practice only.
- Add libraries or templates without an explicit human decision + registry update.
- Skip the registry and only edit the README.
- Bloat `profile/README.md` or the personal Labs section “for completeness”.
- Change the Labs Mermaid **style** (TB + classDef colors) without an explicit human request — content labels may update; visual language stays.
- Claim a product is finished/shipped without the human saying so (`status` in registry).

## How Path and Labs complete each other

| | **galhoom-path** | **galhoom-labs** |
|---|---|---|
| **Job** | Help people **grow as developers** | Help people **use real products** |
| **Projects** | Practice / applied learning | Real products |
| **Together** | One public brand: learn → then ship useful things |

They are **siblings**, not rivals. Path without Labs is only a classroom. Labs without Path loses the craft story. Both stay cross-linked.

### Agent refusal rule (mandatory)

If a human asks to put work in the **wrong** org:

1. **Say no** to the violating placement.
2. Say which org it belongs in and why (one short reason).
3. Offer to do it in the correct org instead.

Examples:
- “Add this Chrome extension under Path Track 5” → **No** — real product → **galhoom-labs**.
- “Add this DSA gym under Labs” → **No** — practice learning → **galhoom-path**.
- “Ship a market app as Path practice” → **No** — product home is **Labs**; Path may only link as a learning milestone if needed.

## CI

GitHub Actions runs **`Validate Galhoom Labs`** on changes to the registry or profile README. A red check means the map is wrong — fix registry + README until `python scripts/validate_labs.py` prints `OK`.
