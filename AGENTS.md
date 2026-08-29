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

## CRITICAL: File Editing on Windows

### ⚠️ MANDATORY: Always Use Backslashes on Windows for File Paths

When using Edit or MultiEdit tools on Windows, you MUST use backslashes (`\`) in file paths, NOT forward slashes (`/`).

❌ WRONG - Will cause errors:
```
Edit(file_path: "D:/repos/project/file.tsx", ...)
MultiEdit(file_path: "D:/repos/project/file.tsx", ...)
```

✅ CORRECT - Always works:
```
Edit(file_path: "D:\repos\project\file.tsx", ...)
MultiEdit(file_path: "D:\repos\project\file.tsx", ...)
```

### ⚠️ "File has been unexpectedly modified" Error

If you get this error: **"File has been unexpectedly modified. Read it again before attempting to write it"**

**Root cause:** The file was modified after you last read it (by linter, formatter, git, or external process).

**Solution: Re-read the file immediately before editing:**

```bash
# 1. Read the file again
Read(file_path: "path\to\file.txt")

# 2. Then immediately edit
Edit(file_path: "path\to\file.txt", old_string="...", new_string="...")
```

**Tool requirements:**

| Tool | Rule |
|------|------|
| **Edit** | Must `Read` immediately before - `old_string` must match current content |
| **Write** | Must `Read` once per conversation before first write |

**Common triggers:**
- Linters/formatters running on save
- Git operations (checkout, merge, rebase)
- File watchers or build processes

**Tip:** If this happens repeatedly, consider disabling auto-formatting for files you're actively editing with Claude Code.
