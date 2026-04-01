---
name: pmx-guidelines
description: PMX prediction markets platform development guidelines, architecture patterns, and project-specific best practices. Use when working on PMX or similar Next.js + Supabase + Solana prediction market codebases. Covers semantic search, real-money safety, deployment workflow, and design system rules.
origin: ECC
---

# PMX Prediction Markets - Development Guidelines

Project-specific development guidelines, architectural patterns, and critical rules for prediction market platforms handling real money.

## When to Activate

- Working on a prediction markets platform
- Building a Next.js + Supabase + Solana application that handles real money
- Implementing semantic search with Redis + OpenAI embeddings
- Following strict deployment workflows (no direct push to production)
- User references PMX or a similar prediction market codebase

## Core Principles

### 1. Real Money Safety
This platform handles real money for real users.
- ONE person does all code review and production deployments
- Bugs mean financial losses. Test everything.
- NEVER push until EVERYTHING is bulletproof

### 2. Many Small Files > Few Large Files
- High cohesion, low coupling
- Files: 200-400 lines typical, 800 max
- Extract utilities from large components
- Organize by feature/domain, not by code type

### 3. No Emojis in Codebase
- Never in documentation, code comments, console output, or error messages
- Use clear text: "SUCCESS:" not checkmarks, "ERROR:" not X marks

### 4. Single README.md for All Documentation
- All documentation in ONE file: `README.md`
- Use collapsible sections for organization
- No separate .md files (except CLAUDE.md)

### 5. Immutability in JavaScript/TypeScript
Always create new objects, never mutate:

```javascript
// WRONG: Mutating original object
async function fetchWithRetry(url, options) {
  options.headers['Authorization'] = newToken  // MUTATION
  response = await fetch(url, options)
}

// CORRECT: Create new object
async function fetchWithRetry(url, options) {
  const retryOptions = {
    ...options,
    headers: {
      ...options.headers,
      Authorization: `Bearer ${newToken}`
    }
  }
  response = await fetch(url, retryOptions)
}
```

## Tech Stack

- **Frontend**: Next.js 15, React 19, TypeScript
- **Database**: Supabase PostgreSQL
- **Blockchain**: Solana Web3.js
- **Authentication**: Privy (@privy-io/react-auth)
- **UI**: Tailwind CSS + Three.js
- **Search**: Redis Stack + OpenAI embeddings (semantic search)
- **Trading**: Meteora CP-AMM SDK
- **Charts**: Lightweight Charts + Recharts

## Semantic Search System

### Architecture (Mandatory Pattern)
```
User Query -> Debounce (500ms) -> Generate Embedding (OpenAI) ->
Vector Search (Redis KNN) -> Fetch Data (Supabase) ->
Sort by Similarity -> Results Displayed
```

### Performance
- ~300ms average (200ms OpenAI + 10ms Redis + 50ms Supabase)
- Cost: ~$0.0001 per search
- Scales to 100K+ markets
- Automatic fallback to substring search if Redis unavailable

### Critical Implementation Rule
Always use the useSemanticSearch hook:

```javascript
const {
  searchQuery,
  searchResults,
  isSearching,
  handleSearchChange,  // Use this, NOT setSearchQuery
  clearSearch
} = useSemanticSearch(500)

// ALWAYS check semantic search is enabled
if (isSemanticEnabled && searchResults) {
  // Use semantic results
} else {
  // Use substring fallback
}
```

## Git Workflow (Critical)

1. Test locally FIRST
2. Commit locally only: `git commit`
3. DO NOT push upstream
4. Wait for review
5. Small commits: one logical change per commit
6. Never commit: `.env.local`, `node_modules/`, build artifacts

### Branch Strategy
- `main` (upstream) - PRODUCTION - DO NOT PUSH DIRECTLY
- `main` (fork) - Your fork - Push here for testing
- Feature branches: `fix/issue-32`, `feat/add-feature`

## Pre-Deployment Requirements (Mandatory)

1. **Comprehensive Local Testing**
   - Every feature tested manually
   - Every API endpoint tested with curl
   - Every edge case considered
   - Mobile AND desktop tested
   - No console errors anywhere

2. **Comprehensive Automated Testing**
   - Unit tests for utilities
   - Integration tests for APIs
   - E2E tests for critical flows
   - Database migration tests
   - Race condition tests

3. **Security Review**
   - No secrets exposed
   - All inputs validated
   - Authentication/authorization verified
   - Rate limiting tested

4. **Only After All Above**
   - Commit locally with detailed message
   - DO NOT push to production
   - Wait for project owner review

## CSS and Styling Rules

- **Unify styles**: Extend existing patterns, never create parallel systems
- **Tailwind first**: Prefer Tailwind utilities over custom CSS
- **One CSS file only**: `globals.css`
- **Delete unused styles immediately**

### Design System
- Background: `#0a1929`, `#1a2a3a`, `#2a3a4a`
- Primary: `#00bcd4` (cyan)
- Text: `#ffffff` (white), `#94a3b8` (gray)
- Spacing: Tailwind spacing scale (4px base)
- Typography: Inter font family
- Shadows: Subtle glows for glass-morphism

## Next.js Best Practices

- Use Next.js built-ins first: `router.back()`, `useSearchParams()`, Server Components
- Client components: `'use client'` for interactivity
- Server components: Static content, data fetching, SEO
- Proper loading states on all data-fetching components
- Dynamic imports for code splitting

## API Design

### Conventions
- Next.js API Routes pattern (route.js files)
- Authentication via Privy (JWT tokens)
- Supabase client for database operations
- Comprehensive error handling with NextResponse
- Rate limiting on search endpoints
- Caching headers for static data

### Supabase Pattern (Mandatory)
```javascript
const { data, error } = await supabase
  .from('markets')
  .select('*')
  .eq('published', true)

if (error) {
  console.error('Supabase error:', error)
  return NextResponse.json({ success: false, error: error.message }, { status: 500 })
}

return NextResponse.json({ success: true, data })
```

## Security

- All API keys server-side only
- Input validation on all API routes
- Sanitize user inputs before queries
- Use Supabase RLS (Row Level Security)
- Rate limiting on expensive operations
- HTTPS everywhere in production
- Never hardcode secrets (Supabase URLs, OpenAI keys, Redis connection strings)

**Remember**: This handles real money. Reliability and correctness are paramount. Test everything. Never push directly to production.
