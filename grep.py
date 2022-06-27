from html.parser import HTMLParser


class InstitutionFinder(HTMLParser):
    def __init__(self):
        self.last_tag = None
        self.datapoints = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.last_tag = tag

    def handle_endtag(self, tag):
        self.last_tag = None

    def handle_data(self, data):
        if self.last_tag != "td":
            return
        self.datapoints.append(data.strip())

    def get_data(self):
        for j in range(len(self.datapoints) // 2):
            yield (self.datapoints[2 * j], self.datapoints[2 * j + 1])


if __name__ == "__main__":
    with open("qrops.txt", "wt", encoding="utf-8") as fw:
        parser = InstitutionFinder()
        with open("history.html", "rt") as f:
            parser.feed(f.read())

        for a, b in parser.get_data():
            fw.write(f"{b}: {a}\n")
