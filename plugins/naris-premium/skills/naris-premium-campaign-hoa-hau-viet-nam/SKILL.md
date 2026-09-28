---
name: naris-premium-campaign-hoa-hau-viet-nam
description: Create or revise Naris Premium social posts for the Hoa Hậu Việt Nam 2026 campaign. Use when the user selects Campaign mode and names Hoa Hậu Việt Nam or HHVN; apply the campaign's warm paper, pink lotus, gold editorial type, approved logos, and fixed Naris-left/HHVN-right lockup without reusing the key-visual person.
---

# Naris Premium Campaign - Hoa Hậu Việt Nam

Create one polished campaign post that is recognizably part of the Hoa Hậu Việt Nam 2026 x Naris Premium visual system.

## Activation boundary

Use this skill only when the user has selected Campaign mode and identifies the campaign as Hoa Hậu Việt Nam, HHVN, Hoa Hậu Việt Nam 2026, or HHVN 2026. Do not use it for Daily posts or another pageant/campaign.

Before generating or editing, read [references/hhvn-visual-system.md](references/hhvn-visual-system.md) completely. The supplied key visual was used only to derive this system; the original character image is not stored in the skill and must not be treated as a reusable asset.

Also read [../../references/deterministic-typography.md](../../references/deterministic-typography.md). The HHVN headline must be typeset from the bundled Editorial New Ultra Light font after image generation. Supporting copy must use bundled Roboto. Do not use SVN-Aptima unless the user explicitly requests it.

## Required inputs

Do not generate until these are known:

1. Product image or images showing the exact packshot(s).
2. Exact copy and required information for the post.
3. Target aspect ratio or pixel size.
4. A separate authorized person image whenever the requested post includes a person.

Reference images beyond the campaign key visual are optional. If the user asks for a person but supplies none, ask for that image. Never reuse, reconstruct, or imitate the woman in the source key visual.

## Fixed campaign rules

- Place the approved **Naris logo on the left** and the approved **HHVN logo on the right** within the shared logo row.
- This order is mandatory even though the source key visual shows the reverse. The user's explicit rule supersedes the source example.
- Use `assets/naris-social-logo-black.png` or its white version for Naris and `assets/hhvn-logo-2026-pink.png` for HHVN. Do not redraw, retype, recolor, distort, or regenerate either logo.
- Keep both logos optically balanced, horizontally aligned, clearly separated, and surrounded by adequate clear space. A thin neutral vertical separator may be used between them.
- Preserve the campaign's warm paper, pageant-pink botanical line art, restrained warm gold headline, and elegant editorial mood.
- The person in the original key visual is not a reusable campaign asset. A person appears only when supplied for the current post.

## Workflow

1. Normalize the brief: product truth, exact copy, ratio, person requirement, additional references, must-keep elements, and prohibited elements.
2. Inspect all supplied images and distinguish product truth, authorized person, style reference, and edit target. Do not infer that a reference person is authorized unless the user provides that image for use.
3. Build one composition using the campaign visual system. Adapt the KV grammar to the requested ratio rather than copying its exact placements.
4. Keep the product as the primary commercial focal point unless the user explicitly asks for a person-led announcement. Even then, the product and sponsor relationship must remain legible.
5. Attach only relevant visual assets to GPT Image: exact product, authorized person, paper texture, and optional decorative motifs. Reserve a quiet headline area and a top logo row, but do not ask GPT Image to render promotional copy or either logo.
6. Generate or edit the text-free art plate with GPT Image. Explicitly prohibit promotional text, pseudo-text, Naris/HHVN logos, badges, and watermarks outside the supplied product packaging.
7. Inspect the art plate for product identity, person identity when supplied, ratio, hierarchy, campaign palette, asset restraint, reserved space, and stray pseudo-text. Perform one focused regeneration when a material defect exists.
8. Use deterministic compositing to typeset the headline with the bundled Editorial New Ultra Light file, supporting copy with bundled Roboto, and place the exact Naris-left/HHVN-right logo assets. Use `../../scripts/compose_social_post.py` from this skill directory or an equivalent deterministic compositor.
9. Inspect the final at full size and thumbnail size. Verify exact copy, actual font files, fixed logo order, logo integrity, product identity, line breaks, safe margins, contrast, and absence of generated duplicate text.
10. Deliver the best acceptable output inline and identify it as Campaign: Hoa Hậu Việt Nam.

## Asset use

The reusable campaign assets are:

- `assets/hhvn-logo-2026-pink.png` - exact HHVN 2026 logo.
- `assets/naris-social-logo-black.png` and `assets/naris-social-logo-white.png` - exact Naris social logos.
- `assets/hhvn-warm-paper-texture.jpg` - warm off-white paper texture.
- `assets/hhvn-lotus-line-art-left.png` - pale pink botanical/lotus edge motif.
- `assets/hhvn-lotus-divider-icon.png` - small pink five-petal divider icon.
- `assets/hhvn-pink-brush-stroke.png` - dry pink brush accent for a lower edge or corner.
- `assets/hhvn-silver-brush-arc-sample.jpg` - pale silver-blue curved brush reference.

Use only the assets that support the composition. Do not force every asset into every post.

## Completion gate

Do not call the post final unless:

- Naris is on the left and HHVN is on the right in the logo row.
- Both logos remain exact, readable, balanced, and undistorted.
- No person from the source key visual has been reused or imitated.
- Any visible person came from an authorized image supplied for the current post and remains recognizable.
- The product pack, count, color, label, and geometry remain faithful to the supplied product image.
- Required copy is exact and readable, with no invented claim, award, price, date, or endorsement.
- The headline is rendered from bundled Editorial New Ultra Light, supporting copy from bundled Roboto, and neither promotional typography nor campaign logos are AI-drawn.
- The warm textured background, restrained pink botanical language, gold editorial hierarchy, and refined pageant mood are recognizable without becoming crowded.
- No asset from another Naris campaign has leaked into the image.
