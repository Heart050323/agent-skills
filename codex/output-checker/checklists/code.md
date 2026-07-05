# CODE checklist

Labels: 🔴 CRITICAL · 🟡 WARNING · 🔵 STYLE (severity scale in SKILL.md).

1. **Does it run?** — syntax errors, missing imports, undefined variables. Ground it: run the file or a smoke import where feasible, don't just read.
2. **Logic correctness** — trace the main flow. Does it do what was intended?
3. **Edge cases** — empty inputs, None/null, zero, negative, very large values, type mismatches.
4. **Output format** — does it return/print what the user expects?
5. **Readability** — variable names, comments, unnecessary complexity.
6. **Security** — hardcoded secrets, injection, unsafe `eval`?

If the code is clean, confirm: "✅ Logic verified — no issues found." Do not invent problems.
