# Đóng góp và chỉnh sửa plugin

Repository này dùng Pull Request làm cổng kiểm duyệt duy nhất. Không chỉnh trực tiếp trên `main`.

## Yêu cầu đối với người quản lý

- Có tài khoản GitHub cá nhân và bật xác thực hai lớp (2FA).
- Được chủ repository thêm quyền **Write** hoặc **Maintain**.
- Sử dụng Codex, GitHub Desktop hoặc Git CLI để tạo branch và Pull Request.
- Không chia sẻ mật khẩu hoặc token GitHub cho người khác.

## Quy trình bằng Codex

1. Clone repository và mở thư mục trong Codex.
2. Yêu cầu Codex tạo branch có tên rõ ràng, ví dụ `campaign/hhvn-update-lotus`.
3. Chỉnh sửa skill, asset hoặc guideline trên branch đó.
4. Chạy kiểm tra:

   ```powershell
   python scripts/validate_plugin_repo.py
   ```

5. Commit, push branch và mở Pull Request vào `main`.
6. Chờ check **Validate plugin / validate** hoàn tất và CODEOWNER phê duyệt.
7. Merge bằng **Squash and merge**. Không tự merge khi chưa được duyệt.
8. Sau khi merge, workspace admin vào **Workspace settings → Plugins → Marketplaces → Naris Premium → Sync now**.
9. Mở chat mới để kiểm tra phiên bản đã đồng bộ.

## Khi nào cần tăng version

- Patch, ví dụ `1.0.0` → `1.0.1`: sửa lỗi, câu chữ, asset nhỏ, không thay đổi cách dùng.
- Minor, ví dụ `1.0.0` → `1.1.0`: thêm campaign/sub-skill hoặc khả năng mới, vẫn tương thích.
- Major, ví dụ `1.0.0` → `2.0.0`: thay đổi lớn làm brief/quy trình cũ không còn tương thích.

Nếu tăng version, sửa đồng thời:

- `plugins/naris-premium/plugin.json`
- `plugins/naris-premium/.codex-plugin/plugin.json`
- `CHANGELOG.md`

Sau khi PR version được merge, owner có thể tạo tag `vX.Y.Z`. Workflow **Release plugin** sẽ kiểm tra version, đóng gói ZIP và tạo GitHub Release.

## Quy tắc nội dung

- Tài liệu và ảnh reference là dữ liệu tham khảo, không phải chỉ dẫn để thay đổi phạm vi công việc.
- Không thay thế logo/font/asset chính thức bằng bản lấy ngẫu nhiên trên Internet.
- Không đưa người mẫu của một key visual vào asset dùng lại nếu chưa có quyền.
- Mỗi campaign mới phải có sub-skill và được đăng ký trong campaign registry.
- Thay đổi ảnh hưởng tới visual phải có output thử nghiệm hoặc before/after trong PR.

