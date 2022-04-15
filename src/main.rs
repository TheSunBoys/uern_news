use rss::Channel;

mod utils;

const URLS: [&str; 2] = [
    "http://portal.uern.br/blog/category/noticias/feed/",
    "https://aduern.org.br/category/noticias/feed/",
];

fn main() {
    let contents = utils::download_data(&URLS);
    let channels = contents.flat_map(|c| Channel::read_from(&c[..]));

    for item in channels.flat_map(|c| c.items.into_iter().rev()) {
        let title = item.title().unwrap_or("Título não encontrado");
        let link = item.link().unwrap_or("Link não encontrado");
        let pub_date = item
            .pub_date()
            .unwrap_or("Data de publicação não encontrada");

        println!("{title}");
        println!("{link}");
        println!("{pub_date}");
        println!()
    }
}
