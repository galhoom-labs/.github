# Galhoom Labs

**Build and share useful things.**

This organization is for **real, usable work**: tools, CLIs, libraries, templates, and products that help people — even if you never follow Galhoom Path.

| This org IS | This org is NOT |
|---|---|
| Tools & CLIs | A study curriculum |
| Products people can use | Interview / DSA practice |
| *(Libraries & templates later)* | Track 1–5 learning repos |
| Real products / SaaS starters | Practice-only apps |

Learning roadmap lives in **[galhoom-path](https://github.com/galhoom-path)**.

```mermaid
flowchart TB
  LABS["🧪 galhoom-labs"]
  LABS --> T["1 · 🛠️ Tools & CLIs"]
  LABS --> LIB["2 · 📦 Libraries"]
  LABS --> TMPL["3 · 📋 Templates"]
  LABS --> PROD["4 · 🚀 Products"]
  T --> T1["Helpers · generators · bots"]
  LIB --> L1["Composer / npm / reusable packages"]
  TMPL --> M1["Generic starters for anyone"]
  PROD --> P1["Apps people deploy or use"]

  classDef org fill:#fce7f3,stroke:#be185d,color:#831843,stroke-width:2px
  classDef track fill:#ede9fe,stroke:#6d28d9,color:#4c1d95,stroke-width:2px
  classDef item fill:#ecfdf5,stroke:#047857,color:#064e3b,stroke-width:2px
  class LABS org
  class T,LIB,TMPL,PROD track
  class T1,L1,M1,P1 item
```

<div align="center">

**[Open galhoom-path →](https://github.com/galhoom-path)** · Learn and progress

</div>

**Promise in one line:** Path = learn. Labs = ship useful things.
