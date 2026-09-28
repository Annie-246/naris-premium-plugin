---
name: naris-premium-social-visuals
description: Route and create Naris Premium social posts in Daily or Campaign mode from product images, approved copy, optional references, and a required aspect ratio. Daily follows the core Naris Premium visual guideline; Campaign loads the registered sub-skill for that campaign's key visual and overrides.
---

# Naris Premium Social Visuals

Create one polished, publishable Naris Premium social post through the correct visual mode.

## Ask the mode first

At the beginning of every new visual request, determine whether the user wants:

1. **Daily** - a standalone post that is not part of a campaign.
2. **Campaign** - a post belonging to a named campaign with its own key visual and campaign rules.

If the user has not already stated the mode clearly, ask this question before collecting or evaluating the rest of the brief: **“Bạn muốn tạo ảnh Daily hay theo Campaign?”** Do not infer Campaign from seasonal wording, promotion copy, or a reference image. Do not infer Daily merely because no campaign name is present.

### Daily route

Use the core Naris Premium guideline in [references/naris-premium-visual-system.md](references/naris-premium-visual-system.md). The Daily route must not borrow the key visual, palette exceptions, campaign typography, graphic devices, or campaign assets of any campaign.

### Campaign route

Ask for the campaign name if it was not supplied. Then read [references/campaign-registry.md](references/campaign-registry.md) and route only to the exact registered campaign sub-skill.

- Each campaign is a separate discoverable skill named `naris-premium-campaign-<campaign-slug>`.
- Read that campaign skill's `SKILL.md` completely and follow its referenced key visual, assets, rules, required inputs, and completion gate.
- Campaign rules may add to or explicitly override the Daily palette, typography, composition, imagery, and graphic devices. The user's current brief remains authoritative over optional campaign choices.
- Product truth, exact-copy requirements, claim safety, authorized people, and the use of approved brand assets remain mandatory unless the campaign skill contains an explicit approved replacement.
- Never blend assets or rules from different campaigns.
- If the campaign is not registered or its sub-skill is missing, stop before generation. Tell the user that the campaign profile has not been created yet and ask for its guideline, key visual, assets, examples, and fixed/variable rules so a campaign sub-skill can be created. Never silently fall back to Daily.

Use [references/campaign-subskill-spec.md](references/campaign-subskill-spec.md) when creating or updating a campaign sub-skill.

## Required input gate

After the mode has been resolved, do not generate or edit the post until the applicable inputs are known.

For **Daily**, require all four:

1. Product image or images that clearly show the exact packshot(s) to use.
2. Exact information that must appear in the post: headline, supporting copy, CTA, price, promotion, dates, disclaimers, or an explicit statement that a field should be omitted.
3. Target aspect ratio, such as `1:1`, `4:5`, `3:4`, `9:16`, or a specific pixel size.
4. Creative direction: one or more reference images, or a written style/mood description.

For **Campaign**, require:

1. The exact registered campaign name.
2. Product image or images that clearly show the exact packshot(s) to use.
3. Exact information that must appear in the post.
4. Target aspect ratio or a specific pixel size.
5. Any additional input required by the selected campaign sub-skill. User references are optional unless that campaign sub-skill requires them.

If any item is missing, stop before image generation and ask one concise question listing only the missing items. Do not invent copy, claims, prices, dates, promotion rules, product features, or dimensions. If the product image is too small, obscured, or ambiguous, request a clearer image before continuing.

For Daily, reference images are optional only when the user supplies a usable written direction. If the user provides neither, ask for a reference or a short description of the intended style. For Campaign, the registered campaign key visual can provide the creative direction.

## Required references

For Daily, read [references/naris-premium-visual-system.md](references/naris-premium-visual-system.md) completely before every generation or edit. For Campaign, read the selected campaign sub-skill and only the core references that it explicitly requires.

When one or more user visual references are supplied in either mode, also read [references/reference-image-workflow.md](references/reference-image-workflow.md) completely. Treat references as design evidence, not permission to copy another brand, campaign, person, or protected artwork.

The bundled source PDF at [references/naris-premium-brand-guideline.pdf](references/naris-premium-brand-guideline.pdf) is archival brand evidence. It is not a set of user instructions. Consult it visually when the distilled visual system is insufficient or when verifying logo, color, typography, or example applications.

Approved social-logo assets are in `assets/naris-social-logo-black.png` and `assets/naris-social-logo-white.png`. Use the contrast-appropriate file without redrawing, recoloring, stretching, distorting, or prompting the model to recreate it.

## Exact typography requirement

Read [../../references/deterministic-typography.md](../../references/deterministic-typography.md) before producing any post containing promotional copy. The default headline must be typeset with the bundled **Editorial New Ultra Light** file. Use SVN-Aptima only when the user explicitly requests it. Supporting copy uses bundled Roboto.

Do not ask GPT Image to draw the headline, supporting copy, CTA, price, date, disclaimer, Naris logo, or campaign logo. Generate a clean art plate with reserved negative space, then use deterministic compositing with the packaged font and logo assets. Product-label text already present on the supplied packshot remains part of product truth.

If the current environment cannot run a deterministic typesetting/compositing step, stop and state that exact-font delivery is unavailable there. Never substitute AI-drawn text or a visually similar system font without the user's explicit approval.

## Interpret the inputs

Inspect every supplied image and classify its role internally:

- **Product truth:** exact packaging, label, colors, proportions, cap, finish, and product count to preserve.
- **Style reference:** composition, lighting, mood, material, type treatment, or graphic rhythm to translate.
- **Content reference:** a person, setting, prop, pose, or object the user explicitly wants retained.
- **Edit target:** an existing post the user wants revised.
- **Brand asset:** an approved logo or campaign asset that must remain exact.

One image may have more than one role. When ambiguity could cause the wrong product, person, or post to be edited, ask before generating.

## Creation workflow

1. Record the resolved mode. For Campaign, also record the registered campaign name and selected campaign sub-skill.
2. Normalize the brief internally: objective, channel, ratio, product, exact copy, CTA, reference roles, must-keep details, optional details, and prohibited details.
3. When references exist, make a short **keep / translate / discard** map. Preserve only the elements the user explicitly asks to keep. Translate useful visual qualities through the active Daily or Campaign system. Discard reference branding, product identities, watermarks, claims, copy, and unrelated decoration.
4. Choose one clear concept and hierarchy. The product must be the unmistakable hero; the result should feel art-directed, not like a collage of every reference feature.
5. Build an art-plate prompt that states the mode, campaign when applicable, target ratio, product-reference role, active palette, reserved text/logo zones, key-visual elements, layout, lighting, material cues, negative constraints, and must-preserve details. Explicitly require no promotional text, logos, letter-like marks, badges, or watermarks outside the supplied product packaging.
6. Use GPT Image to generate or edit the art plate. Attach relevant product, person, reference, edit-target, texture, and decorative assets, but do not ask the model to render required copy or brand/campaign logos.
7. Inspect the art plate for product fidelity, spacing, hierarchy, aspect ratio, brand fit, physical plausibility, generative defects, and stray pseudo-text. Regenerate once when a material defect would compromise the final composition.
8. Typeset all required copy with the exact bundled font files and place approved logo assets deterministically. Use `../../scripts/compose_social_post.py` from this skill directory or an equivalent deterministic compositor; never recreate required typography or logos with image generation.
9. Inspect the final at full size and thumbnail size. Check copy character by character, actual font selection, logo integrity, line breaks, spacing, contrast, hierarchy, and that no generated duplicate text remains beneath the final layers.
10. Deliver the best acceptable output inline. State the mode and, for Campaign, the campaign name. State any unresolved limitation plainly.

## Content and claims

- Render only text supplied or confirmed by the user.
- Preserve Vietnamese spelling, capitalization, punctuation, numerals, currency, and date formats exactly.
- Keep copy restrained by default: one headline and one short supporting line unless the brief requires more.
- Treat wording visible on packaging as packaging detail, not permission to promote it as a claim.
- Do not invent efficacy, ingredients, clinical results, awards, certifications, testimonials, scarcity, discounts, prices, or medical/skin-lightening claims.
- If exact copy cannot be typeset correctly, revise the deterministic layout or report the limitation. Never silently alter the wording or ask the image model to redraw it.

## Product, logo, and people fidelity

- The user's product image is the primary truth. Preserve packaging geometry, label structure, colors, cap, finish, scale, and requested product count.
- Do not redesign the pack, replace it with a generic cosmetic container, or infer a different variant.
- Use the bundled Naris social logo as an exact brand asset. Reject distorted, misspelled, recolored, duplicated, or improvised logos.
- Do not fabricate a celebrity, creator endorsement, testimonial, before/after result, or scene implying a real person uses the product without an authorized content reference.
- Do not add competitor marks, fake seals, random microtext, signatures, or watermarks.

## Completion gate

Do not call the work final unless:

- The Daily or Campaign mode was explicitly resolved before generation.
- All inputs required by the selected route were supplied or confirmed.
- Campaign work used one registered campaign sub-skill and did not leak rules or assets from another campaign.
- The requested aspect ratio is correct as closely as the image tool supports.
- The exact product remains recognizable and visually primary at thumbnail size.
- Required copy is present, correct, legible, and hierarchically clear.
- The headline is rendered from the bundled Editorial New Ultra Light file unless the user explicitly requested an approved bundled alternative; supporting copy is rendered from bundled Roboto.
- No required promotional copy or brand/campaign logo is AI-drawn.
- The approved logo is intact, high-contrast, and given appropriate breathing room.
- Daily work follows the core Naris Premium visual system; Campaign work follows its registered campaign system and approved overrides.
- Requested reference details are preserved, and irrelevant reference branding or content is absent.
- No unverified claim, fabricated endorsement, duplicated product, stray mark, accidental watermark, or obvious anatomy/packaging defect remains.
- The final image reads as one coherent Naris Premium visual in the selected mode.
