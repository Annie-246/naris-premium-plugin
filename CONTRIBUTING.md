# Đóng góp và chỉnh sửa plugin

Repository này dùng Pull Request làm cổng kiểm duyệt duy nhất. Không chỉnh trực tiếp trên `main`.

## Ai làm gì?

| Vai trò | Việc cần làm |
| --- | --- |
| Người chỉnh sửa/maintainer | Tạo branch, chỉnh file, chạy validation, push branch và mở Pull Request. |
| `Annie-246`/CODEOWNER | Đọc nội dung thay đổi, yêu cầu sửa hoặc Approve. |
| Người được phép merge | Chỉ chọn **Squash and merge** khi check đã pass và PR đã được duyệt. |
| Workspace admin | Sau khi merge, bấm **Sync now** để cập nhật plugin của workspace. |

Người chỉnh sửa cần có tài khoản GitHub riêng, nên bật xác thực hai lớp (2FA), và được `Annie-246` mời làm **Collaborator**. Không chia sẻ mật khẩu hoặc token GitHub.

## Quy trình bằng Codex — bản ngắn

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

```text
Maintainer → branch → Pull Request → validation → Annie duyệt
→ Squash and merge → Sync now → kiểm tra bằng chat mới
```

## Ví dụ đầy đủ: sửa typography campaign HHVN

Người chỉnh sửa clone repository, mở thư mục trong Codex và gửi prompt:

```text
Trong plugin Naris Premium, hãy chỉnh campaign Hoa Hậu Việt Nam:

- Headline tiếng Việt phải ưu tiên font Editorial New Bold.
- Không dùng font Light cho headline chính.
- Supporting text tiếp tục dùng Roboto.
- Không thay đổi chế độ Daily.

Hãy tạo branch: fix/hhvn-headline-bold
Sau khi chỉnh xong, chạy python scripts/validate_plugin_repo.py,
commit, push và mở Pull Request vào main.
Không tự merge Pull Request.
```

Codex phải dừng ở Pull Request. Trước khi được duyệt:

- `main` vẫn là bản chính thức cũ.
- Plugin trong workspace vẫn là bản cũ.
- Không bấm **Sync now**.

## Người chỉnh sửa kiểm tra PR trước khi gửi

Trong tab **Files changed**, kiểm tra:

- Chỉ các file đúng phạm vi yêu cầu được sửa.
- Không có logo, font hoặc asset chưa được phê duyệt.
- Không có file tạm, ảnh thử hoặc thông tin bí mật.
- Có before/after nếu thay đổi ảnh hưởng tới visual.
- Check **Validate plugin / validate** màu xanh.

Nếu Codex tạo PR hộ, yêu cầu có thể dùng nguyên văn:

```text
Hãy push branch hiện tại và mở Pull Request vào main.
Trong PR, ghi rõ nội dung thay đổi, file đã sửa, cách kiểm tra
và xác nhận không tự merge.
```

## Annie duyệt Pull Request

1. Mở tab **Pull requests** trong repository.
2. Chọn PR cần kiểm tra.
3. Đọc **Conversation**, **Commits**, **Checks** và **Files changed**.
4. Chọn **Review changes**.
5. Nếu chưa đúng, chọn **Request changes** và ghi rõ phần cần sửa.
6. Nếu đúng và check đã pass, chọn **Approve**.
7. Chọn **Squash and merge**, rồi xác nhận merge.
8. Vào workspace và bấm **Sync now** sau khi merge hoàn tất.

Nếu maintainer push thêm commit sau khi Annie đã duyệt, approval cũ sẽ bị hủy và Annie phải review lại.

> **Quan trọng:** GitHub không cho tác giả tự approve Pull Request của mình. Hiện `Annie-246` là CODEOWNER duy nhất, vì vậy quy trình bình thường là maintainer mở PR và Annie duyệt. Nếu Annie cũng cần thường xuyên mở PR, repository phải có thêm ít nhất một CODEOWNER/reviewer thứ hai.

## Khi có lỗi sau khi merge

Không sửa trực tiếp `main`. Tạo branch mới và mở PR sửa lỗi hoặc PR revert. Sau khi PR khắc phục được duyệt và merge, workspace admin bấm **Sync now** lại.

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

