---
title: "6. GitHub Codespaces"
parent: "Module 1: Introduction to Machine Learning"
nav_order: 6
---

# GitHub Codespaces

> These notes are based on the video [ML Zoomcamp 1.6 - GitHub Codespaces](https://youtu.be/pqQFlV3f9Bo?si=dJUqRaIH8nlQHDwf)

<iframe width="560" height="315" src="https://www.youtube.com/embed/pqQFlV3f9Bo?si=dJUqRaIH8nlQHDwf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

GitHub Codespaces is a cloud-based development environment that requires minimal configuration. It provides a remote environment with most of the tools needed for the Machine Learning Zoomcamp course. The main advantages include:

- Almost no configuration required
- Remote environment with pre-installed tools
- Seamless integration with GitHub
- Accessible from anywhere

## Setting Up a Repository with Codespaces

### Creating a New Repository

1. Create a new repository on GitHub
   - Name it appropriately (e.g., "machine-learning-zoomcamp-homework")
   - Add a README file
   - Make it public
   - Add a Python .gitignore file
   - Click "Create repository"

### Launching Codespaces

1. Navigate to the repository
2. Click on the "Code" button
3. Select the "Codespaces" tab
4. Click "Create codespace on main"

This will create a Visual Studio Code instance within your browser. You can either:
- Use it directly in the browser
- Open it in VS Code desktop by clicking the button in the corner labeled "Open in VS Code Desktop"

## Working with Codespaces

### Basic Operations

- The environment feels like local development
- Files can be created and edited as usual
- Terminal is accessible via:
  - Ctrl+` (Control+Tilda)
  - View > Terminal menu

### Terminal Tips

For a cleaner terminal prompt, you can use:
```bash
PS1="> "
```
This shortens the prompt to just a ">" sign, giving you more space to see your commands.

### Git Operations

Git is pre-configured in Codespaces:
```bash
git status
git commit -am "message"
git push
```

## Installing Required Libraries

Install the necessary Python libraries using pip:

```bash
pip install jupyter numpy pandas scikit-learn seaborn
```

Additional libraries like XGBoost and TensorFlow can be installed the same way when needed.

## Using Jupyter Notebooks

### Starting Jupyter

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Codespaces automatically detects the running service on port 8888 and forwards it to your local machine.

### Accessing Jupyter

1. In Codespaces, look for the "Ports" tab
2. Find the forwarded port 8888
3. Click on the link to open Jupyter in your browser
4. Copy the token from the terminal or the full URL and paste it in the browser if prompted

### Working with Notebooks

1. Create folders for organization (e.g., "01-intro")
2. Create new notebooks
3. Import libraries and start working:
   ```python
   import pandas as pd
   df = pd.read_csv('file.csv')
   ```

## Completing and Submitting Homework

1. Create and complete your homework notebook
2. Rename files as needed (can be done directly in VS Code)
3. Commit and push your changes:
   ```bash
   git add .
   git commit -m "homework"
   git push
   ```
4. Submit the GitHub repository URL in the course homework submission form

## Additional Tips

- Install the VS Code Python extension for better Python support
- When first launching VS Code desktop, it will prompt you to install the Codespaces extension
- If not prompted, you can install it manually:
  1. Go to Extensions
  2. Search for "GitHub Codespaces"
  3. Install the extension

## Conclusion

GitHub Codespaces provides a convenient, pre-configured environment for the Machine Learning Zoomcamp course. It eliminates most setup issues and allows you to focus on learning machine learning concepts rather than environment configuration.
