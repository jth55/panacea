import json
import jinja2
import subprocess


def main():
    with open("./data/patientData0.json") as f:
        data = json.load(f)

        jinja2.Template(f"""
        Hello, {data['patient'][0]['name']}!
        
        We've processed the information you have provided for us and we've decided that pandoc is terrible.
        """).stream(data).dump("out.md")

        subprocess.run(["pandoc", "/home/eric/PycharmProjects/panacea/out.md", "-f", "gfm", "--pdf-engine=wkhtmltopdf", "-o", "out.pdf"])


if __name__ == '__main__':
    main()
