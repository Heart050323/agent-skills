# Citation verification for LaTeX papers

Keep three layers separate: valid entry format, verified bibliographic identity, and support for the manuscript's actual claim. A local citation key or DOI is not proof of claim support.

Use the available browser or scholarly tools to locate the cited edition or version through DOI/publisher metadata, arXiv, or a trusted scholarly index. Prefer metadata from that identified source; if automatic BibTeX retrieval fails, a manually transcribed entry from verified metadata is acceptable. Do not invent missing fields or require a fixed number of search sources.

Check the title, authors, date, venue, and identifier against the version being cited. Read the relevant passage before claiming that the source supports the manuscript. Record its page/section, and distinguish an inaccessible paper from a contradictory one.

The local `scripts/verify_bib.py` helper checks common BibTeX structure and citation-key consistency. Its default offline report does not verify existence or claim support. Keep online checks within the user's authorized scope; use existing tools before proposing dependencies or a new connector.

When evidence is missing, preserve the citation anchor and report the missing verification. Do not automatically replace an existing key with an invented placeholder. Mark unresolved draft citations clearly without presenting them as real references.

For a broader document audit, use [verify-citations](../../../verify-citations/SKILL.md) if installed. Otherwise apply the same identity/metadata/claim distinction directly.

Primary references:
- [Crossref metadata API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/)
- [Semantic Scholar API](https://api.semanticscholar.org/api-docs/)
- [arXiv API](https://info.arxiv.org/help/api/basics.html)
