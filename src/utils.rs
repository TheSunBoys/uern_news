use bytes::Bytes;
use reqwest::blocking::Response;

pub fn download_data<'a>(urls: &'a [&'a str]) -> impl Iterator<Item = Bytes> + 'a {
    urls.iter()
        .copied()
        .flat_map(reqwest::blocking::get)
        .flat_map(Response::bytes)
}
