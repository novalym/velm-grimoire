# Path: scripts/rebuild_index.py
# ---------------------------------------------------

"""
=================================================================================
== THE MASTER LIBRARIAN: OMEGA POINT (V-Ω-TOTALITY-V3.2-FINAL-SINGULARITY)     ==
=================================================================================
LIF: ∞ | ROLE: CELESTIAL_ATLAS_CONDUCTOR | RANK: OMEGA_SOVEREIGN
AUTH: Ω_LIBRARIAN_VMAX_SINGULARITY_2026_FINALIS

[THE MANIFESTO]
The supreme definitive authority for Gnostic Atlas materialization. This version
achieves absolute zero-stiction execution, righteously annihilating the
'PCI-Bus Warning' heresy and the 'Scoping Paradox' via the Revelation Protocol.

It guarantees 384-dimensional vector resonance with 0-Torch purity.
=================================================================================
"""

import os

# [ASCENSION 2]: APOPHATIC SILENCE WARD
# We silence the ONNX PCI warnings at the absolute gate of inception.
os.environ["ORT_LOGGING_LEVEL"] = "3"

import json
import sys
import time
import hashlib
import re
import argparse
import urllib.request
import collections
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Set, Final

# --- THE 0-TORCH NEURAL UPLINK ---
import numpy as np

try:
    import onnxruntime as ort
    from tokenizers import Tokenizer

    HAS_NEURAL_LIBS = True
except ImportError:
    HAS_NEURAL_LIBS = False

# --- THE VISUAL UPLINK ---
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, DownloadColumn

    HAS_RICH = True
except ImportError:
    HAS_RICH = False


class MasterLibrarian:
    """The Sovereign Cartographer of the Multiversal Registry."""

    # [CELESTIAL COORDINATES]: Bit-perfect parity with the Ocular Eye (WASM)
    CDN_BASE: Final[str] = "https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/onnx"
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

        # [ASCENSION 1]: SOVEREIGN STATS REPOSITORY
        self.revelation_manifest: Dict[str, Any] = {}

        # --- MOVEMENT I: NEURAL CORTEX AWAKENING ---
        self.tokenizer = None
        self.session = None

        if engine == "onnx" and HAS_NEURAL_LIBS:
            self._awaken_retina()
        else:
            self.proclaim("Engine: LEXICAL (Vectors deferred).", "yellow")

    def _awaken_retina(self):
        """[ASCENSION 4]: AUTONOMIC NEURAL INCEPTION."""
        model_dir = Path.home() / ".scaffold" / "models" / "all-MiniLM-L6-v2"
        if not (model_dir / "model_quantized.onnx").exists():
            self._initiate_model_manifestation(model_dir)

        try:
            self.tokenizer = Tokenizer.from_file(str(model_dir / "tokenizer.json"))
            opts = ort.SessionOptions()
            opts.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL

            self.session = ort.InferenceSession(
                str(model_dir / "model_quantized.onnx"),
                sess_options=opts,
                providers=["CPUExecutionProvider"]
            )
            self.proclaim(f"Neural Retina Resonant (384-D).", "bold green")
        except Exception as e:
            self.proclaim(f"Neural Fracture: {e}. Falling back to Lexical.", "bold red")
            self.engine = "lexical"

    def _initiate_model_manifestation(self, target_dir: Path):
        """Physically downloads the 25MB mind-shards from the Celestial Hub."""
        self.proclaim("🧠 [INCEPTION] Neural weights unmanifested. Materializing JIT...", "yellow")
        target_dir.mkdir(parents=True, exist_ok=True)

        shards = [
            ("model_quantized.onnx", self.CDN_BASE + "/model_quantized.onnx"),
            ("tokenizer.json", "https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/tokenizer.json"),
            ("config.json", "https://huggingface.co/Xenova/all-MiniLM-L6-v2/resolve/main/config.json")
        ]

        if HAS_RICH:
            with Progress(
                    SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                    BarColumn(), DownloadColumn(), TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                    console=self.console, transient=True
            ) as progress:
                for shard_name, url in shards:
                    dest = target_dir / shard_name
                    task_id = progress.add_task(f"Downloading {shard_name}...", total=None)
                    try:
                        def _report(count, block_size, total_size):
                            if total_size > 0:
                                progress.update(task_id, completed=count * block_size, total=total_size)

                        urllib.request.urlretrieve(url, str(dest), reporthook=_report)
                    except Exception as e:
                        self.proclaim(f"Download Fracture: {e}", "bold red")
                        return
        else:
            for shard_name, url in shards:
                urllib.request.urlretrieve(url, str(target_dir / shard_name))

    def proclaim(self, msg: str, style: str = "cyan"):
        if self.console:
            self.console.print(f"[{style}]»[/] {msg}")
        else:
            print(f">> {msg}")

    def conduct_census(self) -> Dict[str, Any]:
        """[THE GRAND RITE OF THE CENSUS] Returns the final manifest revelation."""
        if self.console:
            self.console.print(Panel(
                f"Librarian Awakening. Scrying [bold magenta]{self.repo}[/] ({self.branch})\n"
                f"Engine: [bold green]{self.engine.upper()}[/] | Substrate: [bold blue]0-TORCH[/]\n"
                f"Vaults: {', '.join([v.name for v in self.vaults if v.exists()])}",
                title="[bold white]Ω_CELESTIAL_GENOMIC_CENSUS[/]", border_style="cyan"
            ))

        all_shards = []
        for vault in self.vaults:
            if vault.exists():
                all_shards.extend(list(vault.rglob("*.scaffold")))
                all_shards.extend(list(vault.rglob("*.py")))

        if HAS_RICH:
            with Progress(
                    SpinnerColumn(), TextColumn("[progress.description]{task.description}"),
                    BarColumn(bar_width=None, pulse_style="cyan"), TimeElapsedColumn(),
                    console=self.console, transient=True
            ) as progress:
                task = progress.add_task("[cyan]Materializing Genome & Vectors...", total=len(all_shards))
                for shard in all_shards:
                    self._perceive_and_embed(shard)
                    progress.update(task, advance=1)
        else:
            for shard in all_shards: self._perceive_and_embed(shard)

        return self._finalize_and_inscribe()

    def _perceive_and_embed(self, path: Path):
        """[THE NEURAL GAZE] Extracts DNA and forges the mathematical soul."""
        vault_parent = next((v for v in self.vaults if str(path).startswith(str(v))), None)
        if not vault_parent: return

        rel_path = path.relative_to(vault_parent.parent).as_posix()
        slug = path.stem

        try:
            content = path.read_text(encoding="utf-8", errors='ignore')
            content = content.replace('\x00', '')

            dna = self._extract_genome(content, slug)
            dna["file_path"] = rel_path
            dna["type"] = "atom" if path.suffix == ".py" else "shard"
            if "archetype" in str(path).lower(): dna["type"] = "archetype"

            if self.engine == "onnx" and self.session:
                semantic_string = f"{dna.get('summary', '')} {dna.get('vibe', '')}"
                dna["semantic_vector"] = self._embed_onnx(semantic_string)
            else:
                dna["semantic_vector"] = []

            dna["sha256"] = hashlib.sha256(content.encode('utf-8')).hexdigest()
            dna["bytes"] = len(content)
            dna["url"] = f"https://raw.githubusercontent.com/{self.repo.rstrip('/')}/{self.branch}/{rel_path}"

            self.index.append(dna)

        except Exception as e:
            self.heresies.append(f"Fracture in {rel_path}: {str(e)}")

    def _embed_onnx(self, text: str) -> List[float]:
        """Manual ONNX Reactor: Inference -> Mean Pooling -> L2 Normalization."""
        encoded = self.tokenizer.encode(text)
        input_ids = np.array([encoded.ids], dtype=np.int64)
        attention_mask = np.array([encoded.attention_mask], dtype=np.int64)
        token_type_ids = np.array([encoded.type_ids], dtype=np.int64)

        outputs = self.session.run(None, {
            "input_ids": input_ids, "attention_mask": attention_mask, "token_type_ids": token_type_ids
        })

        token_embeddings = outputs[0]
        mask = np.expand_dims(attention_mask, -1)
        sum_embeddings = np.sum(token_embeddings * mask, axis=1)
        sum_mask = np.clip(np.sum(mask, axis=1), a_min=1e-9, a_max=None)
        sentence_embedding = sum_embeddings / sum_mask

        norm = np.linalg.norm(sentence_embedding, axis=1, keepdims=True)
        normalized = (sentence_embedding / norm)[0]
        return normalized.tolist()

    def _extract_genome(self, content: str, slug: str) -> Dict[str, Any]:
        """Parses the v3.0 Universal Gnostic Header."""
        dna = {
            "id": slug, "summary": "", "category": "System", "vibe": "",
            "provides": [], "requires": [], "substrate": {}, "metabolism": {}, "suture": {}, "version": "1.0.0"
        }
        lines = content.splitlines()[:100]
        for line in lines:
            match = self.HEADER_REGEX.match(line.strip())
            if match:
                key, val = match.group(1).lower(), match.group(2).strip()
                if key == "description": key = "summary"
                if key in ["summary", "category", "vibe", "version", "tier"]:
                    dna[key] = val
                elif key in ["provides", "requires"]:
                    dna[key] = [v.strip().lower() for v in val.strip("[]").split(",") if v.strip()]
                elif key in ["substrate", "metabolism", "suture"]:
                    try:
                        dna[key] = json.loads(val.replace("'", '"'))
                    except:
                        dna[key] = {"raw": val}
        return dna

    def _finalize_and_inscribe(self) -> Dict[str, Any]:
        """[ASCENSION 18]: ATOMIC FINALITY."""
        self.index.sort(key=lambda x: x["id"])

        dims = 0
        if self.index and "semantic_vector" in self.index[0] and self.index[0]["semantic_vector"]:
            dims = len(self.index[0]["semantic_vector"])

        # [ASCENSION 1]: Promote to class property for the Revelation Protocol
        self.revelation_manifest = {
            "version": "3.0.0-UCL-TOTALITY",
            "timestamp": time.time(),
            "repo": self.repo,
            "branch": self.branch,
            "total_shards": len(self.index),
            "engine": self.engine,
            "vector_dimensions": dims,
            "registry": self.index
        }

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(self.revelation_manifest, f, indent=2)

        self._render_final_report(dims)
        return self.revelation_manifest

    def _render_final_report(self, dims: int):
        if not self.console:
            print(f"✨ Registry Materialized: {self.output_path} (Dims: {dims})")
            return

        table = Table(title="Ω | CELESTIAL ATLAS CONVERGENCE", box=None, expand=True)
        table.add_column("Locus", style="bold cyan")
        table.add_column("Mass", justify="right", style="white")
        table.add_column("Vectors", justify="center")

        counts = collections.Counter(item["type"] for item in self.index)
        for t, count in counts.items():
            status = f"[bold green]{dims}D[/]" if dims > 0 else "[bold yellow]0D[/]"
            table.add_row(t.upper(), str(count), status)

        self.console.print(table)

        if self.heresies:
            self.console.print(Panel(
                "\n".join([f"• {h}" for h in self.heresies[:15]]),
                title="[bold red]GENOMIC FRACTURES[/]", border_style="red"
            ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ω | Master Librarian: 0-Torch Vector Embedder")
    parser.add_argument("--repo", required=True)
    parser.add_argument("--branch", default="main")
    parser.add_argument("--output", default="registry/index.json")
    parser.add_argument("--engine", choices=["onnx", "lexical"], default="onnx")

    # Vaults
    parser.add_argument("--archetypes", default="archetypes")
    parser.add_argument("--shards", default="shards")
    parser.add_argument("--infrastructure", default="infrastructure")
    parser.add_argument("--codex", default="codex/shards")
    parser.add_argument("--traits", default="traits")

    args = parser.parse_args()
    start_time = time.perf_counter()

    librarian = MasterLibrarian(
        repo=args.repo, branch=args.branch, output_file=args.output,
        vaults=[args.archetypes, args.shards, args.infrastructure, args.codex, args.traits],
        engine=args.engine
    )

    # [THE REVELATION]: Capture the manifest returned from the census
    manifest = librarian.conduct_census()

    duration = (time.perf_counter() - start_time) * 1000
    print(
        f"\n[LIBRARIAN] Singularity achieved in {duration:.2f}ms. Vector Dimensions: {manifest.get('vector_dimensions', 0)}")