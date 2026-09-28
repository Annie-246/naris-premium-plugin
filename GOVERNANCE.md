# Quản trị Naris Premium Plugin

## Vai trò

- **Repository owner:** `@Annie-246`, chịu trách nhiệm quyền truy cập, bảo vệ `main` và quyết định phát hành.
- **CODEOWNER/reviewer:** phê duyệt nội dung thương hiệu và kỹ thuật trước khi merge.
- **Maintainer:** được tạo branch, push branch và mở Pull Request; không được bỏ qua review.
- **Workspace admin:** import marketplace, cấu hình ai được dùng plugin và bấm **Sync now** sau khi bản cập nhật đã merge.
- **Người dùng:** sử dụng plugin; không có quyền thay đổi repository nếu không được cấp quyền GitHub.

Một người có thể giữ nhiều vai trò. Quyền dùng plugin và quyền sửa mã nguồn là hai loại quyền độc lập.

## Quy trình thay đổi

```text
Codex/maintainer → branch → Pull Request → validation → owner approval
→ merge vào main → workspace admin Sync now → người dùng mở chat mới
```

Pull Request chưa merge không được marketplace đồng bộ. Chỉ nội dung trên `main` là nguồn chính thức.

## Quy tắc bảo vệ main

- Bắt buộc Pull Request trước khi merge.
- Ít nhất 1 approval.
- Bắt buộc CODEOWNER review.
- Bắt buộc check `Validate plugin / validate` thành công.
- Hủy approval cũ khi PR có commit mới.
- Mọi discussion phải được resolve.
- Không cho force-push hoặc xóa nhánh `main`.
- Áp dụng quy tắc cho cả administrator để tránh cập nhật nhầm.

## Chuyển giao sau này

Giai đoạn đầu repository có thể thuộc tài khoản `Annie-246`. Khi cần chuyển sang quản trị doanh nghiệp, nên:

1. Tạo GitHub Organization do công ty sở hữu.
2. Thêm ít nhất hai Organization Owner dùng tài khoản riêng và bật 2FA.
3. Transfer repository sang Organization.
4. Tạo team `naris-plugin-maintainers` và team `naris-plugin-reviewers`.
5. Cập nhật `CODEOWNERS`, URL manifest và tài liệu nếu URL repository thay đổi.
6. Workspace admin import lại cùng marketplace bằng tài khoản GitHub quản trị mới nếu cần chuyển người giữ kết nối.

Không chuyển giao bằng cách đưa mật khẩu tài khoản `Annie-246` cho người khác.

## Đồng bộ và khôi phục

- Marketplace GitHub mới kiểm tra cập nhật hằng ngày; **Sync now** dùng để yêu cầu cập nhật ngay.
- Nếu bản cập nhật không hợp lệ, workspace giữ bản hoạt động gần nhất.
- Nếu một thay đổi đã merge gây lỗi thương hiệu, tạo PR revert hoặc PR sửa nóng; không sửa trực tiếp `main`.
- GitHub Release/ZIP dành cho lưu trữ hoặc cài thủ công, không tự đồng bộ.

