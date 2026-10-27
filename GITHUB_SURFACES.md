# Galhoom Labs GitHub surfaces — never break these

Canonical rules for **every** public GitHub face owned by [@Galhoom22](https://github.com/Galhoom22) / [galhoom-labs](https://github.com/galhoom-labs).  
Agents: read this **before** editing the Labs org profile, the Labs section of the personal profile, Labs repo About text, pins, or topics.

Learning / Path faces are governed by **[galhoom-path GITHUB_SURFACES.md](https://github.com/galhoom-path/.github/blob/main/GITHUB_SURFACES.md)**. Obey both when editing the personal profile.

---

## 1. Promise (non-negotiable)

| Org | Promise |
|:---|:---|
| **galhoom-path** | Learn and progress — practice / applied projects to grow |
| **galhoom-labs** | **Real products** people can use and benefit from |

Labs is **not** a curriculum. Path is **not** a product store.

---

## 2. Three layers (Labs)

| Layer | Job | Keep out |
|:---|:---|:---|
| **Personal profile** Labs section | Product promise + Labs Mermaid + Labs CTA | Study dashboards; Path curricula pasted under Labs |
| **Labs org homepage** [`profile/README.md`](./profile/README.md) | High-level product map + what belongs here | Lectures, how-to study essays, DSA/interview banks |
| **Each product repo** | Install, usage, docs, releases | Nothing that must live only on org/personal faces |

**Rule:** faces answer *what is this / can I use it / where next?* Depth lives **inside each repo**. Prefer cutting copy over adding sections.

---

## 3. Labs organization homepage (`profile/README.md`)

### Must keep

- Clear **real products** promise (usable by others)
- Explicit contrast with Path (learn / practice vs products)
- **Projects in this org** = real products (not practice exercises)
- Product category Mermaid (**same visual style**: `flowchart TB` + pink/purple/green `classDef`)
- Categories: **Apps** · **Tools & extensions** · **More products** (web/mobile/desktop, CLIs/extensions, games/other)
- Link back to Path for learning

### Must not

- List Path study tracks as Labs categories
- Add libraries / templates categories unless registry + human say so
- Turn the org page into a long product marketing essay
- Change Mermaid style casually (keep TB + classDef language)

---

## 4. Personal profile (`Galhoom22/Galhoom22`) — Labs half

Personal profile is a **two-home** page:

1. Path section — learn / practice (Path Mermaid + Path CTA)
2. Labs section — real products (Labs Mermaid + Labs CTA)

### Must keep (Labs half)

- Comparison that Path projects = practice; Labs projects = products
- Labs Mermaid matching the org Labs diagram
- One Labs CTA: open `galhoom-labs`

### Must not

- Remove Labs to satisfy outdated “single org CTA” wording in older Path notes — **two homes is intentional**
- Present Labs as a learning track
- Duplicate long org essays; keep overview only

---

## 5. Repo About descriptions & topics (Labs)

- Describe the **product** (what users get), not a study syllabus.
- Prefer topics like `cli`, `chrome-extension`, `mobile`, `game`, `saas`, `tool` over `tutorial` / `curriculum` / `interview`.
- Never invent category numbers from memory — use **`labs-registry.json`**.

---

## 6. Order of work when changing Labs surfaces

1. `labs-registry.json` first  
2. `profile/README.md` (keep it short)  
3. `python scripts/validate_labs.py`  
4. Update personal profile Labs section **only** if the diagram/promise would otherwise lie  
5. Fix product repo descriptions/topics if category labels changed  

---

## 7. Hard bans (Labs surfaces)

- No practice-only / “hands dirty to learn” repos as Labs products
- No Path curricula on the Labs org face
- No libraries/templates categories without explicit expansion
- No bloating org/personal READMEs “for completeness”
- No claiming shipped/finished without human confirmation in the registry


## Complement + refusal (Path ↔ Labs)

**galhoom-path** and **galhoom-labs** are complementary faces of one public brand:

1. People benefit as **developers** (Path — learn, practice, hands dirty).
2. People benefit as **users** (Labs — real products they can use).

Agents **must refuse** wrong-org placement and redirect:

- Learning / practice / interview / DSA → **galhoom-path**
- Real usable product → **galhoom-labs**

Do not silently put work in the wrong org to “just ship the ask.”
