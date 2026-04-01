---
name: oura-health
description: Oura Ring health data sync, analysis, and wellness reporting via the Oura API v2. Sleep, readiness, activity, HRV, heart rate, SpO2, stress, and resilience tracking with automated sync and trend analysis. Use when the user wants health data, sleep scores, recovery metrics, or wellness reports from their Oura Ring.
origin: ECC
---

# Oura Health Operations

Sync, analyze, and report on health data from the Oura Ring via the Oura API v2.

## When to Activate

- User asks about sleep quality, readiness, recovery, activity, or health stats
- Generating wellness reports or trend analysis
- Syncing Oura data to local storage or knowledge base
- User says "how did I sleep", "my health stats", "wellness report", "check my Oura", "am I recovered"
- Any Oura API interaction or biometric data analysis

## Authentication

Oura uses OAuth2. Store credentials in environment variables or a `.env` file:

```bash
export OURA_CLIENT_ID="your-client-id"
export OURA_CLIENT_SECRET="your-client-secret"
export OURA_ACCESS_TOKEN="your-access-token"
export OURA_REFRESH_TOKEN="your-refresh-token"
```

### Token Refresh

If the access token is expired, refresh it:

```bash
curl -X POST "https://api.ouraring.com/oauth/token" \
  -d "grant_type=refresh_token" \
  -d "refresh_token=$OURA_REFRESH_TOKEN" \
  -d "client_id=$OURA_CLIENT_ID" \
  -d "client_secret=$OURA_CLIENT_SECRET"
```

Update your `.env` with the new tokens after refresh.

## API Endpoints (v2)

Base URL: `https://api.ouraring.com/v2/usercollection/`

| Endpoint | Data |
|----------|------|
| `daily_sleep` | Sleep score, total sleep, deep/REM/light, efficiency, latency |
| `daily_activity` | Activity score, steps, calories, active time, sedentary time |
| `daily_readiness` | Readiness score, HRV balance, body temp, recovery index |
| `daily_spo2` | Blood oxygen levels |
| `daily_stress` | Stress levels throughout the day |
| `daily_resilience` | Resilience score and contributing factors |
| `heart_rate` | Continuous heart rate data |
| `sleep` | Detailed sleep periods with phases |
| `workout` | Exercise sessions |
| `daily_cardiovascular_age` | Cardio age estimate |

All endpoints accept `start_date` and `end_date` query params (YYYY-MM-DD format).

### Example API Call

```bash
curl -H "Authorization: Bearer $OURA_ACCESS_TOKEN" \
  "https://api.ouraring.com/v2/usercollection/daily_sleep?start_date=2026-03-25&end_date=2026-03-31"
```

```python
import os, requests

headers = {"Authorization": f"Bearer {os.environ['OURA_ACCESS_TOKEN']}"}
params = {"start_date": "2026-03-25", "end_date": "2026-03-31"}

resp = requests.get(
    "https://api.ouraring.com/v2/usercollection/daily_sleep",
    headers=headers, params=params
)
data = resp.json()["data"]
```

## Wellness Report Format

When generating health summaries, use this structure:

1. **Overall Status** -- composite of sleep + readiness + activity scores
2. **Sleep Quality** -- total sleep, deep sleep %, REM %, efficiency, sleep debt
3. **Recovery** -- readiness score, HRV trend, resting HR, body temperature deviation
4. **Activity** -- steps, active calories, goal progress
5. **Trends** -- 7-day rolling averages for key metrics
6. **Recommendations** -- 1-2 actionable suggestions based on the data

Keep it concise. Numbers and insights, not paragraphs.

### Example Output

```
WELLNESS REPORT (Mar 25-31)
===========================

Overall: GOOD (avg readiness 78, sleep 82, activity 71)

Sleep: 7h12m avg (deep 18%, REM 22%, light 60%)
  Efficiency: 91% | Latency: 8min avg
  Sleep debt: -1h32m (improving)

Recovery: Readiness trending up (+4 over 7d)
  HRV: 42ms avg (baseline 38ms) | Resting HR: 58 bpm
  Body temp: +0.1C (normal range)

Activity: 8,420 steps/day avg | 2,180 active cal
  Goal progress: 85% | Sedentary: 9.2h avg

Recommendations:
- Deep sleep below 20%. Try earlier last meal (3h before bed).
- Activity trending down. Add a 20min walk in the afternoon.
```

## Automated Sync

Set up a daily sync cron to pull Oura data automatically:

```bash
# Example: daily sync at 10 AM
claude -p "Pull yesterday's Oura data (sleep, readiness, activity, HRV) and write a summary to memory."
```

### Sync Script Pattern

```bash
#!/bin/bash
# oura-sync.sh - Pull daily Oura data

source ~/.env.oura

# Refresh token if needed
# ... (token refresh logic)

DATE=$(date -v-1d +%Y-%m-%d)  # yesterday

for endpoint in daily_sleep daily_activity daily_readiness daily_stress; do
  curl -s -H "Authorization: Bearer $OURA_ACCESS_TOKEN" \
    "https://api.ouraring.com/v2/usercollection/${endpoint}?start_date=${DATE}&end_date=${DATE}" \
    > "oura-data/${endpoint}_${DATE}.json"
done

# Generate markdown summary from JSON files
```

## Integration with Other Skills

- Use with `knowledge-ops` to persist health trends in the knowledge base
- Use with `content-engine` to create health-related content
- Use with `autonomous-loops` for scheduled health check-ins

## Security

- Never commit Oura tokens to Git
- Store OAuth credentials in `.env` files (gitignored)
- Token auto-refresh should update the `.env` file in place
- Log functions should write to stderr to avoid polluting data pipelines
