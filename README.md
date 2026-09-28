# Naris Premium Social Visuals

Plugin tạo social post Naris Premium theo hai chế độ:

- **Daily:** dùng visual guideline Naris Premium gốc.
- **Campaign:** dùng sub-skill riêng cho từng chiến dịch. Bản hiện tại gồm chiến dịch **Hoa Hậu Việt Nam 2026**.

Plugin đóng gói guideline, logo, asset campaign và font tiếng Việt đã được phê duyệt. Người dùng không cần viết code: chỉ cần cài plugin, gửi ảnh sản phẩm, nội dung, tỷ lệ và chọn Daily hoặc Campaign.

## Cài bằng Codex hoặc ChatGPT Desktop

```powershell
codex plugin marketplace add Annie-246/naris-premium-plugin
codex plugin add naris-premium@naris-premium-marketplace
```

Khởi động lại ứng dụng sau khi cài. Trong cuộc trò chuyện mới, chọn plugin **Naris Premium Social Visuals** hoặc gọi bằng `@Naris Premium` nếu giao diện hỗ trợ.

## Dùng trong ChatGPT workspace

Workspace owner hoặc admin có thể import repository này tại **Workspace settings → Plugins → Add → Import marketplace**. Để nhận các commit mới trên `main`, để trống Branch hoặc nhập `main`. Sau khi một Pull Request được duyệt và merge, admin có thể vào **Marketplaces → Naris Premium → Sync now** để yêu cầu cập nhật ngay; marketplace cũng kiểm tra cập nhật tự động hằng ngày.

Khả năng cài đặt phụ thuộc gói ChatGPT, workspace, quyền của người dùng và bề mặt sản phẩm đang sử dụng.

## Quản lý và cập nhật

Người được cấp quyền GitHub có thể dùng Codex để tạo branch và Pull Request. Nhánh `main` được thiết kế để yêu cầu validation và owner approval trước khi merge. Pull Request chưa merge không làm thay đổi plugin mà mọi người đang dùng.

- Hướng dẫn người chỉnh sửa: [CONTRIBUTING.md](CONTRIBUTING.md)
- Mô hình quyền và chuyển giao: [GOVERNANCE.md](GOVERNANCE.md)
- Lịch sử phiên bản: [CHANGELOG.md](CHANGELOG.md)

## Brief tối thiểu

Gửi đủ:

1. Daily hoặc Campaign; nếu là Campaign, ghi tên chiến dịch.
2. Ảnh packshot sản phẩm cần sử dụng.
3. Nội dung chính xác phải xuất hiện trên ảnh.
4. Tỷ lệ hoặc kích thước đầu ra.
5. Reference hoặc mô tả phong cách khi skill yêu cầu.

Ví dụ:

> Campaign Hoa Hậu Việt Nam, tỷ lệ 1:1. Dùng ba packshot đính kèm. Headline: “Nâng niu làn da Việt”. Supporting copy: “Bộ 3 nước cân bằng Naris Lotion”. Bố cục sản phẩm trên podium.

## Typography

- Headline mặc định cho Daily và Campaign Hoa Hậu Việt Nam: Editorial New Ultra Light được đóng gói trong plugin.
- Supporting copy: Roboto được đóng gói trong plugin.
- SVN-Aptima chỉ được dùng khi người dùng yêu cầu rõ.

GPT Image chỉ tạo art plate không chữ. Codex đặt headline, supporting copy và logo bằng font/asset thật trong bước compositing deterministic. Nếu môi trường hiện tại không chạy được bước này, plugin phải báo giới hạn thay vì để AI vẽ lại font.

## Nội dung gói

- `plugins/naris-premium/skills/naris-premium-social-visuals`: router Daily/Campaign và guideline gốc.
- `plugins/naris-premium/skills/naris-premium-campaign-hoa-hau-viet-nam`: sub-skill HHVN 2026.
- `plugins/naris-premium/assets`: logo và ảnh giới thiệu plugin.
- `.agents/plugins/marketplace.json`: marketplace dành cho Codex/ChatGPT Desktop.

## Quyền sử dụng

Xem [LICENSE](LICENSE). Font và tài sản thương hiệu chỉ được sử dụng trong phạm vi plugin này; không tách riêng để bán hoặc phân phối lại.
