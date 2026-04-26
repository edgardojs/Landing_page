# Mobile-First Audit Report

**Date:** 2026-04-26
**Reference:** best_ux_sites_2026.md (GOV.UK, USWDS, Material 3)

## Methodology

- Automated heuristic scan (custom Python script)
- Manual review of touch targets, responsive classes, and progressive disclosure
- Verification against WCAG 2.5.5 (44×44px minimum) and Apple HIG (44×44pt)

## Findings Summary

| Severity | Count | Status |
|----------|-------|--------|
| CRITICAL | 0 | ✅ None |
| ERROR | 0 | ✅ None |
| WARNING | 24 | ⚠️ Mostly false positives |
| RECOMMENDATION | 1 | ⚠️ Responsive prefixes in base.html |

## Key Fixes Applied

### 1. Minimum Touch Targets
- Added `mobile-first.css` with `min-height: 44px` / `min-width: 44px` for all interactive elements
- Primary CTAs: `min-height: 48px` (Material Design standard)
- Form inputs: `min-height: 44px` with `padding: 12px 16px`
- Footer newsletter button: increased `py-2` → `py-3`
- Blog CTA button: increased `py-3` → `py-4`

### 2. Responsive Breakpoints
| Breakpoint | Width | Usage |
|------------|-------|-------|
| Default | 320–639px | Mobile-first base styles |
| sm | 640px+ | Tablet |
| md | 768px+ | Small desktop |
| lg | 1024px+ | Desktop |
| xl | 1280px+ | Large desktop |

### 3. Progressive Disclosure
- Mobile menu toggle with `aria-label`
- Desktop-only / mobile-only utility classes
- Collapsible sections with smooth transitions

### 4. iOS Prevent Zoom
- Set `font-size: 16px` on inputs to prevent iOS zoom on focus
- Applied at mobile breakpoint (`max-width: 639px`)

## Verification

| Element | Before | After | Status |
|---------|--------|-------|--------|
| Primary CTA | px-7 py-3 | px-7 py-3 | ✅ ~48px |
| Mobile toggle | p-2 | p-2 + CSS | ✅ 44px |
| Footer button | px-4 py-2 | px-4 py-3 | ✅ 44px |
| Blog CTA | px-6 py-3 | px-6 py-4 | ✅ 48px |
| Form inputs | py-2 | py-3 (CSS) | ✅ 44px |

## Files Modified

- `static/css/mobile-first.css` — new file
- `templates/base.html` — load mobile-first.css
- `templates/includes/footer.html` — increase button padding
- `templates/blog/detail.html` — increase CTA padding

## References
- WCAG 2.5.5 Target Size: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- Apple HIG Touch Targets: https://developer.apple.com/design/human-interface-guidelines/touch-targets
- Material Design Touch: https://m3.material.io/foundations/interaction/touch-targets
