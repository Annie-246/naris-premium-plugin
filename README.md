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

Workspace owner hoặc admin có thể import marketplace GitHub này trong phần quản trị Plugins. Khi tính năng upload plugin khả dụng, cũng có thể tải gói ZIP của thư mục `plugins/naris-premium` lên ChatGPT.

Khả năng cài đặt phụ thuộc gói ChatGPT, workspace, quyền của người dùng và bề mặt sản phẩm đang sử dụng.

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

- Daily: Editorial New, SVN-Aptima và Roboto.
- Campaign Hoa Hậu Việt Nam: Editorial New và Roboto.

GPT Image có thể mô phỏng kiểu chữ. Khi cần typography chính xác tuyệt đối, nên dùng Codex hoặc môi trường có khả năng chạy bước typesetting với các font đi kèm.

## Nội dung gói

- `plugins/naris-premium/skills/naris-premium-social-visuals`: router Daily/Campaign và guideline gốc.
- `plugins/naris-premium/skills/naris-premium-campaign-hoa-hau-viet-nam`: sub-skill HHVN 2026.
- `plugins/naris-premium/assets`: logo và ảnh giới thiệu plugin.
- `.agents/plugins/marketplace.json`: marketplace dành cho Codex/ChatGPT Desktop.

## Quyền sử dụng

Xem [LICENSE](LICENSE). Font và tài sản thương hiệu chỉ được sử dụng trong phạm vi plugin này; không tách riêng để bán hoặc phân phối lại.
