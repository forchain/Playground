# Playground

## Question Bank Website

The static question bank indexes the SQL and programming projects in this
repository. Regenerate its data after adding or editing a question project:

```bash
python3 tools/build_question_bank.py
python3 -m http.server 4173 --directory site
```

Open `http://localhost:4173` to browse the generated site.
# Playground
