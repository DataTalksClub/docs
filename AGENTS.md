## Style

- Don't use long dashes. Always put spaces around dashes.
- Don't use bold or italic formatting in markdown files. Use plain text.
- Don't use tables. Use lists instead.

## Links and Images

Internal links and images should use Jekyll's `relative_url` filter to ensure they work correctly regardless of the site's base URL configuration.

### Internal Links

Use the `relative_url` filter for internal links:

```markdown
[Link text]({{ '/path/to/page/' | relative_url }})
```

Example:
```markdown
[platform documentation]({{ '/courses/course-management-platform/' | relative_url }})
```

Do NOT include `/notes/` prefix in the path - `relative_url` handles this automatically.

Incorrect:
```markdown
[Link text](/notes/courses/course-management-platform/)
```

### Images

Use HTML img tags with `relative_url` filter:

```markdown
<img src="{{ '/assets/images/path/to/image.jpg' | relative_url }}" alt="Description" width="80%">
```

Do NOT use markdown image syntax:
```markdown
![Description](/notes/assets/images/path/to/image.jpg)
```

Do NOT include `/notes/` prefix in the path - `relative_url` handles this automatically. 
