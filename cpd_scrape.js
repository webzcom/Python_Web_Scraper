const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://costplusdrugs.com/medications/adefovir-dipivoxil-10mg-tablet-hepsera/';

axios.get(url)
  .then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    // Assuming the JSON is embedded within a <script> tag
    const scriptTags = $('script').toArray();
    let extractedData;

    scriptTags.forEach(tag => {
      const innerHTML = $(tag).html();


      // Check if the script contains the JSON object
      if (innerHTML.includes('medicationDetails',0)) {
        console.log("line 25");

        const jsonMatch = innerHTML.match(/medicationDetails/s);
        console.log(jsonMatch + " JSON Match.");
        if (jsonMatch && jsonMatch[1]) {
          const jsonData = JSON.parse(jsonMatch[1]);
          // Access the nested data
          console.log(jsonData);
          extractedData = jsonData.props;
          console.log(extractedData + ' extracted data');
        }
      }
    });

    if (extractedData) {
      console.log(extractedData);
    } else {
      console.error('No medication details found');
    }
  })
  .catch(error => {
    console.error('Error fetching or parsing data:', error);
  });
