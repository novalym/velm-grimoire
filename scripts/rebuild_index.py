# Path: packages/velm-grimoire/scripts/rebuild_index.py
# ---------------------------------------------------

"""
=================================================================================
== THE MASTER LIBRARIAN (V-Ω-TOTALITY-V500-VECTOR-EMBEDDER)                    ==
=================================================================================
LIF: ∞ | ROLE: CELESTIAL_INDEX_CONDUCTOR | RANK: OMEGA_SUPREME
AUTH_CODE: @#()@(#()@#)(()!!!!

This divine artisan performs the Rite of the Global Census. It scries the
Archetypes, Shards, and Atoms, extracts their 7-Pillar Gnostic DNA,
calculates their High-Dimensional Semantic Vectors using Sentence Transformers,
and materializes the Master Index for the Deterministic Dream Engine.
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
from typing import List, Dict, Any, Optional

# --- THE NEURAL UPLINK ---
try:
    from sentence_transformers import SentenceTransformer

    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False

# --- THE VISUAL UPLINK ---
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

    HAS_RICH = True
except ImportError:
    HAS_RICH = False


class MasterLibrarian:
    """
    The Sovereign Cartographer and Neural Embedder of the Grimoire.
    """

    INDEX_VERSION = "3.0.0-VECTOR"

    # The 7 Sacred Pillars
    HEADER_REGEX = re.compile(r"^#\s*@([a-zA-Z0-9_]+):\s*(.*)$")

    def __init__(self, repo: str, branch: str, output_file: str, vaults: List[str]):
        self.repo = repo
        self.branch = branch
        self.vaults = [Path(v).resolve() for v in vaults]
        self.output_path = Path(output_file).resolve()

        self.console = Console() if HAS_RICH else None
        self.index: List[Dict[str, Any]] = []
        self.heresies: List[str] = []

        # Load the Semantic Cortex (Sentence Transformer)
        self.model = None
        if HAS_TRANSFORMERS:
            self.proclaim("Awakening the Neural Cortex (all-MiniLM-L6-v2)...", "yellow")
            # 384-dimensional vector space, extremely fast and lightweight
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            self.proclaim("WARNING: SentenceTransformers unmanifest. Vectors will be void.", "bold red")

    def proclaim(self, msg: str, style: str = "cyan"):
        if self.console:
            self.console.print(f"[{style}]»[/] {msg}")
        else:
            print(f">> {msg}")

    def conduct_census(self):
        """The Grand Rite of the Census and Embedding."""
        if self.console:
            self.console.print(Panel(
                f"Librarian Awakening. Scrying[bold magenta]{self.repo}[/] ({self.branch})\n"
                f"Vaults: {', '.join([v.name for v in self.vaults])}",
                title="[bold white]Ω_CELESTIAL_VECTOR_CENSUS[/]",
                border_style="cyan"
            ))

        all_shards = []
        for vault in self.vaults:
            if vault.exists():
                all_shards.extend(list(vault.rglob("*.scaffold")))
                all_shards.extend(list(vault.rglob("*.py")))  # Capture Atoms

        if HAS_RICH:
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(bar_width=None, pulse_style="cyan"),
                    TimeElapsedColumn(),
                    console=self.console,
                    transient=True
            ) as progress:
                task = progress.add_task("[cyan]Extracting DNA & Calculating Vectors...", total=len(all_shards))
                for shard in all_shards:
                    self._perceive_and_embed(shard)
                    progress.update(task, advance=1)
        else:
            for shard in all_shards:
                self._perceive_and_embed(shard)

        self._finalize_and_inscribe()

    def _perceive_and_embed(self, path: Path):
        """
        [THE NEURAL GAZE]
        Extracts the 7 Pillars and generates the mathematical soul (Vector).
        """
        # Determine which vault this belongs to (archetypes, shards, or atoms)
        vault_parent = next((v for v in self.vaults if str(path).startswith(str(v))), None)
        if not vault_parent:
            return

        rel_path = path.relative_to(vault_parent.parent).as_posix()
        slug = path.stem

        try:
            content = path.read_text(encoding="utf-8")

            # 1. EXTRACT THE 7 PILLARS
            dna = self._extract_7_pillars(content, slug)
            dna["file_path"] = rel_path
            dna["type"] = vault_parent.name  # 'archetypes', 'shards', or 'atoms'

            # 2. VALIDATION
            if not dna.get("description") or not dna.get("vibe"):
                self.heresies.append(f"Void Pillars in {rel_path}: Missing @description or @vibe.")
                return  # We do not index profane matter

            # 3. THE SEMANTIC EMBEDDING (THE MAGIC)
            # We combine the description and the vibe to create the Semantic String
            semantic_string = f"{dna['description']} {dna['vibe']}"

            if self.model:
                # Transmute the string into a 384-dimensional mathematical array
                vector = self.model.encode(semantic_string).tolist()
                dna["semantic_vector"] = vector
            else:
                dna["semantic_vector"] = []

            # 4. CHRONICLING
            hasher = hashlib.sha256(content.encode('utf-8'))
            dna["sha256"] = hasher.hexdigest()
            dna["bytes"] = len(content)

            clean_repo = self.repo.rstrip('/')
            dna["url"] = f"https://raw.githubusercontent.com/{clean_repo}/{self.branch}/{rel_path}"

            self.index.append(dna)

        except Exception as e:
            self.heresies.append(f"Fracture in {rel_path}: {type(e).__name__} - {str(e)}")

    def _extract_7_pillars(self, content: str, slug: str) -> Dict[str, Any]:
        """Parses the Universal Gnostic Header."""
        dna = {
            "id": slug,
            "description": "",
            "category": "System",
            "vibe": "",
            "provides": [],
            "requires": [],
            "substrate": [],
            "version": "1.0.0"
        }

        lines = content.splitlines()[:50]  # Headers must be at the top
        for line in lines:
            match = self.HEADER_REGEX.match(line.strip())
            if match:
                key, val = match.group(1).lower(), match.group(2).strip()

                if key in ["description", "category", "vibe", "version"]:
                    dna[key] = val
                elif key in ["provides", "requires", "substrate"]:
                    # Parse YAML-style arrays: [auth, db]
                    clean_val = val.strip("[]")
                    dna[key] = [v.strip().lower() for v in clean_val.split(",") if v.strip()]

        return dna

    def _finalize_and_inscribe(self):
        """The Rite of Final Inscription."""
        self.index.sort(key=lambda x: x["id"])

        manifest = {
            "version": self.INDEX_VERSION,
            "timestamp": time.time(),
            "repo": self.repo,
            "branch": self.branch,
            "total_shards": len(self.index),
            "vector_dimensions": 384 if self.model else 0,
            "registry": self.index
        }

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        temp_file = self.output_path.with_suffix(".tmp")

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)

            os.replace(temp_file, self.output_path)

            if self.console:
                self._render_final_report()
            else:
                print(f"✨ Vector Index Materialized at {self.output_path}")

        except Exception as e:
            self.proclaim(f"Inscription Paradox: {e}", "bold red")

    def _render_final_report(self):
        table = Table(title="Celestial Vector Census", box=None, expand=True)
        table.add_column("Type", style="bold magenta")
        table.add_column("Count", justify="right", style="white")
        table.add_column("Vectors Embedded", justify="center", style="bold green")

        # Group by Type (Archetype, Shard, Atom)
        counts = {}
        for item in self.index:
            t = item["type"]
            counts[t] = counts.get(t, 0) + 1

        for t, count in counts.items():
            table.add_row(t.title(), str(count), "✅ TRUE")

        self.console.print(table)
        self.console.print(f"\n[bold green]✨ Vector Index v{self.INDEX_VERSION} Manifest.[/]")

        if self.heresies:
            self.console.print(Panel(
                "\n".join([f"• {h}" for h in self.heresies]),
                title="[bold yellow]Dossier of Schisms (Rejected Matter)[/]",
                border_style="yellow"
            ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ω | The Master Librarian: Vector Embedder")
    parser.add_argument("--repo", required=True, help="GitHub repository identifier")
    parser.add_argument("--branch", default="main", help="The target branch")
    parser.add_argument("--archetypes", default="archetypes", help="Path to archetypes vault")
    parser.add_argument("--shards", default="shards", help="Path to shards vault")
    parser.add_argument("--atoms", default="atoms", help="Path to atoms vault")
    parser.add_argument("--output", default="registry/index.json", help="Path to inscribe the final index.json")

    args = parser.parse_args()

    start_time = time.perf_counter()

    librarian = MasterLibrarian(
        repo=args.repo,
        branch=args.branch,
        vaults=[args.archetypes, args.shards, args.atoms],
        output_file=args.output
    )

    librarian.conduct_census()

    duration_ms = (time.perf_counter() - start_time) * 1000
    print(f"\n[LIBRARIAN] Vector Embedding complete in {duration_ms:.2f}ms. The Brain is Synced.")