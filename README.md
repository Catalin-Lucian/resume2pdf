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

Uses the [jsonresume](https://jsonresume.org/) schema with an optional `coverLetter` section:

```json
{
  "basics": {
    "name": "Your Name",
    "email": "you@email.com",
    "phone": "+1 234 567 890",
    "location": { "city": "City", "region": "Country" },
    "summary": "Brief professional summary...",
    "profiles": [
      { "network": "LinkedIn", "username": "your-profile", "url": "https://linkedin.com/in/your-profile" }
    ]
  },
  "work": [
    {
      "name": "Company",
      "position": "Role",
      "startDate": "2024-01",
      "endDate": null,
      "highlights": ["Achievement 1", "Achievement 2"]
    }
  ],
  "education": [
    {
      "institution": "University",
      "area": "Field of Study",
      "studyType": "B.Sc.",
      "startDate": "2020",
      "endDate": "2024"
    }
  ],
  "skills": [
    { "name": "Category", "keywords": ["Skill 1", "Skill 2"] }
  ],
  "projects": [
    { "name": "Project", "description": "Brief description" }
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

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
