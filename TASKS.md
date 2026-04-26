# Phase 4 — UX Polish Tasks

## Active

- [x] **Accessibility audit vs. WCAG 2.2 AA**
  - Automated scan: axe, WAVE, Lighthouse
  - Keyboard navigation verification
  - Color contrast check (>= 4.5:1)
  - ARIA labels and landmarks
  - Screen reader test (NVDA/VoiceOver)
  - Report: ACCESSIBILITY_AUDIT.md

- [x] **Variable-font / typography alignment**
  - Evaluate current font stack
  - Implement responsive type scale
  - Font-loading discipline (font-display: swap)
  - Reference: SF Pro, IBM Plex, Roboto Flex, Inter
  - Report: TYPOGRAPHY_REPORT.md

- [x] **Mobile-first confirmation**
  - Touch targets >= 44x44 px
  - Progressive disclosure patterns
  - Responsive breakpoints: 320, 768, 1024, 1440 px
  - Hamburger menu and collapsible sections
  - Form usability on small screens
  - Report: MOBILE_FIRST_REPORT.md

- [ ] **Speed validation (Core Web Vitals)**
  - LCP < 2.5 s
  - CLS < 0.1
  - INP < 200 ms
  - Lighthouse performance audit
  - Image optimization (WebP/AVIF, lazy loading)
  - Tailwind CSS purge/minification

## Completed Phase 4 Prep
- [x] Django admin registration for models
- [x] Superuser creation
- [x] requirements.txt / pyproject.toml
- [x] Production settings split
- [x] Static/media deployment handling
