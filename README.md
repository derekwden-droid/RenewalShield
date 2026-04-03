# RenewalShield

**AI-Powered Contract Renewal Operating System for Federal Government Contractors**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)]()
[![Next.js 15](https://img.shields.io/badge/Next.js-15-black.svg)]()
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)]()

---

## Overview

RenewalShield is a B2G SaaS platform purpose-built for government contractors who cannot afford to miss a renewal. It functions as a renewal operating system — centralizing every deadline, document, certification, and compliance obligation into a single AI-monitored workspace with multi-tenant architecture.

## The Problem

Government contractors face one of the most consequential operational challenges in business: federal contract renewals. Compliance deadlines, certification renewals, past performance documentation, and multi-agency reporting are managed across spreadsheets and institutional memory — creating costly lapses that result in lost contracts, debarment risk, and revenue gaps.

## Core Capabilities

- **Automated Lifecycle Tracking** — Deadline escalation and renewal runway alerts
- **AI Past Performance Drafting** — Generate narrative documentation from structured input
- **Certification Monitoring** — SAM.gov, CAGE, SBA, and agency-specific expiration tracking
- **Multi-Tenant Workspaces** — RBAC for contract managers, compliance officers, and executives
- **Document Vault** — Version-controlled solicitation responses and renewal submissions
- **Executive Dashboard** — Portfolio-level renewal health scores and risk flags
- **Integration-Ready** — FPDS, SAM.gov, and agency procurement portal architecture

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 15, Tailwind CSS, TypeScript |
| Backend | FastAPI, Python 3.11+ |
| Database | Supabase (PostgreSQL) |
| AI | Anthropic Claude API |
| Auth | Supabase Auth (multi-tenant RBAC) |

## Quick Start

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
cp .env.example .env.local
npm run dev
```

## Project Structure

```
├── backend/
│   └── app/
│       ├── api/v1/          # Versioned API routes
│       ├── core/            # Config, security, dependencies
│       ├── models/          # Database models
│       ├── schemas/         # Pydantic schemas
│       └── services/        # Business logic & AI services
├── frontend/
│   └── src/
│       ├── app/             # Next.js 15 app router
│       ├── components/      # React components
│       └── lib/             # API client, utilities
└── docs/
```

## Target Market

Federal government contractors, 8(a) firms, small business set-aside contractors, defense subcontractors.

## License

Proprietary — AEGIS Security, Inc. All rights reserved.

---

**Derek Denmark** — Founder & CEO, AEGIS Security, Inc. · Tampa, FL
