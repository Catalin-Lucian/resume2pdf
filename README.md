# resume

CLI tool to generate resume and cover letter PDFs from a JSON file.

## Setup

```bash
cd resume2pdf
uv run resume ../resume.json
```

## Usage

```bash
uv run resume <input.json> [-o <output-dir>]
```

Generates `resume.pdf` and `cover_letter.pdf` (if `coverLetter` section exists) in the same directory as the input file.

## JSON Format

Uses a custom ATS-optimized schema (`schema.json`). See `resume.json` for a full example.

```json
{
  "basics": {
    "name": "Your Name",
    "label": "Senior DevOps Engineer",
    "email": "you@email.com",
    "phone": "+1 234 567 890",
    "summary": "Front-load with title + years + key skills + metrics.",
    "location": { "city": "City", "region": "Country" },
    "profiles": [
      { "network": "LinkedIn", "username": "your-profile", "url": "https://linkedin.com/in/your-profile" }
    ]
  },
  "work": [
    {
      "name": "Company",
      "position": "Role",
      "location": "City, Country",
      "startDate": "2024-01",
      "endDate": null,
      "summary": "One-line overview of responsibilities.",
      "highlights": [
        "Achievement with metric — reduced X by 25%",
        "Led Y adopted by 12+ engineers"
      ]
    }
  ],
  "skills": [
    { "name": "DevOps", "level": "Expert", "keywords": ["Jenkins", "Docker", "GitHub Actions"] }
  ],
  "education": [
    {
      "institution": "University",
      "area": "Field of Study",
      "studyType": "B.Sc.",
      "startDate": "2020",
      "endDate": "2024",
      "courses": ["Relevant Course 1", "Relevant Course 2"]
    }
  ],
  "projects": [
    { "name": "Project", "description": "Brief description", "keywords": ["Python", "Docker"] }
  ],
  "certificates": [
    { "name": "AWS Solutions Architect", "issuer": "Amazon", "date": "2024-06" }
  ],
  "languages": [
    { "language": "English", "fluency": "Native" }
  ],
  "coverLetter": {
    "date": "January 1, 2026",
    "recipient": "Hiring Manager",
    "company": "Company Name",
    "address": "123 Street, City, Country",
    "position": "Job Title",
    "opening": "Opening paragraph...",
    "body": ["Paragraph 1...", "Paragraph 2..."],
    "closing": "Closing paragraph..."
  }
}
```

## ATS Tips

- **Keywords**: Mirror the job posting's exact phrasing
- **Metrics**: Quantify achievements (e.g. "reduced by 25%", "adopted by 12+ engineers")
- **Summary**: Front-load with job title + years + key skills
- **Skills level**: Use `Master`/`Expert`/`Advanced` — ATS filters on these
- **Certificates**: High-value for ATS filtering

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
