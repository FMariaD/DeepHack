import urllib
import feedparser


class Parser:
    def __init__(self):
        self.base_url = "http://export.arxiv.org/api/query?"
        self.start = 0
        self.max_results = 5

    def __call__(self, search_query, max_results=None):
        """
        search top-n articles by query

        :search_query: - query
        :max_results: - max_results searched
        """
        search = "all:" + urllib.parse.quote_plus(search_query)
        if max_results is None:
            max_results = self.max_results

        query = "search_query=%s&start=%i&max_results=%i" % (
            search,
            self.start,
            max_results,
        )
        response = urllib.request.urlopen(self.base_url + query).read()
        feed = feedparser.parse(response)

        articles = []
        for entry in feed.entries:
            authors = ", ".join(author.name for author in entry.authors)
            abs_link, pdf_link = None, None
            for link in entry.links:
                if link.rel == "alternate":
                    abs_link = link.href
                elif link.title == "pdf":
                    pdf_link = link.href
            article = self.create_article(
                id=entry.id.split("/abs/")[-1],
                date=entry.published,
                title=entry.title,
                authors=authors,
                abs_link=abs_link,
                pdf_link=pdf_link,
                summary=entry.summary,
            )
            articles.append(article)

        return articles

    @staticmethod
    def preprocess_date(date):
        date = str(date)
        if 'T' in date:
            date = date[:date.find('T')]
        return date
    def create_article(self, id, date, title, authors, abs_link, pdf_link, summary):
        """
        creates a dictionary describing article with keys:

        :id: - id on arxiv.org
        :date: - date of publishing
        :title: - title of the article
        :authors: - authors
        :abs_link: - link to page on arxiv.org
        :pdf_link: - pdf link
        :summary: - summary
        """
        book = {}
        book["id"] = id
        book["date"] = self.preprocess_date(date)
        book["title"] = title
        book["authors"] = authors
        book["abs_link"] = abs_link
        book["pdf_link"] = pdf_link
        book["summary"] = summary
        return book


