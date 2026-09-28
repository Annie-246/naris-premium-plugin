# Hoa Hậu Việt Nam 2026 x Naris visual system

This campaign system is distilled from the supplied key visual. The source image includes a person, but that person is evidence only and is never a reusable asset.

## Campaign character

The campaign should feel ceremonial, feminine, refined, Vietnamese, and premium. It combines beauty-pageant elegance with Naris restraint: spacious, luminous, textural, and editorial rather than glitter-heavy or theatrical.

## Palette

- Warm paper white: approximately `#F7F6F4` / `#F5F1ED`.
- HHVN campaign pink: approximately `#F05C74`.
- Pale botanical pink: approximately `#E1C8CA`.
- Dry-brush rose: approximately `#DD96A6`.
- Warm restrained gold: approximately `#AE8E5E`.
- Charcoal text: approximately `#1D1B1A`.
- Pale silver-blue brush accent: approximately `#D8DEE7`.

Keep the surface mostly warm white. Pink and gold are accents, not full-field saturation. Use charcoal for supporting text. Avoid neon pink, bright yellow gold, metallic gradients, dense black fields, and multicolor pageant spectacle.

## Typography

### Campaign headline

Use the bundled **Editorial New Ultra Light** file for every default campaign headline: `assets/fonts/editorial-new/BHN-Editorial-New-Ultra-Light.otf`. Typeset it deterministically after the art plate has been generated. Do not ask the image model to imitate it or substitute another serif. Headline treatment is usually uppercase or title-led, very large, and warm gold with generous line spacing.

Do not use heavy slab serif, bubbly beauty fonts, ornate script, blackletter, condensed display type, or exaggerated swashes.

### Supporting copy

Use the bundled **Roboto** variable font with moderate-to-wide tracking. Supporting copy may be uppercase, smaller, charcoal, and framed by thin horizontal rules. Keep it quiet and precise.

The skill bundles the approved font assets below. Use the bundled files instead of searching for substitutes when the production workflow supports deterministic typesetting:

- Editorial New Vietnamese Ultra Light and Ultra Light Italic: `assets/fonts/editorial-new/`.
- Roboto variable Roman and Italic: `assets/fonts/roboto/`, together with its OFL license.

The project owner confirmed permission to package and share the supplied Editorial New files in this Naris Premium plugin. Keep those files scoped to this plugin; do not publish or redistribute them separately.

GPT Image must not draw campaign headlines, supporting copy, or logos. Generate a clean art plate and add these elements with deterministic post-typesetting. If the environment cannot run that step, report the limitation instead of returning approximate typography.

The HHVN logo is an image asset. Never recreate its lettering with a font.

## Background and decorative assets

Build the campaign field from:

- warm off-white paper/plaster texture with subtle natural fibers;
- fine pale-pink lotus or floral line art entering from edges and corners;
- an optional dry pink brush sweep along a lower edge;
- an optional pale silver-blue curved brush arc for depth;
- thin charcoal or gray rules around small headings or dividers;
- the small pink five-petal floral divider icon.

Decorative motifs should frame negative space, never compete with the person, product, copy, or logos. Use one or two motif families per post rather than every stored asset.

## Logo system

Mandatory order for new campaign posts:

1. **Naris logo on the left.**
2. **HHVN logo on the right.**

This is an explicit user-approved override of the supplied key visual's order. Do not mirror it back to the source arrangement.

Place both logos in one horizontal row, aligned optically rather than only by bounding boxes. Match their perceived visual weight, retain clear space, and keep them on a quiet high-contrast zone. A thin vertical separator is optional. Do not create a combined raster lockup that prevents future spacing or ratio adaptations; use the two approved assets while maintaining the fixed left/right order.

## Composition

- Preserve generous negative space.
- Use an editorial grid with one primary message area and one main image/product area.
- The key visual uses a wide landscape arrangement, but other ratios should adapt the hierarchy rather than crop the master layout.
- For vertical posts, place the logo row near the top, then headline/product or headline/person, with botanical motifs entering from outer edges.
- For square posts, keep the logo row compact and allow the product or authorized person to own one side or the lower half.
- Do not automatically reproduce the sample wording, sponsorship line, or English tagline; only use copy supplied for the current post.

## People

No campaign person is stored. If a post needs a beauty queen, ambassador, contestant, or model, the user must supply the exact authorized image for that post. Preserve identity, crown, clothing, pose, jewelry, and requested crop from that source. Do not invent a pageant winner, substitute a generic woman, or imply endorsement by a real person without the supplied image.

## Overrides relative to Daily

This campaign explicitly overrides Daily's cocoa-brown-led appearance with the HHVN palette of warm paper white, pageant pink, warm gold, charcoal, and pale silver-blue. It also adds lotus/floral line art, brush accents, and the paired Naris-HHVN logo row.

Daily requirements for product fidelity, exact copy, claim safety, approved logos, authorized people, refined whitespace, and restrained premium execution remain active.

## Anti-patterns

Reject busy crowns and sparkle graphics, dark gala backgrounds, neon magenta, excessive gold foil, red-carpet clichés, random Vietnamese heritage motifs, unauthorized portraits, generic beauty-pageant contestants, duplicated crowns, dense floral frames, altered logos, or a reversed HHVN-left/Naris-right logo row.
