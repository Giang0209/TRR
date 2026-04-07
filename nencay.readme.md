**Prufer Code (Nén cây)**
_Mô tả_

**Chương trình nhập một cây (n đỉnh, n-1 cạnh) và in ra mã Prufer code tương ứng.**__

_Input_
Nhập n: số đỉnh
Nhập m: số cạnh (phải = n - 1)
Nhập m cạnh dạng u v

_Output_
**In ra: Prufer code: ...**

_Ý tưởng_
Tính bậc (degree) của mỗi đỉnh
Lặp n - 2 lần:
Tìm lá nhỏ nhất (degree = 1)
Lấy đỉnh kề → thêm vào Prufer
Xóa lá, giảm bậc đỉnh kề

**Biên dịch & chạy**
gcc prufercode.c -o prufercode
./prufercode
