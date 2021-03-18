const axios = require('axios').default;
const cheerio = require('cheerio');

const baseUrl = 'https://ru.investing.com';

function parseHref(response) {
  const $ = cheerio.load(response.data);
  return $($('.js-inner-all-results-quote-item.row')[0]).attr('href');
}

export default function getTickerPage(ticker) {
  return axios.get(`${baseUrl}/search`, {
    params: {
      q: ticker,
    },
  }).then((response) => parseHref(response));
}
