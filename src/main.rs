use std::fs;

mod utils;

const URLS: [&str; 2] = [
    "http://portal.uern.br/blog/category/noticias/feed/",
    "https://aduern.org.br/category/noticias/feed/",
];

fn main() {
    const DATA_PATH: &str = "data";
    fs::create_dir(DATA_PATH).unwrap();
    utils::download_files(&URLS, DATA_PATH);
}
