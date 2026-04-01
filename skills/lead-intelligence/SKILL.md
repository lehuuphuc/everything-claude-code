---
name: lead-intelligence
description: AI-native lead intelligence and outreach pipeline. Replaces Apollo, Clay, and ZoomInfo with agent-powered signal scoring, mutual ranking, warm path discovery, and personalized outreach. Use when the user wants to find, qualify, and reach high-value contacts.
origin: ECC
---

# Lead Intelligence

Agent-powered lead intelligence pipeline that finds, scores, and reaches high-value contacts through social graph analysis and warm path discovery.

## When to Activate

- User wants to find leads or prospects in a specific industry
- Building an outreach list for partnerships, sales, or fundraising
- Researching who to reach out to and the best path to reach them
- User says "find leads", "outreach list", "who should I reach out to", "warm intros"
- Needs to score or rank a list of contacts by relevance
- Wants to map mutual connections to find warm introduction paths

## Tool Requirements

### Required
- **Exa MCP** -- Deep web search for people, companies, and signals (`web_search_exa`)
- **X API** -- Follower/following graph, mutual analysis, recent activity

### Optional (enhance results)
- **LinkedIn** -- Via browser-use MCP or direct API for connection graph
- **Apollo/Clay API** -- For enrichment cross-reference if user has access
- **GitHub MCP** -- For developer-centric lead qualification

## Pipeline Overview

```
1. Signal    ->  2. Mutual    ->  3. Warm Path   ->  4. Enrich  ->  5. Outreach
   Scoring        Ranking          Discovery                         Draft
```

## Stage 1: Signal Scoring

Search for high-signal people in target verticals. Assign a weight to each based on:

| Signal | Weight | Source |
|--------|--------|--------|
| Role/title alignment | 30% | Exa, LinkedIn |
| Industry match | 25% | Exa company search |
| Recent activity on topic | 20% | X API search, Exa |
| Follower count / influence | 10% | X API |
| Location proximity | 10% | Exa, LinkedIn |
| Engagement with your content | 5% | X API interactions |

### Signal Search Approach

1. Define target parameters (verticals, roles, locations)
2. Run Exa deep search for people and companies in each vertical
3. Run X API search for active voices on relevant topics
4. Score each result against the signal weights
5. Rank and deduplicate

## Stage 2: Mutual Ranking

For each scored target, analyze the user's social graph to find the warmest path.

### Algorithm

1. Pull user's X following list and LinkedIn connections
2. For each high-signal target, check for shared connections
3. Rank mutuals by:

| Factor | Weight |
|--------|--------|
| Number of connections to targets | 40% |
| Mutual's current role/company | 20% |
| Mutual's location | 15% |
| Industry alignment | 15% |
| Mutual's identifiability (handle/profile) | 10% |

### Output Format

```
MUTUAL RANKING REPORT
=====================

#1  @mutual_handle (Score: 92)
    Name: Jane Smith
    Role: Partner @ Acme Ventures
    Location: San Francisco
    Connections to targets: 7
    Connected to: @target1, @target2, @target3, ...
    Best intro path: Jane invested in Target1's company

#2  @mutual_handle2 (Score: 85)
    ...
```

## Stage 3: Warm Path Discovery

For each target, find the shortest introduction chain:

```
You --[follows]--> Mutual A --[invested in]--> Target Company
You --[follows]--> Mutual B --[co-founded with]--> Target Person
You --[met at]--> Event --[also attended]--> Target Person
```

### Path Types (ordered by warmth)
1. **Direct mutual** -- You both follow/know the same person
2. **Portfolio connection** -- Mutual invested in or advises target's company
3. **Co-worker/alumni** -- Mutual worked at same company or attended same school
4. **Event overlap** -- Both attended same conference/program
5. **Content engagement** -- Target engaged with mutual's content or vice versa

## Stage 4: Enrichment

For each qualified lead, pull:

- Full name, current title, company
- Company size, funding stage, recent news
- Recent X posts (last 30 days): topics, tone, interests
- Mutual interests with user (shared follows, similar content)
- Recent company events (product launch, funding round, hiring)

### Enrichment Sources
- Exa: company data, news, blog posts
- X API: recent tweets, bio, followers
- GitHub: open source contributions (for developer-centric leads)
- LinkedIn (via browser-use): full profile, experience, education

## Stage 5: Outreach Draft

Generate personalized outreach for each lead. Two modes:

### Warm Intro Request (to mutual)
```
hey [mutual name],

quick ask. i see you know [target name] at [company].
i'm building [your product] which [1-line relevance to target].
would you be open to a quick intro? happy to send you a
forwardable blurb.

[your name]
```

### Direct Cold Outreach (to target)
```
hey [target name],

[specific reference to their recent work/post/announcement].
i'm [your name], building [product]. [1 line on why this is
relevant to them specifically].

[specific low-friction ask].

[your name]
```

### Anti-Patterns (never do)
- Generic templates with no personalization
- Long paragraphs explaining your whole company
- Multiple asks in one message
- Fake familiarity ("loved your recent talk!" without specifics)
- Bulk-sent messages with visible merge fields

## Configuration

Users should set these environment variables:

```bash
# Required
export X_BEARER_TOKEN="..."
export X_ACCESS_TOKEN="..."
export X_ACCESS_TOKEN_SECRET="..."
export X_API_KEY="..."
export X_API_SECRET="..."
export EXA_API_KEY="..."

# Optional
export LINKEDIN_COOKIE="..."  # For browser-use LinkedIn access
export APOLLO_API_KEY="..."   # For Apollo enrichment
```

## Related Skills

- `x-api` -- X/Twitter API integration for graph analysis
- `investor-outreach` -- Investor-specific outreach patterns
- `market-research` -- Company and fund due diligence
