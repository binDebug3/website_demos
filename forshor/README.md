# For Shor

FastAPI-based implementation starter for the For Shor website.

## Features

- Multi-page website experience with shared navigation and footer.
- Primary pages: Home, Locations, Products and Equipment, About, Careers, Contact, FAQs.
- Utah location pages with five city-specific detail pages.
- Products page with sidebar catalog (20 popular items) and detail panel.
- Server-rendered landing page with stronger brand presentation and animated sections.
- Quote/contact lead submission forwarded to Formspree (no database, no in-memory lead storage).
- File-based gallery from local static image files.
- Expanded API and domain tests with coverage reporting. 

## Project Structure

- `src/forshor/api`: Application entrypoint, routes, and dependencies.
- `src/forshor/domain`: Core business models and services.
- `src/forshor/templates`: HTML templates.
- `src/forshor/static`: CSS and static assets.
- `tests`: Test suite.

## Formspree Configuration

Set Formspree endpoint in your environment before running:

```powershell
$env:FORSHOR_FORMSPREE_ENDPOINT="https://formspree.io/f/your_form_id"
```

If not set, form submissions are accepted by the app but not forwarded, and the UI shows an error banner.

## Gallery Images

Put gallery images in:

- `src/forshor/static/images/gallery`

Supported extensions:

- `.jpg`, `.jpeg`, `.png`, `.webp`

Filename tips for automatic category detection:

- Use `res` or `home` in filename for `Residential`.
- Use `infra` or `bridge` in filename for `Infrastructure`.
- Otherwise image defaults to `Commercial`.

If no images exist, the page shows a clear empty-state message in the gallery section.

## Additional Image Placeholders

Use these folders for location and product placeholder images:

- `src/forshor/static/images/locations`
- `src/forshor/static/images/products`

## Quick Start

```powershell
cd forshor
python -m pip install -e .[dev]
python -m uvicorn forshor.api.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Test

```powershell
cd forshor
python -m pytest
```

Generate coverage report:

```powershell
cd forshor
python -m pytest --cov=forshor --cov-report=term-missing --cov-report=html
```

HTML report is generated at `forshor/htmlcov/index.html`.

## Next Steps

- Add regional SEO pages and analytics events for call taps and form submits.
