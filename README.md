Working through "Data visualization with Python and JavaScript" by Kyran Dale

Doing this in Python3 with modern JavaScript libraries (eg, lodash instead of
underscore); rather than the tools recommended in the book.

Use `conda` env "pyjsviz" (see `env/environment.yml` or `env/requirements.txt`
for details)

Libraries / tools:

- [d3.js / jQuery / lodash] from a CDN:
  - `<script src="https://d3js.org/d3.v6.min.js"></script>`
  - `<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>`
  - `<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"><\script>`
- [sqlite3] is already installed
- [ipython / jupyter] installed via conda (ipython7, jupyter-4.7)
- [pandas] 1.2.1 installed via conda
- [numpy] 1.19.5 installed via conda
- [sqlalchemy] 1.3.23 installed via conda
- [sqlite] 3.34.0 was already installed by conda
- [dataset] installed via pip
  - this also installed Mako, alembic, banal, python-editor via pip
  - banal not available through conda
  - replaced alembic/mako with conda-forge version)
  - attempted to install conda-forge python-editor but it doesn't work: after
    a seemingly successful conda-install, it is present as a pip-installed
    package when looking at `conda env export`
- [mongodb / pymongo] installed via conda
  - might be good to install mongodb via docker container when working on
    server
- [nodejs / npm] installed using `sudo apt install ...` (had to update to
  Ubuntu 18.04 before I could get a modern version of nodejs)
  - current node=8.10.0, npm=3.5.2
- [nvm] (manages nodejs versions) v 0.37.2 installed:
  - `sudo apt install build-essential checkinstall libssl-dev`
  - `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash`
  - ran `nvm ls-remote` to check available node versions
  - ran `nvm install v14.15.5` to install latest LTS version of node
- [eslint] requires node == 10.12.0 or >= 12.0.0; once 14.15.5 was installed
  through nvm:
  - ran `npm install eslint --save-dev`
  - ran `./node_modules/.bin/eslint --init`
  - used all defaults when setting up eslint (except no framework selected)
- [prettier] installed v2.2.1 using npm
  - `npm install --save-dev --save-exact prettier`
  - `echo {}> .prettierrc.json`
  - `touch .prettierignore`
  - `npx prettier -w .` to destructively style all subfiles
  - added specific files that needn't be styled to .prettierignore

Dev tools

- [pylint] / [black] from conda

# New things I learned

## Chapter 2

- CHROME: Ctrl-Shift-J to open the console
- PY: `python -m http.server <PORT>` to start a lightweight http server locally
  (the book uses the python2 equivalent: SimpleHTTPServer)
- JUPYTER: `jupyter qtconsole` to open a lightweight jupyter/ipython shell in
  qt
- JS `var`: variables declared outside of functions or missing the 'var'
  keyword are global (so may leach into other JS scripts)
- JS `use strict`: catches some typical JS errors
- PY: recommend using `logging` module instead of using `print`
- JS: variables are processed before other code, so declare variables at the
  top of each function
- JS: strings are UCS-2
- JS: only one numeric type - 64 bit doubles (with 'type'='number')
- JS: var x = {abc: 123}; here 'x' is a JS object (not a dict/hashmap)
- JS: can access elements of an object using either dot or key-string (x.abc
  === x["abc"])
- JS: two ways to define a function:
  - [function] `function f(param){};`
  - [functionexpression] `var f = function(param){};`
- JS: no default vals for function params in the parameter list (overwrite if
  undefined to achieve this) [js < ECMASCRIPT6]
- JS: no base method for iterating over k/v pairs in JS objects, use
  lodash/underscore instead
- JS: `this` == implicit reference to the 'calling context' of the function
- JS: `lodash` should be sourced (in index.html) before any `*.js` scripts that
  use it
- HTML: to add inline javascript to an .html file: <script>some_javascript;</script>
- HTML: to run code asynchronously: <script type="XYZ" src="some/path" async></script>
  but note that the order of console.logs (etc) will not be predictable
- JS: use `_.map(xs, "key")` instead of `_.pluck(xs, "key")` to pull out by
  keys from each entry in an array (pluck was removed in v4.0.0 of lodash)
- JS: use closures to allow for private variables
- JS: can also define public/private methods by returning a public api
- PY: use 'nonlocal' to define closures in python (but don't, just don't)

# Chapter 3

- PY: `pylint` fails to import modules in the same directory (so shows a lint
  when importing `nobel.NOBEL_WINNERS` from `nobel.py` into `nobel_csv.py` when
  the two .py files are in the same directory; because pylint copies things
  over to temporary directories)
- PY: `pymongo` for interacting with mongo databases
- PY: `a = some_dict.keys(); a.sort()` does not work in py3.9; `dict_keys` has
  no attribute `sort`; therefore use `a = list(some_dict.keys()); a.sort()`
- PY: (I'm sure I knew but ...) `file_writer.writelines(xs)` does not append
  newlines
- PY: `print(some_line),` with trailing comma - the book says this should print
  without any trailing newline, but it doesn't work in python 3.9.1 --
  therefore use `print(some_line.strip())`
- PY: `csv.DictWriter` for constructing a .csv from a collection of
  dictionaries.
- PY: `csv.DictReader` for constructing a list of dictionaries from a .csv
- PY: `csv.reader` reads in all data as strings (so you need to convert to
  numeric etc if reqd)
- PY: `json.dump` (`json.load`) to save (load) a collection (here, list of
  dictionaries) to json format
- PY: `json.dumps` cannot handle arbitrary classes, eg,
  `json.dumps(datetime.now())` fails; so encode them using a custom encoder
  using `json.dumps(xs, cls=CustomEncoder)`
- PY: use `datetime.datetime.strptime(date_string, format)` to decode datetimes
- PY: [sqlalchemy] database URL:
  `dialect+driver://username:password@host:port/database`
- PY: [sqlalchemy] creating database engine: `create_engine(url, echo=True)`
  (echo=True means that SQL instructions will be printed to console)
- PY: [sqlalchemy] tables represented as classes; import `declarative_base` and
  inherit from this (& sqlalchemy will work out the relationships between
  tables)
- PY: [sqlalchemy] `declarative_base().metadata.create_all(engine)` to create
  the database
- PY: [sqlalchemy] create sessions using `sessionmaker`
- PY: [sqlalchemy] `session.add()` to add to a table; use as few commits as
  possible (let sqlalchemy optimise the db access)
- PY: [sqlalchemy] `session.expunge(obj)` to remove 'obj' from the session (and
  prevent it being added to the database)
- PY: [dataset] removes boilerplate of sqlalchemy (eg, at schema definition)
- PY: [dataset] table.find() returns a collection of OrderedDicts (each
  OrderedDict being a row in the table)
- PY: [dataset] .freeze method used to allow printing sql query results to .csv
  or .json; the method has been moved to {datafreeze} and that package is
  defunct. Recommend using `pandas.to_csv` instead
- MONGO: uses binary json for storage (BSON)
- MONGO: creating databases like `client["some_db"]` is prone to typos;
  recommend using a constant string in the script `DB = "some_db"; client[DB]`
- MONGO: default port 27017; optional u/n & p/w
- MONGO: use `*.insert_one()` or `*.insert_all()` rather than `*.insert`
- MONGO: default dbpath is `/data/db`; but I'm using `/mongo_data/db`
- MONGO: start mongo server using `mongod --dbpath /mongo_data/db`
- MONGO: `*.insert_all(collection)` modifies `collection` by adding an `_id`
  field to each dictionary

# Chapter 4

- JS: `npx` to run a locally-installed module
- JS: `npm` to install modules
- JS: `prettier` for destructive styling
- JS: `eslint` for code checking / linting
- JS: details on running eslint in vim: https://daqo.medium.com/vim-and-eslint-16fa08cc580f
- JS: add `globals: {_: "readonly"}` to .eslintrc so that lodash `_` character
  doesn't throw lints
