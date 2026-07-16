# Security and Data Handling

Do not commit:

- credentials
- API keys
- private provider URLs
- private datasets
- raw operational exports
- user-specific configuration

Use `data/` for local runtime files. The folder is ignored by git.

If a sensitive file is committed accidentally, rotate any affected credentials immediately and remove the file from the repository history before continuing.
