##  What's this?

This is a Scrapy spider to scrape Zippy's blog.

[Scrapy](https://scrapy.org/) is a web scrapping and crawling framework.

It is helpful to read the [docs](https://docs.scrapy.org/en/latest/) and go through the [tutorial](https://docs.scrapy.org/en/latest/).

## What it does

It will go through each url in `posts.csv`, and scrape the post and comments into a `json` file.

It scrapes the post's `title`, `date`, `content` and, for each comment, the comment's `author`, `date`, and `content`.

This a very crude, preliminary version. More work is needed in parsing the stylistic HTML elements in the post text, as well as links. Same for comments. Also, the text encoding needs to be aligned with whatever it actually is.


None of this should be terribly difficult to do, but it does need to be done. 

Here's an incomplete list of stuff which should probably be fleshed out and/or turned into issues:

- [ ] Parse HTML in post content and comments
    - What do we do with style tags *e.g.* `<bold>`, `<i>`, etc?
    - Parse links - both external and to other posts
- [ ] Parse dates of both posts and comments 
- [ ] Non-ASCII characters are coming as unicode code points. Encoding needs to be sorted out.
- [ ] Double-check the list in `posts.csv` is exhaustive. 
    - Alternatively, we can make Scrapy crawl the website, but since we know there won't be new posts, this seems pointless work.
- [ ] Move most of this file's contents to the wiki

## Setup

You'll need Python installed.

Everything will be a lot easier if you know how to make virtualenvs - that means *virtual environments*. These keep Python versions and packages from interfering with each other.

If you have a sane OS, i.e. not-Windows, I'd recommend [pyenv](https://github.com/pyenv/pyenv). It can easily be installed with [pyenv-installer](https://github.com/pyenv/pyenv-installer).

The following is a list of steps that will get you up and running, assuming the above.

If you do not have a sane OS, already have Python installed and/or you just don't care, you should be able to jump to step 5.

##### 0. Pre-requisites

###### pick one according to your operating system

* Ubuntu/Debian: 

```sh
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
```

* Fedora/CentOS/RHEL:

```sh
sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel \
openssl-devel xz xz-devel libffi-devel
```

* macOS:

```sh
brew install readline xz
```

##### 1. Install pyenv

```sh
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

##### 2. Install a Python version
```sh
pyenv install 2.7.14
```

##### 3. Create a virtualenv
```sh
pyenv virtualenv 2.7.14 scrapy
```

##### 4. Activate the virtualenv
```sh
pyenv activate scrapy
```

##### 5. Install project dependencies
`cd` into this project's directory and run:
```sh
pip install -r requirements.txt
```

##### 6. Run scrapy
At this point you should have a Python environment ready to run the spider. To do so, run:
```sh
scrapy crawl posts -o zippy.json
```
this will output the scrape result into a file called `zippy.json` in the current directory.

## Help

Create an issue or contact me.