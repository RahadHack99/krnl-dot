import os

pkg_c_old = "me_weishu_kernelsu"
pkg_c_new = "com_rhd_krnl"

for root, _, files in os.walk('manager/app/src/main/cpp'):
    for f in files:
        if f.endswith(('.cc', '.cpp', '.h')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            new_content = content.replace(pkg_c_old, pkg_c_new)
            if content != new_content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
print("JNI patched.")
