# Deterministic typography workflow

Use this workflow whenever required copy appears outside the product packaging.

## Non-negotiable rule

GPT Image creates the art plate only. It must not draw promotional copy, headlines, supporting copy, CTAs, prices, dates, disclaimers, or brand/campaign logos. Preserve any real text already printed on the supplied product pack; do not remove or rewrite packaging labels.

After the art plate is accepted, place all required copy and approved logos deterministically with the bundled assets. The final typography must come from the packaged `.otf` or `.ttf` file, not from an AI approximation.

If deterministic compositing is unavailable in the current environment, stop and explain that exact-font output cannot be completed there. Do not silently fall back to AI-drawn text.

## Default mapping

- Headline: `Editorial New Ultra Light` from the active skill's `assets/fonts/editorial-new/BHN-Editorial-New-Ultra-Light.otf`.
- Italic headline only when the design calls for it: `BHN-Editorial-New-Ultra-Light-Italic.otf`.
- Supporting copy: the bundled `Roboto-VariableFont_wdth,wght.ttf`.
- SVN-Aptima: do not select it by default or infer it from a generic request for bold text. Use it only when the user explicitly requests SVN-Aptima or a specific bundled SVN-Aptima file.

Do not synthesize bold, italic, condensed, or another weight that is not present in the selected bundled file.

## Art-plate generation

1. Reserve clean negative space for every text block and logo row.
2. Tell the image model explicitly: no promotional text, no typography, no letter-like marks, no logos, no badges, and no watermark outside the supplied product packaging.
3. Generate or edit the visual background, product scene, person when authorized, lighting, podium, texture, and decorative motifs.
4. Reject an art plate containing stray pseudo-text in a required text or logo zone.

## Deterministic composition

The plugin includes `scripts/compose_social_post.py`. It accepts a JSON spec and uses Pillow to place bundled fonts and exact image assets. Paths in the spec are relative to the spec file unless absolute.

Example:

```json
{
  "base_image": "art-plate.png",
  "output": "final.png",
  "layers": [
    {
      "type": "text",
      "text": "Nâng niu làn da Việt",
      "font": "../plugins/naris-premium/skills/naris-premium-campaign-hoa-hau-viet-nam/assets/fonts/editorial-new/BHN-Editorial-New-Ultra-Light.otf",
      "font_size": 88,
      "x": 540,
      "y": 150,
      "max_width": 900,
      "align": "center",
      "line_height": 102,
      "tracking": 0,
      "fill": "#AE8E5E"
    },
    {
      "type": "image",
      "path": "../plugins/naris-premium/skills/naris-premium-campaign-hoa-hau-viet-nam/assets/naris-social-logo-black.png",
      "x": 100,
      "y": 60,
      "width": 320,
      "height": 90
    }
  ]
}
```

Run:

```powershell
python plugins/naris-premium/scripts/compose_social_post.py --spec path/to/layout.json
```

Choose font size, wrapping, tracking, coordinates, and logo boxes for the active composition rather than treating the example values as a template.

## Final QA

- Compare Vietnamese spelling and punctuation character by character with the approved copy.
- Confirm the headline font file is Editorial New Ultra Light unless the user explicitly requested an approved alternative.
- Confirm body copy uses bundled Roboto.
- Confirm no AI-drawn duplicate of the headline or logos remains underneath the deterministic layers.
- Check safe margins, line breaks, contrast, hierarchy, logo clear space, and thumbnail readability.
- Keep a clean art plate and the composition spec alongside the final output when future revision is likely.

