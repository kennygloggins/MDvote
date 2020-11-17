import requests
from censusAPI.censusCfg import api_key


class censusRequest:
    def __init__(
        self, host, year, dataset, api_key, state="state:*", get_vars=["NAME"]
    ):
        self.host = host
        self.year = year
        self.dataset = dataset
        self.get_vars = get_vars
        self.api_key = api_key
        self.state = state

    def chunker(self, seq, size):
        """
        break a list into chunks of requested size
        """
        return (seq[pos : pos + size] for pos in range(0, len(seq), size))

    def setURL(self, dataset) -> str:
        base_url = "/".join([self.host, self.year, dataset])
        return base_url

    def setPredicates(self, vars) -> dict:
        predicates = {}
        print(vars)
        predicates["get"] = ",".join(vars)
        predicates["for"] = self.state
        predicates["key"] = self.api_key
        return predicates

    def censusVarReq(self):  # 24 = MD
        base_url = self.setURL(self.dataset)
        predicates = self.setPredicates(self.get_vars)
        r = requests.get(base_url, params=predicates)
        result = r.json()
        result = result[4:]
        return result

    def censusMDreq(self):
        """
        Using the variables from censusVarReq(), send a request
        in chunks of 50(max limit of reqests module) with
        chunker(), and return the table information.
        """
        results = self.censusVarReq()
        for result in results:
            get_vars.append(result[0])

        # pop off last item on url ie 'variables' to be replaced
        # with actual variable id we just looked up above.
        dataset = self.dataset.split("/")
        dataset = "/".join(dataset[:-1])
        base_url = self.setURL(dataset)

        # step through the list of census variables in groups and make request
        for topics in self.chunker(get_vars[1:], 50):
            predicates = self.setPredicates(topics)
            r = requests.get(base_url, params=predicates)
            print(r.text)


################################################################################
# Test#
################################################################################
host = "https://api.census.gov/data"
year = "2019"
dataset = "acs/acs1/variables"
get_vars = ["NAME"]

dec = censusRequest(host, year, dataset, api_key, "state:24", get_vars)
dec.censusMDreq()