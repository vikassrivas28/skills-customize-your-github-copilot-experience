## Project Description

This project is an educational website for sharing homework assignments and coding exercises with students. Students can browse assignments, read their instructions, and download supporting files from the portal.

## Project Structure

- `assignments/`: Each assignment has its own subfolder containing a `README.md` and, where needed, starter code or data files.
- `templates/`: Reusable templates for creating new content.
- `assets/`: Website CSS, JavaScript, images, and the assignment detail page.
- `index.html`: The static portal page. It loads course and assignment data from the root-level `config.json`.
- `config.json`: Course details, assignment metadata, due dates, and downloadable attachment definitions.

## Project Guidelines

- Maintain consistent styling across all pages by reusing the shared stylesheet in `assets/css/styles.css`.
- Keep file and folder names descriptive and organized.
- Keep assignment metadata in `config.json` consistent with the corresponding files under `assignments/`.
- Follow the existing assignment format: provide a learning objective, clearly scoped tasks, and concrete requirements; include starter files or datasets when useful.

## Educational Standards

- Make content learning-focused, with clear objectives and an appropriate difficulty level.
- Use clear, encouraging, student-friendly language.
