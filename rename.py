import os
import shutil

# 1. Update string resources for app name
app_name_old = ">KernelSU<"
app_name_new = ">krnl dot<"

for root, _, files in os.walk('manager/app/src/main/res'):
    for f in files:
        if f == 'strings.xml':
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace app_name only
            content = content.replace('<string name="app_name">KernelSU</string>', '<string name="app_name">krnl dot</string>')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# 2. Update package name in text
pkg_old = "me.weishu.kernelsu"
pkg_new = "com.rhd.krnl"
pkg_path_old = "me/weishu/kernelsu"
pkg_path_new = "com/rhd/krnl"

for root, _, files in os.walk('manager'):
    for f in files:
        if f.endswith(('.kt', '.java', '.xml', '.kts', '.pro', '.aidl')):
            path = os.path.join(root, f)
            try:
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                new_content = content.replace(pkg_old, pkg_new).replace(pkg_path_old, pkg_path_new)
                
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(new_content)
            except Exception:
                pass

# 3. Move directories
def move_dir(base_path):
    old_dir = os.path.join(base_path, 'me', 'weishu', 'kernelsu')
    new_dir = os.path.join(base_path, 'com', 'rhd', 'krnl')
    if os.path.exists(old_dir):
        os.makedirs(new_dir, exist_ok=True)
        for item in os.listdir(old_dir):
            shutil.move(os.path.join(old_dir, item), new_dir)
        # clean up old empty dirs
        os.rmdir(old_dir)
        os.rmdir(os.path.join(base_path, 'me', 'weishu'))
        os.rmdir(os.path.join(base_path, 'me'))

move_dir('manager/app/src/main/java')
move_dir('manager/app/src/main/aidl')

print("Rename complete.")
