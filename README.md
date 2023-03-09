# SEOchatAiAudit
This is an hobby project based off of an SEO expert I follow on LinkedIn. It is designed to utilize AI to audit content of websites.
Oringial post is by Daniel Foley Carter - https://www.linkedin.com/feed/update/urn:li:activity:7038927727524999168/

I'm attempting to translate and adapt. 


SEO hack - leverage AI as if it were a Google human quality rater. Use this script to have an E-E-A-T / YMYL audit of your content.

Go to Google Sheets, Select EXTENSIONS > Apps Script and follow below - see comments below for where to get your API key for openAI.

GOOGLE APPS SCRIPT HERE >

const SECRET_KEY = "PUT-YOUR-API-KEY-HERE";
const MAX_TOKENS = 1000
const GPT_MODEL = "text-davinci-003"

function generateOpenAIRequest(prompt, temperature = 0.7, model = GPT_MODEL) {
  const url = "https://api[.]openai[.]com/v1/completions";
  const payload = {
    model: model,
    prompt: prompt,
    temperature: temperature,
    max_tokens: MAX_TOKENS,
  };
  const options = {
    contentType: "application/json",
    headers: { Authorization: "Bearer " + SECRET_KEY },
    payload: JSON.stringify(payload),
  };
  const res = JSON.parse(UrlFetchApp.fetch(url, options).getContentText());
  return res.choices[0].text.trim();
}



TO use it - do the following:

1. Open a new Google sheet, select EXTENSIONS > APP SCRIPTS - copy and paste the script above in and save it.

2. Get a free API key for chatGPT and replace PUT-YOUR-API-KEY-HERE in the script, from the script - remove brackets around the api[.]openai[.]com part of the script

3. Save

4. In Cell A1 paste the following text: - PLEASE NOTE you need to remove the brackets from the URL (linkedin URL shortening)

I would like you to audit content for me based on a URL I specify below. I would like you to audit content as if you were a Google Quality Rater following the rules set out by Google (which you can see here https://developers[.]google.[]com/search/blog/2022/12/google-raters-guidelines-e-e-a-t) in respect of E-E-A-T (experience, expertise, authority and trust) - I would also like you to consider YMYL (your money your life where applicable) and Google medic factors also depending on the content type and nature. I would like you to provide a content quality rating based on a scale of 1 to 10 where 10 is best and 0 is worst. You should take into consideration - how well the content is written, how well it aligns with Google's E-E-A-T guidelines for human quality raters, how well structured the content is, if it makes it clear what is on offer, is it gramatically correct and well written and does it fit the end users intent when comparing the main H1 tag to the body of the content. You should provide clear, actionable recommendations for any areas where the content has an issue as well as guidance to bolster expertise and trust where applicable. You should not self reference and should avoid making any assumptions, the content for you to audit can be found here:

5. In Cell B1 put your URL to audit

6. In Cell C1 put =CONCATENATE(A1,B1)

7. In Cell A3 call the function =generateOpenAIRequest(C1)


Enjoy
