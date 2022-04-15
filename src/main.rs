use rss::Channel;

mod utils;

const URLS: [&str; 2] = [
    "http://portal.uern.br/blog/category/noticias/feed/",
    "https://aduern.org.br/category/noticias/feed/",
];

fn main() {
    let contents = utils::download_data(&URLS);
    let channels: Vec<Channel> = contents
        .iter()
        .map(|c| Channel::read_from(&c[..]).unwrap())
        .collect();

    for item in channels.iter().flat_map(|c| c.items.iter().rev()) {
        let title = item.title().unwrap();
        let link = item.link().unwrap();
        let pub_date = item.pub_date().unwrap();

        println!("{title}");
        println!("{link}");
        println!("{pub_date}");
        println!()
    }
}
