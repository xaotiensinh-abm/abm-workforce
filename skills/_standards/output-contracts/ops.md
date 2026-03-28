# Output Contract: Ops Domain

> Áp dụng cho tất cả skill thuộc category `ops` (W7:OpsAgent)
> Version: 1.0 | Last Updated: 2026-03-28

---

## Required Sections

Mọi ops output PHẢI có:

- [ ] **Architecture diagram** — Mermaid hoặc ASCII
- [ ] **Configuration files** — đầy đủ, annotated, không placeholder
- [ ] **Security hardening** — secrets management, network policies
- [ ] **Monitoring & alerting** — health checks, log aggregation
- [ ] **Rollback plan** — cách revert nếu deployment fail
- [ ] **Runbook** — step-by-step cho common operations

## Format Standards

| Tiêu chí | Yêu cầu |
|----------|---------|
| Diagrams | Mermaid cho architecture, flowcharts |
| Config | YAML/TOML with inline comments |
| Commands | Full command with flags, not abbreviated |
| Secrets | Placeholder `${VAR}` + .env.example |
| Ports | Documented port mapping |
| Logs | Structured JSON logging |

## Infrastructure Checklist

### Docker/Containers
- [ ] Multi-stage build (minimize image size)
- [ ] Non-root user
- [ ] Health check defined
- [ ] `.dockerignore` present
- [ ] No secrets in image layers
- [ ] Volume mounts for persistent data

### CI/CD Pipeline
- [ ] Lint → Test → Build → Deploy stages
- [ ] Secrets injected via CI variables, not committed
- [ ] Branch protection rules documented
- [ ] Rollback mechanism defined
- [ ] Deployment approval gates (production)

### Monitoring
- [ ] Health endpoint (`/health` or `/ready`)
- [ ] Structured logging (JSON)
- [ ] Error alerting (Slack/Email/PagerDuty)
- [ ] Resource utilization tracking (CPU/Memory/Disk)
- [ ] Uptime monitoring

## Self-Check Rubric (0-10)

| Dimension | Weight | Mô tả |
|-----------|:------:|-------|
| **Reliability** | 25% | High availability, auto-recovery, health checks |
| **Security** | 25% | Secrets management, network isolation, least privilege |
| **Automation** | 20% | IaC, CI/CD, zero manual steps in deploy |
| **Observability** | 15% | Logs, metrics, traces, alerting |
| **Documentation** | 15% | Runbook, architecture docs, troubleshooting guide |

### Grading Scale

| Score | Grade | Action |
|:-----:|:-----:|--------|
| 9-10 | S | Production-ready |
| 7-8 | A | Minor hardening → deploy |
| 5-6 | B | Needs security/monitoring review |
| 3-4 | C | Significant gaps — not production safe |
| 0-2 | F | Re-architect |

**Minimum threshold**: Grade A (7/10) cho production deployment.

## Environment Standards

| Environment | Purpose | Safeguards |
|-------------|---------|------------|
| `dev` | Local development | No approval needed |
| `staging` | Pre-production testing | Auto-deploy from `main` |
| `production` | Live traffic | Manual approval required |

## Anti-Patterns

```
❌ Deploy trực tiếp lên production không qua staging
   → staging test → approval → production

❌ SSH vào server để sửa config thủ công
   → IaC (Terraform/Pulumi) hoặc config management

❌ Secrets trong git repository
   → Environment variables, sealed secrets, vault

❌ Không có health check endpoint
   → /health endpoint returning {status: "ok", uptime: ...}

❌ Log toàn bộ request body (có thể chứa PII)
   → Redact sensitive fields, structured logging

❌ Single point of failure
   → Redundancy, load balancing, auto-scaling
```
