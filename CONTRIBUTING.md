# Contributing to DataTalks.Club Zoomcamps Notes and Resources

Thank you for contributing to our notes and resources repository! This document provides guidelines to ensure consistency across the repository.

## Image References

When adding images to your markdown files, please follow these guidelines:

1. Place your images in the appropriate directory under `assets/images/`.
2. When referencing images in markdown files, always include the `/notes` prefix in the path.

**Correct Image Reference:**
```markdown
![Image Description](/notes/assets/images/your-path/image.png)
```

**Incorrect Image Reference:**
```markdown
![Image Description](/assets/images/your-path/image.png)
```

This is necessary because the site is configured with a baseurl of `/notes` in the `_config.yml` file. Without this prefix, images will not display correctly when the site is deployed.

## Building and Testing

To build and test the site locally:

```bash
bundle install
bundle exec jekyll serve
```

Visit `http://localhost:4000/notes/` to view the site.

## Pull Requests

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes
4. Test your changes locally
5. Submit a pull request

Thank you for helping improve our documentation! 