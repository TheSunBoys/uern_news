use std::io;
use std::fs::File;
use reqwest;

const URLS: [&str; 2] = [
   "http://portal.uern.br/blog/category/noticias/feed/",
   "https://aduern.org.br/category/noticias/feed/"
];

fn main() {
    for (idx, url) in URLS.into_iter().enumerate() {
        let mut resp = reqwest::blocking::get(url).unwrap();
        let mut out = File::create(format!("file{idx}.xml")).unwrap();
        io::copy(&mut resp, &mut out).expect("failed to copy content");
    }
}
