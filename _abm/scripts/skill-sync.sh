#!/usr/bin/env bash
# ============================================================
# ABM Skill Sync — Single Source of Truth + Symlink
# ============================================================
# Mục đích: Đồng bộ skills từ _abm/bmm/agents/skills/ sang
#           .agents/skills/ và .gemini/skills/ bằng symlinks
#
# Sử dụng:
#   bash _abm/scripts/skill-sync.sh              # chạy bình thường
#   bash _abm/scripts/skill-sync.sh --dry-run    # chỉ xem preview
#   bash _abm/scripts/skill-sync.sh --force      # ghi đè bản thật
#   bash _abm/scripts/skill-sync.sh --verbose    # chi tiết
#   bash _abm/scripts/skill-sync.sh --clean-only # chỉ dọn dẹp
# ============================================================

set -euo pipefail

# ─── Configuration ──────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

SOURCE_DIR="$PROJECT_ROOT/_abm/bmm/agents/skills"
REGISTRY_FILE="$SOURCE_DIR/skill-registry.yaml"

# Targets — sync tới đây
TARGETS=(
    ".agents/skills"
    ".gemini/skills"
)

# Exclude patterns — không sync
EXCLUDES=(
    "_archive"
    "skill-registry.yaml"
)

# ─── CLI Arguments ──────────────────────────────────────────
DRY_RUN=false
FORCE=false
VERBOSE=false
CLEAN_ONLY=false

for arg in "$@"; do
    case "$arg" in
        --dry-run)    DRY_RUN=true ;;
        --force)      FORCE=true ;;
        --verbose)    VERBOSE=true ;;
        --clean-only) CLEAN_ONLY=true ;;
        --help)
            echo "Usage: bash skill-sync.sh [--dry-run] [--force] [--verbose] [--clean-only]"
            echo ""
            echo "  --dry-run     Preview changes without executing"
            echo "  --force       Overwrite real directories with symlinks"
            echo "  --verbose     Show detailed output"
            echo "  --clean-only  Only remove broken symlinks and empty dirs"
            exit 0
            ;;
        *)
            echo "❌ Unknown argument: $arg"
            exit 1
            ;;
    esac
done

# ─── Helpers ────────────────────────────────────────────────
log()       { echo "  $1"; }
log_v()     { $VERBOSE && echo "  📋 $1" || true; }
log_ok()    { echo "  ✅ $1"; }
log_warn()  { echo "  ⚠️  $1"; }
log_err()   { echo "  ❌ $1"; }
log_skip()  { echo "  ⏭️  $1"; }

is_excluded() {
    local name="$1"
    for exc in "${EXCLUDES[@]}"; do
        if [[ "$name" == "$exc" ]]; then
            return 0
        fi
    done
    return 1
}

# ─── Stats ──────────────────────────────────────────────────
STAT_CREATED=0
STAT_SKIPPED=0
STAT_REPLACED=0
STAT_CLEANED=0
STAT_ERRORS=0

# ─── Phase 1: Validate ─────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║       🔄 ABM Skill Sync — v1.0.0                    ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""

if [ ! -d "$SOURCE_DIR" ]; then
    log_err "Source directory not found: $SOURCE_DIR"
    exit 1
fi

# Count skills
SKILL_COUNT=0
SKILL_NAMES=()
for skill_dir in "$SOURCE_DIR"/*/; do
    [ ! -d "$skill_dir" ] && continue
    skill_name="$(basename "$skill_dir")"
    
    # Skip excluded
    if is_excluded "$skill_name"; then
        log_v "Excluded: $skill_name"
        continue
    fi
    
    # Must have SKILL.md
    if [ ! -f "$skill_dir/SKILL.md" ]; then
        log_v "No SKILL.md: $skill_name (skipped)"
        continue
    fi
    
    SKILL_NAMES+=("$skill_name")
    ((SKILL_COUNT++))
done

echo "📊 Source: $SOURCE_DIR"
echo "📊 Skills found: $SKILL_COUNT"
echo "📊 Targets: ${TARGETS[*]}"
$DRY_RUN && echo "📊 Mode: DRY RUN (no changes)" || true
$FORCE && echo "📊 Mode: FORCE (overwrite real dirs)" || true
echo ""

# ─── Phase 2: Clean ────────────────────────────────────────
echo "── Phase 1: Clean up ──────────────────────────────────"

for target in "${TARGETS[@]}"; do
    target_path="$PROJECT_ROOT/$target"
    [ ! -d "$target_path" ] && continue
    
    log "Cleaning $target/"
    
    for item in "$target_path"/*/; do
        [ ! -e "$item" ] && continue
        item_name="$(basename "$item")"
        
        # Remove broken symlinks
        if [ -L "$item" ] && [ ! -e "$item" ]; then
            log_warn "Broken symlink: $target/$item_name"
            if ! $DRY_RUN; then
                rm "$item"
                ((STAT_CLEANED++))
            fi
            continue
        fi
        
        # Remove empty directories (no files at all)
        if [ -d "$item" ] && [ ! -L "$item" ]; then
            file_count=$(find "$item" -type f 2>/dev/null | wc -l | tr -d ' ')
            if [ "$file_count" -eq 0 ]; then
                log_warn "Empty dir: $target/$item_name"
                if ! $DRY_RUN; then
                    rm -rf "$item"
                    ((STAT_CLEANED++))
                fi
            fi
        fi
    done
done

echo "  Cleaned: $STAT_CLEANED items"
echo ""

if $CLEAN_ONLY; then
    echo "── Done (clean-only mode) ─────────────────────────────"
    exit 0
fi

# ─── Phase 3: Create Symlinks ──────────────────────────────
echo "── Phase 2: Create symlinks ───────────────────────────"

for target in "${TARGETS[@]}"; do
    target_path="$PROJECT_ROOT/$target"
    
    # Create target dir if not exists
    if [ ! -d "$target_path" ]; then
        log "Creating $target/"
        if ! $DRY_RUN; then
            mkdir -p "$target_path"
        fi
    fi
    
    echo ""
    log "→ $target/"
    
    for skill_name in "${SKILL_NAMES[@]}"; do
        skill_source="$SOURCE_DIR/$skill_name"
        skill_target="$target_path/$skill_name"
        
        # Calculate relative path from target to source
        # e.g., from .agents/skills/ to _abm/bmm/agents/skills/
        rel_path="$(python3 -c "import os.path; print(os.path.relpath('$skill_source', '$target_path'))")"
        
        # Case 1: Symlink already exists and is correct
        if [ -L "$skill_target" ]; then
            existing_link="$(readlink "$skill_target")"
            if [ "$existing_link" = "$rel_path" ]; then
                log_v "OK: $skill_name (already linked)"
                ((STAT_SKIPPED++))
                continue
            else
                # Wrong target — fix it
                log_warn "Relink: $skill_name ($existing_link → $rel_path)"
                if ! $DRY_RUN; then
                    rm "$skill_target"
                    ln -s "$rel_path" "$skill_target"
                    ((STAT_REPLACED++))
                fi
                continue
            fi
        fi
        
        # Case 2: Real directory exists
        if [ -d "$skill_target" ] && [ ! -L "$skill_target" ]; then
            if $FORCE; then
                log_warn "Replace real dir: $skill_name"
                if ! $DRY_RUN; then
                    rm -rf "$skill_target"
                    ln -s "$rel_path" "$skill_target"
                    ((STAT_REPLACED++))
                fi
            else
                log_skip "$skill_name (real dir exists, use --force to replace)"
                ((STAT_SKIPPED++))
            fi
            continue
        fi
        
        # Case 3: Create new symlink
        log_ok "$skill_name → $rel_path"
        if ! $DRY_RUN; then
            ln -s "$rel_path" "$skill_target"
            ((STAT_CREATED++))
        else
            ((STAT_CREATED++))
        fi
    done
done

echo ""

# ─── Phase 4: Clean legacy .agent/skills/ ──────────────────
LEGACY_DIR="$PROJECT_ROOT/.agent/skills"
if [ -d "$LEGACY_DIR" ]; then
    echo "── Phase 3: Clean legacy .agent/skills/ ───────────────"
    legacy_count=$(find "$LEGACY_DIR" -maxdepth 1 -type d | wc -l | tr -d ' ')
    if [ "$legacy_count" -le 1 ] || $FORCE; then
        log "Removing legacy .agent/skills/"
        if ! $DRY_RUN; then
            rm -rf "$LEGACY_DIR"
            log_ok "Removed .agent/skills/"
        fi
    else
        log_skip ".agent/skills/ has content (use --force)"
    fi
    echo ""
fi

# ─── Phase 5: Update Registry ──────────────────────────────
if [ -f "$REGISTRY_FILE" ] && ! $DRY_RUN; then
    # Update last_sync and total_skills in registry
    TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
    if command -v sed &>/dev/null; then
        sed -i.bak "s/last_sync:.*/last_sync: \"$TIMESTAMP\"/" "$REGISTRY_FILE" 2>/dev/null || true
        sed -i.bak "s/total_skills:.*/total_skills: $SKILL_COUNT/" "$REGISTRY_FILE" 2>/dev/null || true
        rm -f "$REGISTRY_FILE.bak"
    fi
fi

# ─── Summary ───────────────────────────────────────────────
echo "══════════════════════════════════════════════════════"
echo "  📊 Sync Summary"
echo "──────────────────────────────────────────────────────"
echo "  Skills in source:  $SKILL_COUNT"
echo "  Symlinks created:  $STAT_CREATED"
echo "  Symlinks replaced: $STAT_REPLACED"
echo "  Skipped:           $STAT_SKIPPED"
echo "  Cleaned:           $STAT_CLEANED"
echo "  Errors:            $STAT_ERRORS"
echo "══════════════════════════════════════════════════════"
$DRY_RUN && echo "  ⚠️  DRY RUN — no changes were made" || true
echo ""
