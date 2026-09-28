# Quản trị Naris Premium Plugin

## Vai trò

- **Repository owner:** `@Annie-246`, chịu trách nhiệm quyền truy cập, bảo vệ `main` và quyết định phát hành.
- **CODEOWNER/reviewer:** phê duyệt nội dung thương hiệu và kỹ thuật trước khi merge.
- **Collaborator/maintainer:** được clone, tạo branch, push branch và mở Pull Request; không được bỏ qua review.
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

## Cấp quyền cho một người chỉnh sửa

Repository hiện thuộc tài khoản cá nhân `Annie-246`. Với personal repository, GitHub có hai nhóm quyền chính: **Owner** và **Collaborator**. Collaborator có thể đọc và push code, nhưng branch protection vẫn ngăn họ đưa thay đổi trực tiếp vào `main`.

### Annie mời collaborator

1. Yêu cầu người đó gửi đúng **GitHub username**; không yêu cầu mật khẩu.
2. Mở <https://github.com/Annie-246/naris-premium-plugin>.
3. Chọn **Settings**.
4. Trong mục **Access**, chọn **Collaborators** hoặc **Collaborators & teams**.
5. Chọn **Add people**.
6. Tìm đúng username, kiểm tra avatar/profile rồi gửi lời mời.
7. Người được mời phải đăng nhập GitHub và chọn **Accept invitation**.
8. Sau khi họ chấp nhận, yêu cầu họ clone repo và làm một PR thử chỉ chỉnh tài liệu.

Không cấp mật khẩu/token của `Annie-246`, không tắt branch protection và không cho maintainer tự merge PR chưa được duyệt.

### Thêm người duyệt thứ hai

Collaborator không tự động trở thành CODEOWNER. Nếu muốn người đó có thể duyệt thay Annie:

1. Xác nhận họ hiểu guideline và có thẩm quyền duyệt thương hiệu.
2. Thêm GitHub username của họ vào `.github/CODEOWNERS` bằng một Pull Request được kiểm soát.
3. Sau khi merge, kiểm tra một PR thử để chắc rằng GitHub tự request review đúng người.

Nên có ít nhất hai CODEOWNER để tránh trường hợp người mở PR cũng là reviewer duy nhất và không thể tự approve.

### Thu hồi quyền

1. Vào **Settings → Collaborators/Collaborators & teams**.
2. Tìm đúng username.
3. Chọn **Remove access** hoặc **Remove**.
4. Nếu người đó có trong `.github/CODEOWNERS`, mở PR xóa username của họ.
5. Kiểm tra các branch/PR còn mở và đổi các secret/token liên quan nếu từng được chia sẻ ngoài quy trình chuẩn.

Việc xóa collaborator chỉ thu hồi quyền truy cập; nó không xóa tên khỏi Contributors nếu người đó đã có commit trên `main`.

## Ma trận quyền thực tế

| Hành động | Người chưa được mời | Collaborator | CODEOWNER | Owner `Annie-246` |
| --- | ---: | ---: | ---: | ---: |
| Xem repo public | Có | Có | Có | Có |
| Push branch lên repo | Không | Có | Có | Có |
| Mở Pull Request | Qua fork | Có | Có | Có |
| Approve PR | Không | Có, nhưng chưa đủ nếu cần CODEOWNER | Có | Có |
| Merge khi chưa đủ điều kiện | Không | Không | Không | Không |
| Mời/xóa collaborator | Không | Không | Không | Có |
| Bấm Sync now trong ChatGPT workspace | Chỉ khi là workspace admin | Chỉ khi là workspace admin | Chỉ khi là workspace admin | Chỉ khi là workspace admin |

Quyền GitHub và quyền quản trị ChatGPT workspace là hai hệ thống riêng.

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

