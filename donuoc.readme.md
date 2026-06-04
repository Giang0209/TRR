# Water Jug Problem - DFS

## Mô tả

Ba bình có dung tích:

- 10 lít
- 7 lít
- 4 lít

Trạng thái ban đầu:

(0,7,4)

Mỗi thao tác đổ nước từ một bình sang bình khác cho đến khi:

- bình nguồn hết nước hoặc
- bình đích đầy.

## Mục tiêu

Tìm các trạng thái có:

- 2 lít trong bình 7 lít hoặc
- 2 lít trong bình 4 lít.

## Thuật toán

Sử dụng DFS trên đồ thị trạng thái.

## Biên dịch

gcc waterjug.c -o waterjug

## Chạy

waterjug < input.txt

## Kết quả

Sinh file:

dothi.dot

Vẽ ảnh:

dot -Tpng dothi.dot -o dothi.png
