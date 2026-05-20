#import necessary libraries
import xml.dom.minidom
import xml.sax
from datetime import datetime

#record results
results = {
    "molecular_function": {"max_count": -1, "go_id": "", "name": ""},
    "biological_process": {"max_count": -1, "go_id": "", "name": ""},
    "cellular_component": {"max_count": -1, "go_id": "", "name": ""}
}

#DOM
def dom_parse(xml_path):
    start = datetime.now()
    dom_tree = xml.dom.minidom.parse(xml_path)
    terms = dom_tree.getElementsByTagName("term")

    for term in terms:
        #extract id
        id_elems = term.getElementsByTagName("id")
        go_id = id_elems[0].firstChild.data if id_elems else ""

        #extract name
        name_elems = term.getElementsByTagName("name")
        name = name_elems[0].firstChild.data if name_elems else ""

        #extract namespace
        ns_elems = term.getElementsByTagName("namespace")
        ns = ns_elems[0].firstChild.data if ns_elems else ""
        if ns not in results:
            continue

        #count <is_a>
        is_a_list = term.getElementsByTagName("is_a")
        count = len(is_a_list)

        #update maximum
        if count > results[ns]["max_count"]:
            results[ns]["max_count"] = count
            results[ns]["go_id"] = go_id
            results[ns]["name"] = name

    end = datetime.now()
    return end - start

#SAX
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.go_id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "term":
            #replace by new term
            self.go_id = ""
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0

    def characters(self, content):
        #add new information
        if self.current_tag == "id":
            self.go_id += content.strip()
        elif self.current_tag == "name":
            self.name += content.strip()
        elif self.current_tag == "namespace":
            self.namespace += content.strip()
        elif self.current_tag == "is_a":
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            ns = self.namespace
            if ns in results:
                if self.is_a_count > results[ns]["max_count"]:
                    results[ns]["max_count"] = self.is_a_count
                    results[ns]["go_id"] = self.go_id
                    results[ns]["name"] = self.name
        self.current_tag = ""

def sax_parse(xml_path):
    start = datetime.now()
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_path)
    end = datetime.now()
    return end - start

if __name__ == "__main__":
    XML_FILE = "go_obo.xml"

    #clear results
    for k in results:
        results[k] = {"max_count": -1, "go_id": "", "name": ""}

    print("=== Running DOM ===")
    dom_time = dom_parse(XML_FILE)
    print("DOM spent time:", dom_time.total_seconds(), "s")
    for ns, info in results.items():
        print(f"{ns}: GO={info['go_id']}, name={info['name']}, max_is_a={info['max_count']}")

    print("\n=== Running SAX ===")
    # clear results
    for k in results:
        results[k] = {"max_count": -1, "go_id": "", "name": ""}
    sax_time = sax_parse(XML_FILE)
    print("SAX spent time:", sax_time.total_seconds(), "s")
    for ns, info in results.items():
        print(f"{ns}: GO={info['go_id']}, name={info['name']}, max_is_a={info['max_count']}")

    #compare speed
    print("\n=== Compare Speed ===")
    if sax_time < dom_time:
        print("SAX was faster")
    else:
        print("DOM was faster")