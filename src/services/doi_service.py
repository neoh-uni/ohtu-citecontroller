import requests


class DoiService:
    def __init__(self):
        self.crossref_url = "https://api.crossref.org/works/"
        self.datacite_url = "https://api.datacite.org/works/"

    def get_doi_data(self, doi: str):
        doi, is_arxiv = self.clean_doi_url(doi)
        url = self.crossref_url + doi

        if is_arxiv:
            url = self.datacite_url + doi
            return self.get_from_datacite(self.get_request(url))
        return self.get_from_crossref(self.get_request(url))

    def get_from_datacite(self, response):
        try:
            if response["errors"][0]["status"] == "404":
                return self.not_found()
        except KeyError:
            pass
        doi_dict = response.json()
        data_dict = doi_dict["data"]["attributes"]

        input_dict = {}

        input_dict["inputAuthor"] = ", ".join(
            f"{name['given']} {name['family']}" for name in data_dict["author"]
        )
        input_dict["inputTitle"] = data_dict["title"]
        input_dict["inputYear"] = data_dict["published"]

        if data_dict["resource-type-subtype"] == "Article":
            input_dict["article"] = True
        if data_dict["resource-type-subtype"] == "Book":
            input_dict["book"] = True
            input_dict["inputPublisher"] = data_dict["container-title"]

        return input_dict

    def get_from_crossref(self, response):
        try:
            if response == "Resource not found.":
                return self.not_found()
        except KeyError:
            pass

        doi_dict = response.json()
        data_dict = doi_dict["message"]
        input_dict = {}

        input_dict["inputAuthor"] = ", ".join(
            f"{name['given']} {name['family']}" for name in data_dict["author"]
        )
        input_dict["inputTitle"] = data_dict["title"][0]
        input_dict["inputYear"] = data_dict["created"]["date-parts"][0][0]

        if data_dict["type"] == "journal-article":
            input_dict["article"] = True
        if data_dict["type"] == "monograph" or data_dict["type"] == "book-chapter":
            input_dict["book"] = True
            input_dict["inputPublisher"] = data_dict["publisher"]

        return input_dict

    def clean_doi_url(self, doi: str):
        ws_str = doi.strip()
        lower_str = ws_str.lower()
        is_arxiv = False

        if lower_str.find("arxiv") != -1:
            is_arxiv = True

        check_str = lower_str.split("/")
        if "doi.org" in check_str:
            return "/".join(check_str[3:5]), is_arxiv
        return doi, is_arxiv

    def get_request(self, api_url: str) -> dict:
        return requests.get(api_url, verify=False, timeout=10)

    def not_found(self):
        return "{'books':True, 'title': 'Resource not found.'}"


doi_service = DoiService()
