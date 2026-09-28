#!/usr/bin/env python3
"""Deterministically place bundled fonts and approved image assets on an art plate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageColor, ImageDraw, ImageFont
except ImportError as exc:  # pragma: no cover - depends on the host environment
    raise SystemExit(
        "Pillow is required for deterministic typography. "
        "Install Pillow in the active Python environment; do not fall back to AI-drawn text."
    ) from exc


PLUGIN_ROOT = Path(__file__).resolve().parents[1]


def resolve_path(value: str, spec_dir: Path) -> Path:
    path = Path(value)
    return path.resolve() if path.is_absolute() else (spec_dir / path).resolve()


def require_bundled_font(path: Path) -> None:
    fonts_roots = [p.resolve() for p in PLUGIN_ROOT.glob("skills/*/assets/fonts")]
    if not any(root == path.parent or root in path.parents for root in fonts_roots):
        raise ValueError(f"Font must come from the plugin's bundled assets: {path}")
    if not path.is_file():
        raise FileNotFoundError(path)


def measure(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, tracking: float) -> float:
    if not text:
        return 0
    width = float(draw.textlength(text, font=font))
    return width + max(0, len(text) - 1) * tracking


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: float | None,
    tracking: float,
) -> list[str]:
    if not max_width:
        return text.splitlines() or [""]
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if measure(draw, candidate, font, tracking) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def draw_tracked_text(
    draw: ImageDraw.ImageDraw,
    position: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    tracking: float,
) -> None:
    x, y = position
    if tracking == 0:
        draw.text((x, y), text, font=font, fill=fill)
        return
    for char in text:
        draw.text((x, y), char, font=font, fill=fill)
        x += float(draw.textlength(char, font=font)) + tracking


def render_text(canvas: Image.Image, layer: dict, spec_dir: Path) -> None:
    required = {"text", "font", "font_size", "x", "y"}
    missing = sorted(required - layer.keys())
    if missing:
        raise ValueError(f"Text layer is missing: {', '.join(missing)}")
    font_path = resolve_path(str(layer["font"]), spec_dir)
    require_bundled_font(font_path)
    font = ImageFont.truetype(str(font_path), int(layer["font_size"]))
    variation = layer.get("variation_name")
    if variation and hasattr(font, "set_variation_by_name"):
        font.set_variation_by_name(str(variation))

    draw = ImageDraw.Draw(canvas)
    tracking = float(layer.get("tracking", 0))
    max_width = float(layer["max_width"]) if layer.get("max_width") else None
    lines = wrap_text(draw, str(layer["text"]), font, max_width, tracking)
    line_height = int(layer.get("line_height", round(int(layer["font_size"]) * 1.15)))
    align = str(layer.get("align", "left")).lower()
    fill = ImageColor.getcolor(str(layer.get("fill", "#1D1B1A")), "RGBA")
    x = float(layer["x"])
    y = float(layer["y"])

    for line in lines:
        width = measure(draw, line, font, tracking)
        line_x = x
        if align == "center":
            line_x = x - width / 2
        elif align == "right":
            line_x = x - width
        elif align != "left":
            raise ValueError(f"Unsupported text alignment: {align}")
        draw_tracked_text(draw, (line_x, y), line, font, fill, tracking)
        y += line_height


def render_image(canvas: Image.Image, layer: dict, spec_dir: Path) -> None:
    required = {"path", "x", "y", "width", "height"}
    missing = sorted(required - layer.keys())
    if missing:
        raise ValueError(f"Image layer is missing: {', '.join(missing)}")
    source_path = resolve_path(str(layer["path"]), spec_dir)
    if not source_path.is_file():
        raise FileNotFoundError(source_path)
    source = Image.open(source_path).convert("RGBA")
    box_width, box_height = int(layer["width"]), int(layer["height"])
    source.thumbnail((box_width, box_height), Image.Resampling.LANCZOS)
    x = int(layer["x"] + (box_width - source.width) / 2)
    y = int(layer["y"] + (box_height - source.height) / 2)
    opacity = float(layer.get("opacity", 1.0))
    if not 0 <= opacity <= 1:
        raise ValueError("Image opacity must be between 0 and 1")
    if opacity < 1:
        alpha = source.getchannel("A").point(lambda value: round(value * opacity))
        source.putalpha(alpha)
    canvas.alpha_composite(source, (x, y))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, help="Path to the JSON composition specification")
    args = parser.parse_args()
    spec_path = Path(args.spec).resolve()
    spec = json.loads(spec_path.read_text(encoding="utf-8-sig"))
    spec_dir = spec_path.parent

    base_path = resolve_path(str(spec["base_image"]), spec_dir)
    output_path = resolve_path(str(spec["output"]), spec_dir)
    canvas = Image.open(base_path).convert("RGBA")
    for layer in spec.get("layers", []):
        layer_type = layer.get("type")
        if layer_type == "text":
            render_text(canvas, layer, spec_dir)
        elif layer_type == "image":
            render_image(canvas, layer, spec_dir)
        else:
            raise ValueError(f"Unsupported layer type: {layer_type}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() in {".jpg", ".jpeg"}:
        canvas.convert("RGB").save(output_path, quality=95, subsampling=0)
    else:
        canvas.save(output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"Composition failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

