from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "naris-premium"
COMPOSITOR = PLUGIN / "scripts" / "compose_social_post.py"


class CompositorSmokeTest(unittest.TestCase):
    def test_bundled_editorial_and_roboto_render_vietnamese(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir_value:
            temp_dir = Path(temp_dir_value)
            output = temp_dir / "result.png"
            spec = {
                "base_image": str(PLUGIN / "assets" / "daily-example.png"),
                "output": str(output),
                "layers": [
                    {
                        "type": "text",
                        "text": "Nâng niu làn da Việt",
                        "font": str(
                            PLUGIN
                            / "skills"
                            / "naris-premium-social-visuals"
                            / "assets"
                            / "fonts"
                            / "editorial-new"
                            / "BHN-Editorial-New-Ultra-Light.otf"
                        ),
                        "font_size": 48,
                        "x": 40,
                        "y": 40,
                        "max_width": 800,
                        "fill": "#51362B",
                    },
                    {
                        "type": "text",
                        "text": "Bộ 3 nước cân bằng Naris Lotion",
                        "font": str(
                            PLUGIN
                            / "skills"
                            / "naris-premium-social-visuals"
                            / "assets"
                            / "fonts"
                            / "roboto"
                            / "Roboto-VariableFont_wdth,wght.ttf"
                        ),
                        "font_size": 24,
                        "x": 40,
                        "y": 110,
                        "max_width": 800,
                        "fill": "#392B1F",
                    },
                ],
            }
            spec_path = temp_dir / "spec.json"
            spec_path.write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
            subprocess.run(
                [sys.executable, str(COMPOSITOR), "--spec", str(spec_path)],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertTrue(output.is_file())
            self.assertGreater(output.stat().st_size, 0)


if __name__ == "__main__":
    unittest.main()

