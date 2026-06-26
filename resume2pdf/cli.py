#!/usr/bin/env python3
"""resume - Generate resume and cover letter PDFs from JSON."""

import json
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("-o", "--output-dir", type=click.Path(), default=None, help="Output directory (default: same as input)")
def main(input_file, output_dir):
    """Generate resume and cover letter PDFs from a JSON file."""
    input_path = Path(input_file)

    if output_dir is None:
        output_dir = input_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as f:
        resume = json.load(f)

    template_dir = Path(__file__).parent
    env = Environment(loader=FileSystemLoader(str(template_dir)))

    # Generate resume
    template = env.get_template("template.html")
    html_content = template.render(resume=resume)
    resume_path = output_dir / "resume.pdf"
    HTML(string=html_content).write_pdf(str(resume_path))
    click.echo(f"Resume: {resume_path}")

    # Generate cover letter if present
    if "coverLetter" in resume:
        template = env.get_template("cover_letter.html")
        html_content = template.render(resume=resume)
        cover_path = output_dir / "cover_letter.pdf"
        HTML(string=html_content).write_pdf(str(cover_path))
        click.echo(f"Cover letter: {cover_path}")


if __name__ == "__main__":
    main()
