# Landing Page

A Django-based marketing website and landing-page project built with server-rendered templates, HTMX-powered form interactions, and a mobile-first UI.

## Status

**Current phase:** Phase 3 operational

What is working now:
- Public marketing pages
- Blog list/detail pages
- Newsletter signup flow
- Contact form flow
- Legal pages
- HTMX success/error interactions for newsletter and contact submissions

Recently completed:
- Phase 3 conversion-flow repair
- Canonical repo normalization and push setup
- Runtime verification of newsletter/contact/legal routes

## Stack

- **Backend:** Django 5
- **Database:** SQLite (development default)
- **Templating:** Django Templates
- **Frontend styling:** Tailwind CSS via CDN
- **Interactivity:** HTMX
- **Icons:** Font Awesome + Material Symbols

## Project Goals

This project is designed as a content/marketing website with these core goals:
- present a clear brand/message
- publish blog content
- convert visitors into newsletter subscribers
- collect contact inquiries
- remain simple to maintain without a heavy frontend framework

## Features

### Core pages
- Home
- About
- Contact
- Landing page
- Blog list
- Blog detail
- Newsletter signup
- Newsletter thanks page
- Privacy policy
- Terms of service

### Conversion flows
- Inline newsletter signup
- Landing-page CTA signup
- Footer newsletter signup
- Blog-detail newsletter CTA
- Contact form with inline validation feedback
- HTMX partial responses for success/error states

### Content/data models
- `Post`
- `Subscriber`
- `ContactMessage`

## URL Map

### Core
- `/` → home
- `/about/` → about page
- `/contact/` → contact page
- `/landing/` → focused landing page

### Blog
- `/blog/` → published posts list
- `/blog/<slug>/` → blog detail

### Newsletter
- `/newsletter/signup/` → signup page / POST endpoint
- `/newsletter/thanks/` → success page

### Legal
- `/legal/privacy/`
- `/legal/terms/`

### Admin
- `/admin/`

## Project Structure

```text
Landing_page/
├── apps/
│   ├── blog/
│   ├── core/
│   ├── legal/
│   └── newsletter/
├── project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── templates/
│   ├── base.html
│   ├── blog/
│   ├── core/
│   ├── includes/
│   ├── legal/
│   └── newsletter/
├── static/
├── manage.py
├── run.sh
└── README.md
```

## Data Models

### `Post`
Used for blog publishing.

Fields currently include:
- `title`
- `slug`
- `excerpt`
- `content`
- `featured_image`
- `is_published`
- `published_at`
- `created_at`
- `updated_at`

### `Subscriber`
Used for newsletter capture.

Fields currently include:
- `email`
- `name`
- `source`
- `created_at`
- `is_active`

### `ContactMessage`
Used for contact submissions.

Fields currently include:
- `name`
- `email`
- `subject`
- `message`
- `created_at`

## Local Development

### 1. Create a virtual environment

This repo does **not** currently commit a local `venv/`, so create your own:

```bash
cd ~/Programs/Landing_page
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

At minimum:

```bash
pip install django pillow
```

If you want reproducible installs later, add a `requirements.txt` or `pyproject.toml`.

### 3. Run migrations

```bash
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver 0.0.0.0:8000
```

Then open:

```text
http://localhost:8000/
```

## Convenience Script

A `run.sh` file exists for local startup:

```bash
./run.sh
```

Note: it expects a local `venv/` inside the repo. If you haven't created one yet, do that first.

## Validation

Useful checks:

```bash
python manage.py check
python manage.py migrate
```

Phase 3 runtime verification previously confirmed:
- valid newsletter/contact flows return `200`
- invalid HTMX submissions return `400`
- newsletter/legal pages resolve successfully

## Git

This project is tracked in the canonical repo at:

```text
~/Programs/Landing_page
```

The repo uses an SSH host alias for GitHub in this environment, but that is environment-specific and not required for all users.

## Current Gaps / Next Steps

Recommended next work:
- register `Post`, `Subscriber`, and `ContactMessage` in Django admin
- create a superuser for content management
- add a dependency manifest (`requirements.txt` or `pyproject.toml`)
- implement production settings split
- configure static/media handling for deployment
- add analytics and anti-spam controls
- perform Phase 4 UX polish
- perform Phase 5 production-readiness work

## Roadmap by Phase

### Phase 4 — UX polish
- popup behavior refinement
- accessibility pass
- responsive cleanup
- typography/spacing polish
- icon consistency review

### Phase 5 — production readiness
- PostgreSQL configuration
- environment-based secrets/settings
- static/media deployment handling
- analytics
- anti-spam controls
- deployment checklist

## License

Add a license file if this project will be distributed publicly.

## Phase 4 — UX Polish (Active)

Goals and rubric derived from `best_ux_sites_2026.md` (Drive `oc inbox`).

### Checklist

- [ ] **Accessibility audit vs. WCAG 2.2 AA**
  - Run automated scans (axe, WAVE, Lighthouse accessibility)
  - Verify keyboard navigation and focus order
  - Check color contrast ratios (minimum 4.5:1 for normal text)
  - Validate ARIA labels and landmarks
  - Test with screen reader (NVDA/VoiceOver)

- [ ] **Variable‑font / typography alignment**
  - Evaluate current font stack against references:
    - Apple SF Pro (system font, variable optical sizes)
    - IBM Plex (open-source, variable weight/width)
    - Roboto Flex (Material 3 variable font)
    - Shopify Inter / Polaris type scale
  - Implement responsive type scale with CSS custom properties
  - Ensure font-loading discipline (font-display: swap)

- [ ] **Mobile‑first confirmation**
  - Verify touch targets ≥ 44×44 px
  - Test progressive disclosure patterns
  - Confirm responsive breakpoints work at 320 px, 768 px, 1024 px, 1440 px
  - Validate hamburger menu and collapsible sections
  - Test form usability on small screens

- [ ] **Speed validation**
  - Target Core Web Vitals:
    - LCP (Largest Contentful Paint) < 2.5 s
    - CLS (Cumulative Layout Shift) < 0.1
    - INP (Interaction to Next Paint) < 200 ms
  - Run Lighthouse performance audit
  - Optimize images (WebP/AVIF, lazy loading)
  - Minimize render-blocking resources
  - Verify Tailwind CSS purge/minification

### References
- GOV.UK Design System: https://design-system.service.gov.uk/
- USWDS: https://designsystem.digital.gov/
- Material Design 3: https://m3.material.io/
- IBM Carbon: https://carbondesignsystem.com/
- Shopify Polaris: https://polaris-react.shopify.com/
