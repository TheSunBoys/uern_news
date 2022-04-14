use std::fs::File;
use std::io;

pub fn download_files(urls: &[&str], directory_save: &str) {
    for (idx, url) in urls.iter().enumerate() {
        let mut resp = reqwest::blocking::get(*url).unwrap();
        let mut out = File::create(format!("{directory_save}/file{idx}.xml")).unwrap();
        io::copy(&mut resp, &mut out).expect("failed to copy content");
    }
}
