# Example: How to Use Unique Names with Display Masking

## Method 1: Using display_name (requires custom navigation)

### Module Index File
```yaml
---
title: "de-zoomcamp-module-01-docker-terraform"  # Unique internal ID
display_name: "Module 1: Docker & Terraform"    # What users see
parent: "Data Engineering Zoomcamp"
nav_order: 1
---
```

### FAQ Index File  
```yaml
---
title: "de-zoomcamp-module-01-faq"              # Unique internal ID
display_name: "FAQ"                             # What users see
parent: "de-zoomcamp-module-01-docker-terraform"
nav_order: 2
---
```

### Specific FAQ Files
```yaml
---
title: "de-zoomcamp-module-01-docker-faq"      # Unique internal ID
display_name: "Docker Issues"                  # What users see  
parent: "de-zoomcamp-module-01-faq"
nav_order: 1
---
```

## Method 2: Using Jekyll's built-in hierarchy (recommended)

### Module Index File
```yaml
---
title: "DE Module 1: Docker & Terraform"       # Unique but readable
parent: "Data Engineering Zoomcamp"
nav_order: 1
---
```

### FAQ Index File
```yaml
---
title: "FAQ"                                   # Generic name is OK
parent: "DE Module 1: Docker & Terraform"     # Parent makes it unique
nav_order: 2
---
```

### Specific FAQ Files
```yaml
---
title: "Docker Issues"                         # Descriptive name
parent: "FAQ"                                  # Now unique due to hierarchy
nav_order: 1
---
```

## Method 3: Short Prefix System

### Module Index File
```yaml
---
title: "DE-M1: Docker & Terraform"            # Short prefix
parent: "Data Engineering Zoomcamp"
nav_order: 1
---
```

### FAQ Index File
```yaml
---
title: "FAQ"                                  # Generic is fine
parent: "DE-M1: Docker & Terraform"          # Unique parent
nav_order: 2
---
```

## Method 4: Using nav_title (custom implementation)

### Module Index File
```yaml
---
title: "data-engineering-zoomcamp-module-01-containerization-infrastructure-code"
nav_title: "Module 1: Docker & Terraform"
parent: "Data Engineering Zoomcamp"
nav_order: 1
---
```

This would require modifying the navigation templates to use:
`{{ node.nav_title | default: node.title }}` 