#!/bin/bash
# ============================================================
# ABM Workforce — Auto Setup Script (Mac/Linux)
# Usage: chmod +x setup.sh && ./setup.sh
# ============================================================

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Config
ABM_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$ABM_ROOT/_abm/bmm/agents/skills"
WORKFLOWS_SRC="$ABM_ROOT/.agents/workflows"
GLOBAL_DIR="$HOME/.agents"
GLOBAL_SKILLS="$GLOBAL_DIR/skills"
GLOBAL_WF="$GLOBAL_DIR/workflows"

# ============================================================
# Banner
# ============================================================
show_banner() {
    echo ""
    echo -e "${CYAN}  ╔══════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}  ║    🧠 ABM Workforce — Auto Setup        ║${NC}"
    echo -e "${CYAN}  ║    AI Business Master v9.0               ║${NC}"
    echo -e "${CYAN}  ╚══════════════════════════════════════════╝${NC}"
    echo ""
}

# ============================================================
# Check Prerequisites
# ============================================================
check_prereqs() {
    echo -e "${YELLOW}[CHECK] Kiểm tra điều kiện...${NC}"
    
    if [ ! -d "$SKILLS_SRC" ]; then
        echo -e "  ${RED}[FAIL] Không tìm thấy _abm/bmm/agents/skills/${NC}"
        echo -e "  ${RED}Hãy chạy script từ thư mục gốc ABM Workforce.${NC}"
        exit 1
    fi
    echo -e "  ${GREEN}[OK] ABM source: $ABM_ROOT${NC}"
    echo -e "  ${GREEN}[OK] Shell: $SHELL${NC}"
}

# ============================================================
# Install Skills
# ============================================================
install_skills() {
    echo ""
    echo -e "${YELLOW}[SKILLS] Cài đặt skills...${NC}"
    
    mkdir -p "$GLOBAL_SKILLS"
    
    local installed=0
    local skipped=0
    
    for skill_dir in "$SKILLS_SRC"/*/; do
        local skill_name=$(basename "$skill_dir")
        
        # Skip _archive
        if [ "$skill_name" = "_archive" ]; then
            continue
        fi
        
        local target="$GLOBAL_SKILLS/$skill_name"
        
        if [ -L "$target" ] || [ -d "$target" ]; then
            if [ "$1" = "--force" ]; then
                rm -rf "$target"
            else
                skipped=$((skipped + 1))
                continue
            fi
        fi
        
        ln -s "$skill_dir" "$target" 2>/dev/null || {
            echo -e "  ${RED}[FAIL] $skill_name${NC}"
            continue
        }
        installed=$((installed + 1))
    done
    
    echo -e "  ${GREEN}[DONE] Installed: $installed | Skipped: $skipped${NC}"
}

# ============================================================
# Install Workflows
# ============================================================
install_workflows() {
    echo ""
    echo -e "${YELLOW}[WORKFLOWS] Cài đặt workflows...${NC}"
    
    if [ ! -d "$WORKFLOWS_SRC" ]; then
        echo -e "  ${YELLOW}[SKIP] .agents/workflows/ not found${NC}"
        return
    fi
    
    mkdir -p "$GLOBAL_WF"
    
    local installed=0
    for wf_file in "$WORKFLOWS_SRC"/*.md; do
        [ -f "$wf_file" ] || continue
        cp "$wf_file" "$GLOBAL_WF/" 2>/dev/null
        installed=$((installed + 1))
    done
    
    echo -e "  ${GREEN}[DONE] $installed workflows installed${NC}"
}

# ============================================================
# Install Rules
# ============================================================
install_rules() {
    echo ""
    echo -e "${YELLOW}[RULES] Cài đặt global rules...${NC}"
    
    local global_gemini="$HOME/.gemini"
    mkdir -p "$global_gemini"
    
    local rules_file="$ABM_ROOT/_abm/RULES_GLOBAL.md"
    if [ -f "$rules_file" ]; then
        cp "$rules_file" "$global_gemini/RULES.md"
        echo -e "  ${GREEN}[DONE] Global rules → $global_gemini/RULES.md${NC}"
    else
        echo -e "  ${YELLOW}[SKIP] RULES_GLOBAL.md not found${NC}"
    fi
}

# ============================================================
# Verify
# ============================================================
verify() {
    echo ""
    echo -e "${YELLOW}[VERIFY] Kiểm tra cài đặt...${NC}"
    
    local issues=0
    
    if [ -d "$GLOBAL_SKILLS" ]; then
        local count=$(ls -d "$GLOBAL_SKILLS"/*/ 2>/dev/null | wc -l)
        echo -e "  ${GREEN}[OK] Global skills: $count${NC}"
    else
        echo -e "  ${RED}[FAIL] Global skills missing${NC}"
        issues=$((issues + 1))
    fi
    
    if [ -d "$GLOBAL_WF" ]; then
        local count=$(ls "$GLOBAL_WF"/*.md 2>/dev/null | wc -l)
        echo -e "  ${GREEN}[OK] Global workflows: $count${NC}"
    else
        echo -e "  ${RED}[FAIL] Global workflows missing${NC}"
        issues=$((issues + 1))
    fi
    
    echo ""
    if [ $issues -eq 0 ]; then
        echo -e "  ${GREEN}✅ ABM Workforce installed successfully!${NC}"
        echo -e "  ${CYAN}Gõ /jarvis trong Antigravity IDE để bắt đầu.${NC}"
    else
        echo -e "  ${YELLOW}⚠️ $issues issues found.${NC}"
    fi
}

# ============================================================
# Uninstall
# ============================================================
uninstall() {
    echo ""
    echo -e "${YELLOW}[UNINSTALL] Gỡ cài đặt ABM Workforce...${NC}"
    
    if [ -d "$GLOBAL_SKILLS" ]; then
        find "$GLOBAL_SKILLS" -maxdepth 1 -type l -delete 2>/dev/null
        echo -e "  ${GREEN}[DONE] Skill symlinks removed${NC}"
    fi
    
    if [ -d "$GLOBAL_WF" ]; then
        rm -f "$GLOBAL_WF"/*.md 2>/dev/null
        echo -e "  ${GREEN}[DONE] Workflows removed${NC}"
    fi
    
    echo -e "  ${GREEN}✅ ABM Workforce uninstalled.${NC}"
}

# ============================================================
# Main
# ============================================================
show_banner

case "${1:-install}" in
    install)
        check_prereqs
        install_skills "$2"
        install_workflows
        install_rules
        verify
        ;;
    --force)
        check_prereqs
        install_skills "--force"
        install_workflows
        install_rules
        verify
        ;;
    --verify)
        verify
        ;;
    --uninstall)
        uninstall
        ;;
    --help)
        echo "Usage: ./setup.sh [options]"
        echo ""
        echo "Options:"
        echo "  (none)       Install ABM Workforce globally"
        echo "  --force      Force reinstall (overwrite existing)"
        echo "  --verify     Check installation status"
        echo "  --uninstall  Remove ABM Workforce"
        echo "  --help       Show this help"
        ;;
    *)
        echo "Unknown option: $1. Use --help for usage."
        ;;
esac

echo ""
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}  📖 Xem README.md để biết thêm chi tiết.${NC}"
echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
