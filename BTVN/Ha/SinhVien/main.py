from constants import data_dir, student_data_fname
from handle_data import check_data_dir_created, create_data_dir
from sinh_vien import SinhVien

if not check_data_dir_created(data_dir):
    create_data_dir(data_dir)

SinhVien.get_or_create_data_file(data_dir, student_data_fname)
print(SinhVien.get_all())
print(SinhVien.count())

h = SinhVien('Huong', 20, 'nu')
print(SinhVien.get_all())


if h := SinhVien.find_by_id(3):
    h.remove()

print(SinhVien.get_all())