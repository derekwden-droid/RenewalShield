# RenewalShield — Vercel Fix Instructions

## Root Cause
This is a monorepo (`frontend/` + `backend/`). Vercel was scanning the **repo root** and finding no `package.json` with `next` in it, causing the build to fail.

## Two-Step Fix

### Step 1 — Vercel Dashboard (REQUIRED — do this first)
1. Go to [vercel.com](https://vercel.com) → your RenewalShield project
2. Click **Settings** → **General**
3. Find **Root Directory** → set it to: `frontend`
4. Click **Save**

This tells Vercel to treat `frontend/` as the project root, so it finds `package.json`, `next.config.ts`, and all build files correctly.

### Step 2 — Drop these files into your repo
Copy the entire `frontend/` folder contents from this zip into your existing `frontend/` directory.

**Files included:**
| File | Notes |
|------|-------|
| `frontend/package.json` | Next.js 15 + Supabase + Anthropic deps — **merge your existing custom deps** |
| `frontend/vercel.json` | Framework config, env var mapping |
| `frontend/next.config.ts` | TS-native config with CORS headers for FastAPI backend |
| `frontend/tsconfig.json` | Standard Next.js 15 TS config with `@/*` path alias |
| `frontend/tailwind.config.ts` | App Router content paths |
| `frontend/postcss.config.mjs` | ESM postcss config |
| `frontend/.env.example` | Env var template for Supabase + Anthropic + backend URL |

### Step 3 — Set Vercel Environment Variables
In Vercel → Settings → Environment Variables, add:
- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `ANTHROPIC_API_KEY`
- `NEXT_PUBLIC_API_URL` (your FastAPI backend URL)

### Step 4 — Push & Redeploy
```bash
git add .
git commit -m "fix: vercel monorepo config for frontend"
git push origin main
```

Vercel will auto-trigger a new deployment from the `frontend/` root.

## Verify Locally Before Pushing
```bash
cd frontend
npm install
npm run build
# Should complete cleanly before pushing
```

---
AEGIS Security, Inc. — RenewalShield
