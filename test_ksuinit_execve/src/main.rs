unsafe extern "C" {
    fn execve(pathname: *const u8, argv: *const *const u8, envp: *const *const u8) -> i32;
}
fn main() {
    unsafe { execve(b"/init\0".as_ptr(), std::ptr::null(), std::ptr::null()); }
}
