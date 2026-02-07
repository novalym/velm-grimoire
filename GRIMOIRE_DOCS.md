# =================================================================================
# == THE CONSTITUTION OF THE GRIMOIRE (V-Ω-TOTALITY)                            ==
# =================================================================================
# LIF: ∞ | ROLE: ARCHITECTURAL_LAW | RANK: OMEGA_SUPREME
# AUTH_CODE: Ω_GRIMOIRE_2026_FINALIS
# =================================================================================

## I. THE PHILOSOPHY OF THE FORGE

The **Velm Grimoire** is the sovereign repository of architectural DNA. It is built upon the **Quadratic Strategy**: a unified system where human intent is distilled into `.scaffold` shards, automatically indexed by a **Celestial Scribe**, and streamed to clients across the multiverse.

Its purpose is to **Annihilate Technical Entropy**. By enshrining perfected patterns here, we ensure that every new reality born from Velm is "Titanium Stable" from the first microsecond of its inception.

---

## II. THE ANATOMY OF A SHARD (.scaffold)

Every file in the `archetypes/` directory is a **Shard of Form**. To be manifest in the **Master Index**, a shard must follow the **7-Pillar Header Protocol**.

### 1. The Gnostic Header
```scaffold
# =================================================================================
# == GNOSTIC ARCHETYPE: [LUMINOUS NAME] (V-Ω-TOTALITY)                           ==
# =================================================================================
# @description: [A powerful, single-sentence summary of the intent.]
# @category: [Backend | Frontend | Infrastructure | Intelligence | System | Meta]
# @tags: [comma, separated, semantic, keywords]
# @difficulty: [Novice | Adept | Master | Grand Architect]
# @is_integration: [true | false]
# @dna: key=val, key2=val2  # Gnostic Overrides for the Engine
# =================================================================================

2. The Internal Logic

    The Cloaking Ritual: Use \"\"\" for all nested Python docstrings. The engine's Backslash Healing faculty will restore them to pure matter during materialization.

    Duality of Naming: Use {{ project_slug }} for kebab-case (Files/Folders) and {{ package_name }} for snake_case (Python Logic).

    The Maestro's Will: Every shard should include a %% post-run block for cinematic guidance and an %% on-heresy block for transactional safety.

III. THE CELESTIAL SCRIBE (Automation)

The repository is a Self-Indexing Intelligence. You never manually update the index.json.
1. The Rite of the Push

When you push to the main branch, the .github/workflows/ascension.yml scripture awakens:

    Materialization: Summons a Python 3.11 environment.

    Inquest: Scans every shard for header purity.

    The Census: Runs scripts/rebuild_index.py to forge a new index.json.

    Inscription: Performs a git commit --amend to surgically update the index and force-pushes it back to the chronicle.

2. The Resulting Artifact

The final index is available via the Celestial Coordinate:
https://raw.githubusercontent.com/novalym/velm-grimoire/main/index.json
IV. MAINTENANCE & HEALING
1. Adding a New Shard

    Forge a new .scaffold file in the appropriate sub-sanctum (e.g., archetypes/backend/).

    Inscribe the 7-Pillar Header.

    git add . -> git commit -m "feat(shard): manifest [name]" -> git push.

    Watch the GitHub Actions Ocular HUD for the green seal of success.

2. Healing a Schism

If a push fails the Inquest:

    Identify the fractured file in the GitHub Actions log.

    Correct the header (usually a missing @description or @category).

    Re-push. The Scribe will automatically attempt the ascension again.

3. Manual Census (Local Testing)

If you wish to prophesy the index before pushing:
code Bash

# Ensure dependencies are manifest
pip install -r requirements.txt

# Run the Librarian
python scripts/rebuild_index.py --repo novalym/velm-grimoire

V. THE FINALITY VOW

The Grimoire is the foundation of Novalym Systems. Its growth is our growth. Every shard willed into this sanctum makes the next creation faster, safer, and more profound.

Guard the Purity of the Header. Honor the Law of the Suture. Manifest the Future.

««« SCRIPTURE SEALED // OMEGA TOTALITY »»»