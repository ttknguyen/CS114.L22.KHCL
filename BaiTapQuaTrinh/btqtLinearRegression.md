# Bài Tập Quá Trình Môn Machine Learning
## Thành viên trong nhóm:
- Thái Trần Khánh Nguyên - 19520188
- Nguyễn Khánh Như - 19520209
- Đoàn Nguyễn Nhật Quang - 19520235
## Nội dung:
### Yêu cầu:
* Mỗi nhóm tìm dăm ba ví dụ về bài toán regression *****TRONG THỰC TẾ*****  
* Ghi rõ input, output và cách thu thập + xử lý data,
### Trả lời:

1.  Ví dụ 1: 
	* Bài toán: Mối quan hệ giữa tài chính (thu nhập) và hạnh phúc.
	* Mô tả: Hiện nay, hầu hết trong mọi lĩnh vực đời sống của con người đều cần phải sử dụng tiền. Nó không chỉ đáp ứng các nhu cầu về cơ sở vật chất mà còn về tinh thần của con người.
		* Input: Thu nhập bình quân của một người và yêu cầu họ xếp hạng mức độ hạnh phúc của họ trên thang điểm từ 1-10
		* Output: Mối quan hệ giữa tài chính và hạnh phúc
	* Thu thập dữ liệu: Đi khảo sát những người khác nhau (độ tuổi, giới tính, mức lương,…) để thu thập được số liệu một cách đa dạng hơn.
	* Xử lý dữ liệu: Sau khi thu thập dữ liệu, chọn lọc lại những dữ liệu phù hợp, bỏ đi những bộ sai hoặc thiếu thông tin. Sau đó chuyển các dữ liệu thu thập được vào các bảng tính để có thể đưa vào mô hình
2. Ví dụ 2: 
	* Bài toán: Dự đoán xu hướng xem loại video của người dùng
	* Mô tả: Hiện nay nhu cầu giải trí của con người trên mạng xã hội ngày càng cao. Đặc biệt, từ khi xuất hiện các nển tảng mạng xã hội về video như Tiktok, Youtube, ... Một trong những thành công của Tiktok chính là họ sử dụng những thuật toán về máy học để có thể hiểu được người dùng đang muốn xem những thể loại video nào mà từ đó đề xuất những video phù hợp cho họ.
		* Input: Danh sách thông tin về những video mà người dùng đã xem gần đây (trong vòng 1 tuần) gồm:  tiêu đề(được biểu diễn dạng string), mô tả, từ khóa(được biểu diễn dạng string), hình thu nhỏ của video(dạng hình ảnh, file png or jpg), mức độ tương tác của người dùng(chỉ số like, dislike, comment)
		* Output: Dự đoán các video mà người dùng có hứng thú
	* Thu thập dữ liệu: Thu thập các số liệu, hành vi của người dùng, những video được người dùng tương tác tốt.
	* Xử lý dữ liệu: ở mỗi video lọc ra những thông tin cần sử dụng về caption, hashtag, chủ đề, thời lượng…
3. Ví dụ 3: 
	* Bài toán: Dự đoán tình trạng sức khoẻ thông qua dữ liệu nhịp tim trong 1 tháng
	* Mô tả:
		* Input: Số nhịp đập trên 1 phút - bpm (kiểu số nguyên)
		* Output: Tình trạng cơ thể (kiểu chuỗi kí tự)
	* Thu thập dữ liệu: Thu thập chỉ số nhịp tim thông qua chức năng đo nhịp tim có sẵn trên các loại đồng hồ thông minh hoặc vòng đeo tay thông minh
	* Xử lý dữ liệu: Tạo 1 file CSV với 2 cột là chỉ số nhịp tim và thứ tự ngày trong tháng (từ ngày 1 đến ngày 30)
