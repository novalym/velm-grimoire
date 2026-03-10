# Path: scripts/rebuild_index.py
# ---------------------------------------------------

"""
=================================================================================
== THE MASTER LIBRARIAN: OMEGA (V-Ω-TOTALITY-V3.0-0-TORCH-VECTOR-FINALIS)      ==
=================================================================================
LIF: ∞ | ROLE: CELESTIAL_INDEX_CONDUCTOR | RANK: OMEGA_SOVEREIGN
AUTH: Ω_LIBRARIAN_VMAX_0_TORCH_2026_FINALIS

[THE MANIFESTO]
The supreme definitive authority for Registry materialization. It has been
transfigured to achieve 0-Torch Purity, utilizing the ONNX Runtime to
transmute Gnostic DNA into 384-dimensional mathematical souls.

It righteously enforces the v3.0 Genomic Specification, ensuring every
shard arriving in the Hub is genetically whole.
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
from typing import List, Dict, Any, Optional, Tuple, Set, Final

# --- THE 0-TORCH NEURAL UPLINK ---
import numpy as np

try:
    import onnxruntime as ort
    from tokenizers import Tokenizer

    HAS_NEURAL = True
except ImportError:
    HAS_NEURAL = False

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
    """The Sovereign Cartographer of the Multiversal Registry."""

    # [ASCENSION 3]: v3.0 GENOMIC SPECIFICATION
    # The 10 Pillars of Gnosis
    GENOMIC_PILLARS: Final[List[str]] = [
        "id", "version", "tier", "summary", "vibe",
        "provides", "requires", "metabolism", "substrate", "suture"
    ]

    HEADER_REGEX: Final[re.Pattern] = re.compile(r"^#\s*@([a-zA-Z0-9_]+):\s*(.*)$")

    def __init__(self, repo: str, branch: str, output_file: str, vaults: List[str], engine: str = "onnx"):
        """[THE RITE OF INCEPTION]"""
        self.repo = repo
        self.branch = branch
        self.vaults = [Path(v).resolve() for v in vaults]
        self.output_path = Path(output_file).resolve()
        self.engine = engine

        self.console = Console() if HAS_RICH else None
        self.index: List[Dict[str, Any]] = []
        self.heresies: List[str] = []

        # --- MOVEMENT I: NEURAL CORTEX AWAKENING ---
        self.tokenizer = None
        self.session = None

        if engine == "onnx" and HAS_NEURAL:
            self._load_onnx_retina()
        else:
            self.proclaim("Engine: LEXICAL (Vector generation deferred).", "yellow")

    def _load_onnx_retina(self):
        """[ASCENSION 2]: THE 0-TORCH METABOLISM SUTURE."""
        model_dir = Path.home() / ".scaffold" / "models" / "all-MiniLM-L6-v2"

        try:
            self.proclaim(f"Awakening 0-Torch Retina: {model_dir.name}", "yellow")
            self.tokenizer = Tokenizer.from_file(str(model_dir / "tokenizer.json"))

            opts = ort.SessionOptions()
            opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

            self.session = ort.InferenceSession(
                str(model_dir / "model_quantized.onnx"),
                sess_options=opts,
                providers=["CPUExecutionProvider"]
            )
        except Exception as e:
            self.proclaim(f"Neural Fracture: {e}. Defaulting to Lexical Mode.", "bold red")
            self.engine = "lexical"

    def proclaim(self, msg: str, style: str = "cyan"):
        if self.console:
            self.console.print(f"[{style}]»[/] {msg}")
        else:
            print(f">> {msg}")

    def conduct_census(self):
        """[THE GRAND RITE OF THE CENSUS]"""
        if self.console:
            self.console.print(Panel(
                f"Librarian Awakening. Scrying [bold magenta]{self.repo}[/] ({self.branch})\n"
                f"Engine: [bold green]{self.engine.upper()}[/] | Substrate: [bold blue]0-TORCH[/]\n"
                f"Vaults: {', '.join([v.name for v in self.vaults if v.exists()])}",
                title="[bold white]Ω_CELESTIAL_GENOMIC_CENSUS[/]",
                border_style="cyan"
            ))

        all_shards = []
        for vault in self.vaults:
            if vault.exists():
                all_shards.extend(list(vault.rglob("*.scaffold")))
                all_shards.extend(list(vault.rglob("*.py")))

        if HAS_RICH:
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    BarColumn(bar_width=None, pulse_style="cyan"),
                    TimeElapsedColumn(),
                    console=self.console,
                    transient=True
            ) as progress:
                task = progress.add_task("[cyan]Materializing Genome...", total=len(all_shards))
                for shard in all_shards:
                    self._perceive_and_embed(shard)
                    progress.update(task, advance=1)
        else:
            for shard in all_shards:
                self._perceive_and_embed(shard)

        self._finalize_and_inscribe()

    def _perceive_and_embed(self, path: Path):
        """[THE NEURAL GAZE] Extracts DNA and forges the mathematical soul."""
        # Detect Vault Parent
        vault_parent = next((v for v in self.vaults if str(path).startswith(str(v))), None)
        if not vault_parent: return

        rel_path = path.relative_to(vault_parent.parent).as_posix()
        slug = path.stem

        try:
            content = path.read_text(encoding="utf-8", errors='ignore')
            content = content.replace('\x00', '')  # Null-byte exorcism

            # 1. GENOMIC EXTRACTION
            dna = self._extract_genome(content, slug)
            dna["file_path"] = rel_path
            dna["tier"] = dna.get("tier", "mind")

            # [THE MASTER SUTURE]: Map Path relative to Hub
            dna["type"] = "atom" if path.suffix == ".py" else "shard"
            if "archetype" in str(path).lower(): dna["type"] = "archetype"

            # 2. VALIDATION OF THE PILLARS
            if not dna.get("summary") or not dna.get("vibe"):
                self.heresies.append(f"Genomic Drift in {rel_path}: Missing @summary or @vibe.")
                return

            # 3. THE 0-TORCH MATH STRIKE (VECTORIZATION)
            if self.engine == "onnx" and self.session:
                semantic_string = f"{dna['summary']} {dna['vibe']}"
                dna["semantic_vector"] = self._embed_onnx(semantic_string)
            else:
                dna["semantic_vector"] = []

            # 4. CHRONICLING
            dna["sha256"] = hashlib.sha256(content.encode('utf-8')).hexdigest()
            dna["bytes"] = len(content)
            dna["url"] = f"https://raw.githubusercontent.com/{self.repo.rstrip('/')}/{self.branch}/{rel_path}"

            self.index.append(dna)

        except Exception as e:
            self.heresies.append(f"Fracture in {rel_path}: {str(e)}")

    def _embed_onnx(self, text: str) -> List[float]:
        """
        =============================================================================
        == THE ONNX REACTOR (V-Ω-MEAN-POOLING-FINALIS)                             ==
        =============================================================================
        Perges the 384-dimensional vector soul without Torch.
        """
        # 1. Tokenization
        encoded = self.tokenizer.encode(text)
        input_ids = np.array([encoded.ids], dtype=np.int64)
        attention_mask = np.array([encoded.attention_mask], dtype=np.int64)
        token_type_ids = np.array([encoded.type_ids], dtype=np.int64)

        # 2. Inference
        outputs = self.session.run(None, {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "token_type_ids": token_type_ids
        })

        # 3. [THE CURE]: Manual Mean-Pooling
        token_embeddings = outputs[0]
        mask = np.expand_dims(attention_mask, -1)

        sum_embeddings = np.sum(token_embeddings * mask, axis=1)
        sum_mask = np.clip(np.sum(mask, axis=1), a_min=1e-9, a_max=None)

        sentence_embedding = sum_embeddings / sum_mask

        # 4. L2 Normalization
        norm = np.linalg.norm(sentence_embedding, axis=1, keepdims=True)
        normalized = (sentence_embedding / norm)[0]

        return normalized.tolist()

    def _extract_genome(self, content: str, slug: str) -> Dict[str, Any]:
        """[FACULTY 11]: Sovereign Header Sieve."""
        dna = {
            "id": slug,
            "summary": "",
            "category": "System",
            "vibe": "",
            "provides": [],
            "requires": [],
            "substrate": {},
            "metabolism": {},
            "suture": {},
            "version": "1.0.0"
        }

        # Scan the first 100 lines for the genome
        lines = content.splitlines()[:100]
        for line in lines:
            match = self.HEADER_REGEX.match(line.strip())
            if match:
                key, val = match.group(1).lower(), match.group(2).strip()

                # [THE FIX]: Support both v2.0 'description' and v3.0 'summary'
                if key == "description": key = "summary"

                if key in ["summary", "category", "vibe", "version", "tier"]:
                    dna[key] = val
                elif key in ["provides", "requires"]:
                    dna[key] = [v.strip().lower() for v in val.strip("[]").split(",") if v.strip()]
                elif key in ["substrate", "metabolism", "suture"]:
                    # [ASCENSION 3]: Parse JSON/YAML-style fragments in headers
                    try:
                        dna[key] = json.loads(val.replace("'", '"'))
                    except:
                        dna[key] = {"raw": val}

        return dna

    def _finalize_and_inscribe(self):
        """[ASCENSION 18]: Atomic Finality."""
        self.index.sort(key=lambda x: x["id"])

        manifest = {
            "version": "3.0.0-UCL-TOTALITY",
            "timestamp": time.time(),
            "repo": self.repo,
            "branch": self.branch,
            "total_shards": len(self.index),
            "engine": self.engine,
            "vector_dimensions": 384 if self.engine == "onnx" else 0,
            "registry": self.index
        }

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        temp_file = self.output_path.with_suffix(".tmp")

        try:
            with open(temp_file, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)

            os.replace(temp_file, self.output_path)
            self._render_final_report()

        except Exception as e:
            self.proclaim(f"Inscription Paradox: {e}", "bold red")

    def _render_final_report(self):
        if not self.console:
            print(f"✨ Registry Ascended: {self.output_path}")
            return

        table = Table(title="Ω | CELESTIAL ATLAS CONVERGENCE", box=None, expand=True)
        table.add_column("Locus", style="bold cyan")
        table.add_column("Mass", justify="right", style="white")
        table.add_column("Status", justify="center", style="bold green")

        counts = collections.Counter(item["type"] for item in self.index)
        for t, count in counts.items():
            table.add_row(t.upper(), str(count), "RESONANT")

        self.console.print(table)

        if self.heresies:
            self.console.print(Panel(
                "\n".join([f"• {h}" for h in self.heresies[:20]]),
                title="[bold red]GENOMIC FRACTURES (REDEMPTION REQUIRED)[/]",
                border_style="red"
            ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ω | Master Librarian: 0-Torch Vector Embedder")
    parser.add_argument("--repo", required=True, help="GitHub repository identifier")
    parser.add_argument("--branch", default="main", help="The target branch")
    parser.add_argument("--output", default="registry/index.json", help="Output path")
    parser.add_argument("--engine", choices=["onnx", "lexical"], default="onnx", help="The inference engine")

    # Stratum targets
    parser.add_argument("--archetypes", default="archetypes")
    parser.add_argument("--shards", default="shards")
    parser.add_argument("--infrastructure", default="infrastructure")
    parser.add_argument("--codex", default="codex/shards")
    parser.add_argument("--traits", default="traits")

    args = parser.parse_args()
    start_time = time.perf_counter()

    librarian = MasterLibrarian(
        repo=args.repo,
        branch=args.branch,
        output_file=args.output,
        vaults=[args.archetypes, args.shards, args.infrastructure, args.codex, args.traits],
        engine=args.engine
    )

    librarian.conduct_census()

    duration_ms = (time.perf_counter() - start_time) * 1000
    print(f"\n[LIBRARIAN] Totality achieved in {duration_ms:.2f}ms. The Multiverse is Indexed.")