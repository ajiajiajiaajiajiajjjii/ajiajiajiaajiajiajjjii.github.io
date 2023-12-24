# ajiajiajiaajiajiajjjii.github.io

## Plan for minimum viable product
- [ ] Script to read from [MIUR website](https://bandi.miur.it/) and write to entries.json
- [ ]  Script to convert that into website with simple filters; we already have a version of this from Lorenzo's project so we only need to  update this.
- [ ]  Automation: do both of these automatically daily with Github Actions


## Instructions

The site can be tried locally by running 

```
jekyll serve
```

(provided `jekyll` is installed). 

The structure is as follows: 

- `entries.json` contains the raw data that is then converted into html format by running `./generate_index.sh`, which in turn calls the `add_entries.py` Python script and writes to `index.html`. In my previous project, I wrote into `entries.json` manually; here, we'd need to write a script that writes into `entries.json` by reading from the [MIUR website](https://bandi.miur.it/).
- `scripts.html` gets appended to `index.html` and contains scripts to filter the list of things.
- `_config.yml` contains configuration details of the website
- `404.md` and `about.md` are other pages in the website
- `style.scss` defines the style of the website, together with the files in `_sass/`
- `_includes/` and `layouts/` contain various html files that define how the website looks. We'll likely need to modify some of them (most likelyl `_layouts/default.html`).


## Automation

See [this](https://github.com/simulation-based-inference/simulation-based-inference.github.io/blob/main/.github/workflows/pull_paper.yml) for how to set up the automation and [this python script](https://github.com/simulation-based-inference/simulation-based-inference.github.io/blob/main/main.py) for how they do the crawling.
