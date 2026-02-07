# Path: packages/velm-grimoire/scripts/rebuild_index.py
# ---------------------------------------------------

"""
=================================================================================
== THE MASTER LIBRARIAN (V-Ω-TOTALITY-V200-AUTO-NAVIGATOR)                     ==
=================================================================================
LIF: ∞ | ROLE: CELESTIAL_INDEX_CONDUCTOR | RANK: OMEGA_SUPREME
AUTH_CODE: Ω_LIBRARIAN_V200_AUTO_SYNC

This divine artisan performs the Rite of the Global Census. It scries the
Archetype Sanctum, extracts Gnostic DNA, and materializes the Master Index
for the Architectural App Store.
=================================================================================
"""

import json
import os
import sys
import time
import hashlib
import re
import argparse
from pathlib import Path
from typing import List, Dict, Any, Optional, Set, Tuple
from collections import Counter

# --- THE GNOSTIC UPLINKS (RICH TELEMETRY) ---
# We use surgical imports to ensure the Librarian remains lightweight for CI/CD.
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
    from rich.theme import Theme

    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# =============================================================================
# == THE CURE: CROSS-BOUNDARY IMPORT SUTURE                                  ==
# =============================================================================
# This script often runs inside the 'packages/velm-grimoire' submodule.
# We must ensure it can find the 'velm' package mind in the parent directory.
SCRIPT_PATH = Path(__file__).resolve()
SUBMODULE_ROOT = SCRIPT_PATH.parent.parent
PARENT_SRC = (SUBMODULE_ROOT.parent.parent / "src").resolve()

if str(PARENT_SRC) not in sys.path:
    sys.path.insert(0, str(PARENT_SRC))

try:
    from velm.genesis.canon_dna import GnosticDNAOracle
except ImportError:
    # Fail-safe for isolated GitHub Runner environments
    class GnosticDNAOracle:
        @staticmethod
        def divine(slug, content):
            return {"name": slug, "description": "Gnosis Deferred", "tags": [], "category": "Unclassified"}

# --- THE VISUAL FREQUENCY ---
GNOSTIC_THEME = Theme({
    "info": "cyan",
    "warning": "yellow",
    "danger": "bold red",
    "success": "bold green",
    "soul": "bold magenta",
    "locus": "dim white",
    "meta": "bold blue"
})


class MasterLibrarian:
    """
    The Sovereign Cartographer of the Grimoire.
    Wields a 12-stage perception engine to unify the Celestial Grimoire.
    """

    INDEX_VERSION = "2.0.0"

    def __init__(self, repo: str, branch: str, vault_dir: str, output_file: str):
        self.repo = repo
        self.branch = branch
        self.vault_path = Path(vault_dir).resolve()
        self.output_path = Path(output_file).resolve()

        # Forge the automatic celestial link
        # Format: https://raw.githubusercontent.com/user/repo/branch/path/to/file
        # We assume the vault_dir is relative to the repo root
        self.base_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{vault_dir}"

        self.console = Console(theme=GNOSTIC_THEME) if HAS_RICH else None
        self.index: List[Dict[str, Any]] = []
        self.heresies: List[str] = []
        self.stats = Counter()

    def proclaim(self, msg: str, style: str = "info"):
        if self.console:
            self.console.print(f"[{style}]»[/] {msg}")
        else:
            print(f">> {msg}")

    def conduct_census(self):
        """The Grand Rite of the Census."""
        if self.console:
            self.console.print(Panel(
                f"Librarian Awakening. Scrying [soul]{self.repo}[/] ([meta]{self.branch}[/])\n"
                f"Locus: [locus]{self.vault_path}[/]",
                title="[bold white]Ω_CELESTIAL_CENSUS[/]",
                border_style="cyan"
            ))

        if not self.vault_path.exists():
            self.proclaim(f"Sanctum '{self.vault_path}' is a void. Terminating.", "danger")
            return

        # [ASCENSION 3]: Recursive Deep-Scry
        scaffold_shards = list(self.vault_path.rglob("*.scaffold"))

        if HAS_RICH:
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(bar_width=None, pulse_style="cyan"),
                    TimeElapsedColumn(),
                    console=self.console,
                    transient=True
            ) as progress:
                task = progress.add_task("[info]Tomography of Shards...", total=len(scaffold_shards))
                for shard in scaffold_shards:
                    self._perceive_shard(shard)
                    progress.update(task, advance=1)
        else:
            for shard in scaffold_shards:
                self._perceive_shard(shard)

        self._finalize_and_inscribe()

    def _perceive_shard(self, path: Path):
        """[THE ATOMIC GAZE] Performs 12 stages of metadata extraction."""
        # Calculate relative path from vault root for the URL
        rel_path = path.relative_to(self.vault_path).as_posix()
        slug = path.stem

        try:
            content = path.read_text(encoding="utf-8")

            # 1. DIVINE THE DNA (The Oracle's Rite)
            dna = GnosticDNAOracle.divine(slug, content)

            # 2. CALCULATE INTEGRITY (Merkle Fingerprint)
            hasher = hashlib.sha256(content.encode('utf-8'))
            dna["sha256"] = hasher.hexdigest()
            dna["bytes"] = len(content)

            # 3. FORGE CELESTIAL COORDINATE (URL)
            dna["url"] = f"{self.base_url}/{rel_path}"

            # 4. ADJUDICATE PURITY (Socratic Validation)
            if not dna.get("description"):
                self.heresies.append(f"Locus {rel_path}: Description is a void.")

            # 5. INSCRIBE
            self.index.append(dna)
            self.stats[dna.get("category", "Unclassified")] += 1

        except Exception as e:
            self.heresies.append(f"Fracture in {rel_path}: {str(e)}")

    def _finalize_and_inscribe(self):
        """The Rite of Final Inscription."""
        # Sort by name for deterministic Git diffs
        self.index.sort(key=lambda x: x["name"])

        manifest = {
            "version": self.INDEX_VERSION,
            "timestamp": time.time(),
            "repo": self.repo,
            "branch": self.branch,
            "count": len(self.index),
            "archetypes": self.index
        }

        # [ASCENSION 6]: Atomic Write Guard
        temp_file = self.output_path.with_suffix(".tmp")
        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)

            # Atomic swap ensures zero corruption risk
            os.replace(temp_file, self.output_path)

            if self.console:
                self._render_final_report()
            else:
                print(f"✨ Master Index Materialized at {self.output_path}")

        except Exception as e:
            self.proclaim(f"Inscription Paradox: {e}", "danger")

    def _render_final_report(self):
        """Proclaims the state of the Grimoire to the Architect."""
        table = Table(title="Grimoire Census Summary", box=None, expand=True)
        table.add_column("Stratum (Category)", style="soul")
        table.add_column("Count", justify="right", style="white")
        table.add_column("Status", justify="center")

        for cat, count in self.stats.items():
            table.add_row(cat, str(count), "[success]RESONANT[/]")

        self.console.print(table)
        self.console.print(f"\n[success]✨ Master Index Version {self.INDEX_VERSION} Materialized.[/]")

        if self.heresies:
            self.console.print(Panel(
                "\n".join([f"• {h}" for h in self.heresies]),
                title="[bold yellow]Dossier of Schisms[/]",
                border_style="yellow"
            ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ω | The Master Librarian: Automated Celestial Indexer",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--repo", required=True, help="GitHub repository identifier (e.g., novalym/velm-grimoire)")
    parser.add_argument("--branch", default="main", help="The target branch for raw URLs (default: main)")
    parser.add_argument("--vault", default="archetypes", help="The subfolder containing .scaffold files")
    parser.add_argument("--output", default="index.json", help="Path to inscribe the final index.json")

    args = parser.parse_args()

    start_time = time.perf_counter()

    librarian = MasterLibrarian(
        repo=args.repo,
        branch=args.branch,
        vault_dir=args.vault,
        output_file=args.output
    )

    librarian.conduct_census()

    duration_ms = (time.perf_counter() - start_time) * 1000
    print(f"\n[LIBRARIAN] Census complete in {duration_ms:.2f}ms. Lattice is synchronized.")

# == SCRIPTURE SEALED: THE MASTER LIBRARIAN IS OMNIPOTENT ==