use bytes::Bytes;

pub fn download_data(urls: &[&str]) -> Vec<Bytes> {
    let mut contents = Vec::with_capacity(urls.len());

    for url in urls {
        let content = reqwest::blocking::get(*url).unwrap();
        contents.push(content.bytes().unwrap());
    }
    contents
}
