# Galhoom Labs — organization meta

> Powers the [org homepage](https://github.com/galhoom-labs) and the **canonical product rules**.

## What’s here

| Path | Role |
|:---|:---|
| [`profile/README.md`](./profile/README.md) | Org profile (rendered on [github.com/galhoom-labs](https://github.com/galhoom-labs)) |
| [`GITHUB_SURFACES.md`](./GITHUB_SURFACES.md) | Org + personal surface rules — **read before editing faces** |
| [`labs-registry.json`](./labs-registry.json) | Source of truth for product categories and product repos |
| [`AGENTS.md`](./AGENTS.md) | Rules for AI / maintainers placing new Labs repos |
| [`scripts/validate_labs.py`](./scripts/validate_labs.py) | CI check: registry ↔ profile stay aligned |

## Promise

```text
galhoom-path  = Learn & grow (practice / applied projects)
galhoom-labs  = Real products people can use
```

## Categories (do not invent a 4th casually)

```text
1 Apps → 2 Tools & extensions → 3 More products
```

## Validate locally

```bash
python scripts/validate_labs.py
```

Maintainer: [@Galhoom22](https://github.com/Galhoom22)
