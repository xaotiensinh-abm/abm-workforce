#!/usr/bin/env node

/**
 * ABM Workforce
 * Kịch bản đồng bộ não bộ Antigravity IDE (Cross-Platform / 1-Click) 
 * Tương thích Mac, Linux, Windows CMD/Powershell 100%
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const os = require('os');

function runCmd(command, cwd) {
    try {
        execSync(command, { cwd, stdio: 'inherit' });
    } catch (error) {
        console.error(`\n❌ LỖI KHI CHẠY LỆNH: ${command}`);
        process.exit(1);
    }
}

const args = process.argv.slice(2);
const ACTION = args[0];
const REPO_URL = args[1] || "https://github.com/DungTQ87/abm-memory.git";

if (ACTION !== 'up' && ACTION !== 'down') {
    console.error("❌ Lệnh không hợp lệ. Vui lòng gọi lệnh 1-Click:\n- Up lên mây: npm run sync:up\n- Kéo về máy: npm run sync:down");
    process.exit(1);
}

// Xử lý thông minh thư mục Users của Windows lẫn Mac qua path & os lõi
const homeDir = os.homedir(); 
const antigravityDir = path.join(homeDir, '.gemini', 'antigravity');

if (!fs.existsSync(antigravityDir)) {
    fs.mkdirSync(antigravityDir, { recursive: true });
}

process.chdir(antigravityDir);

const gitPath = path.join(antigravityDir, '.git');

// KỊCH BẢN 1 CỦA MÁY MỚI
if (!fs.existsSync(gitPath)) {
    console.log("🧠 PHÁT HIỆN HỆ THỐNG CHƯA GẮN KẾT GIT (HOẶC MÁY MỚI MUA) 🧠");
    console.log(`Đang gán điểm neo vào trạm thu phát: ${REPO_URL}`);

    runCmd('git init', antigravityDir);
    runCmd('git branch -m main', antigravityDir);
    runCmd(`git remote add origin "${REPO_URL}"`, antigravityDir);

    console.log("Đang dò quét dữ liệu trên Đám Mây Mẹ...");
    let hasRemoteBranch = false;
    try {
        execSync(`git ls-remote --exit-code origin main`, { stdio: 'ignore' });
        hasRemoteBranch = true;
    } catch (e) {
        hasRemoteBranch = false;
    }

    if (hasRemoteBranch) {
        console.log("🌐 Đã tìm thấy Ý thức AI trên mây! Đang tự động tải bộ não 1-Click về máy Windows/Mac mới của sếp...");
        runCmd('git fetch origin main', antigravityDir);
        runCmd('git reset --hard origin/main', antigravityDir);
        runCmd('git branch --set-upstream-to=origin/main main', antigravityDir);
        console.log("✅ KẾT NỐI VÀ SAO CHÉP TÂM TRÍ QUA MÁY MỚI THÀNH CÔNG RỰC RỠ! SẾP CÓ THỂ MỞ WORKSPACE LÀM VIỆC TIẾP!");
        process.exit(0);
    } else {
        console.log("Kho chứa trên Github trống. Đang đẩy Dữ liệu Gốc lên Mây chặn đầu...");
        const gitignorePath = path.join(antigravityDir, '.gitignore');
        const ignoreRules = ".DS_Store\nassets/\nbrowser_recordings/\n*.bak\n";
        fs.writeFileSync(gitignorePath, ignoreRules, 'utf8');

        runCmd('git add .', antigravityDir);
        runCmd('git commit -m "Init: Khởi tạo Bộ Không Gian Ký Ức Đầu Tiên (Cross-Platform)"', antigravityDir);
        runCmd('git push -u origin main -f', antigravityDir);
        console.log("✅ KHỞI TẠO BỘ NHỚ LÊN MÂY THÀNH CÔNG TỪ SỐ 0!");
        process.exit(0);
    }
}

// KỊCH BẢN 2 LÊN MÂY CUỐI NGÀY
if (ACTION === 'up') {
    console.log("🚀 ĐANG ĐÓNG GÓI CHUYẾN Ý THỨC LÊN MÂY (Sync UP 1-Click)...");
    runCmd('git add .', antigravityDir);
    
    const timestamp = new Date().toLocaleString('vi-VN');
    
    try {
        execSync(`git commit -m "Auto sync: Kết ca làm việc - ${timestamp}"`, { cwd: antigravityDir, stdio: 'ignore' });
        console.log("Đã cập nhật thay đổi mới vào cấu trúc.");
    } catch (e) {
        console.log("Bộ nhớ tạm không có thay đổi nào mới. Vẫn sẽ đối chiếu với Mây...");
    }

    runCmd('git push origin main', antigravityDir);
    console.log("✅ KẾT THÚC CỮ LÀM VIỆC! SẾP CÓ THỂ AN TÂM TẮT MÁY. DATA ĐÃ ĐƯỢC CHỨNG THỰC.");

// KỊCH BẢN KÉO MƯỢT XUYÊN THIẾT BỊ
} else if (ACTION === 'down') {
    console.log("🌐 ĐANG KÉO DÒNG Ý THỨC ĐÊM QUA VỀ MÁY NÀY (Sync DOWN)...");
    runCmd('git pull origin main --rebase', antigravityDir);
    console.log("✅ MỚI NHẤT! Con AI đã cập nhật ký ức từ máy kia xong. Sếp Mở Chat ra nào!");
}
