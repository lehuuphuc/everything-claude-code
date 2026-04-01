---
name: knowledge-ops
description: Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.
origin: ECC
---

# Knowledge Operations

Manage a multi-layered knowledge system for ingesting, organizing, syncing, and retrieving knowledge across multiple stores.

## When to Activate

- User wants to save information to their knowledge base
- Ingesting documents, conversations, or data into structured storage
- Syncing knowledge across systems (local files, MCP memory, Supabase, Git repos)
- Deduplicating or organizing existing knowledge
- User says "save this to KB", "sync knowledge", "what do I know about X", "ingest this", "update the knowledge base"
- Any knowledge management task beyond simple memory recall

## Knowledge Architecture

### Layer 1: Claude Code Memory (Quick Access)
- **Path:** `~/.claude/projects/*/memory/`
- **Format:** Markdown files with frontmatter
- **Types:** user preferences, feedback, project context, reference
- **Use for:** Quick-access context that persists across conversations
- **Automatically loaded at session start**

### Layer 2: MCP Memory Server (Structured Knowledge Graph)
- **Access:** MCP memory tools (create_entities, create_relations, add_observations, search_nodes)
- **Use for:** Semantic search across all stored memories, relationship mapping
- **Cross-session persistence with queryable graph structure**

### Layer 3: External Data Store (Supabase, PostgreSQL, etc.)
- **Use for:** Structured data, large document storage, full-text search
- **Good for:** Documents too large for memory files, data needing SQL queries

### Layer 4: Git-Backed Knowledge Base
- **Use for:** Version-controlled knowledge, shareable context
- **Good for:** Conversation exports, session snapshots, reference documents
- **Benefits:** Full history, collaboration, backup

## Ingestion Workflow

When new knowledge needs to be captured:

### 1. Classify
What type of knowledge is it?
- Business decision -> memory file (project type) + MCP memory
- Personal preference -> memory file (user/feedback type)
- Reference info -> memory file (reference type) + MCP memory
- Large document -> external data store + summary in memory
- Conversation/session -> Git knowledge base repo

### 2. Deduplicate
Check if this knowledge already exists:
- Search memory files for existing entries
- Query MCP memory with relevant terms
- Do not create duplicates. Update existing entries instead.

### 3. Store
Write to appropriate layer(s):
- Always update Claude Code memory for quick access
- Use MCP memory for semantic searchability and relationship mapping
- Commit to Git KB for version control on major additions

### 4. Index
Update any relevant indexes or summary files.

## Sync Operations

### Conversation Sync
Periodically sync conversation history into the knowledge base:
- Sources: Claude session files, Codex sessions, other agent sessions
- Destination: Git knowledge base repo
- Generate a session index for quick browsing
- Commit and push

### Workspace State Sync
Mirror workspace configuration and scripts to the knowledge base:
- Generate directory maps
- Redact sensitive config before committing
- Track changes over time

### Cross-Source Knowledge Sync
Pull knowledge from multiple sources into one place:
- Claude/ChatGPT/Grok conversation exports
- Browser bookmarks
- GitHub activity events
- Write status summary, commit and push

## Memory Patterns

```
# Short-term: current session context
Use TodoWrite for in-session task tracking

# Medium-term: project memory files
Write to ~/.claude/projects/*/memory/ for cross-session recall

# Long-term: MCP knowledge graph
Use mcp__memory__create_entities for permanent structured data
Use mcp__memory__create_relations for relationship mapping
Use mcp__memory__add_observations for new facts about known entities
Use mcp__memory__search_nodes to find existing knowledge
```

## Best Practices

- Keep memory files concise. Archive old data rather than letting files grow unbounded.
- Use frontmatter (YAML) for metadata on all knowledge files.
- Deduplicate before storing. Search first, then create or update.
- Redact sensitive information (API keys, passwords) before committing to Git.
- Use consistent naming conventions for knowledge files (lowercase-kebab-case).
- Tag entries with topics/categories for easier retrieval.

## Quality Gate

Before completing any knowledge operation:
- no duplicate entries created
- sensitive data redacted from any Git-tracked files
- indexes and summaries updated
- appropriate storage layer chosen for the data type
- cross-references added where relevant
