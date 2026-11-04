# cli-tools-learning

Personal learning repository for command-line tools, with versioned practice material on dedicated branches.

Exercises are tracked in [ankify](https://github.com/WSmithDR/ankify). Practice branches are stable starting points: they are never merged or deleted.

## Tools

| Tool | Deck | Status |
|---|---|---|
| pdfinfo | Current::Programación de Sistemas::Terminal | Ready on pdf-samples |

## What lives here

| Material | Branch | File |
|---|---|---|
| PDF inspection and conversion | pdf-samples | muestras/FESD_Recopilatorio_Unidad_1.pdf |

The PDF is a byte-for-byte copy of the document supplied by the user. It has 34 pages and is used as fixed input, not as an exercise solution. Keep it unchanged so future reviews remain reproducible. The pdfinfo executable must already be installed.

## Criteria for a tool to live here

A tool belongs in this repo when its exercises are **command-based** — no source files to build or commit between features. If a tool requires a real project with files (GitHub Actions, Docker Compose, etc.), it gets its own dedicated repo.
