<h1 align="center">
    ColorLib - Checker
</h1>
<p align="center">
    <strong>A tool which checks Plugins and Translation files for bad color tags.</strong>
</p>

ColorLib - Check looks for bad color tags that do not match any of the colors
defined from the input config, the config format is the same as that for Color
Gen.

## Usage
First you need to install `colorlib_check` with `py ./setup.py install`.

To change the colors to check you first need to create a new or edit your config
file.

There is an example config file provided that it is recommended you copy from it
can be seen [here](example_conf.yaml).

Then you can rerun `colorlib_check` on a file to find any bad color tags.

#### Example
```bash
# for more info use ./colorlib_check.py -h
colorlib_check -re -c "./example_conf.yaml" "./colorlib_example.sp"
```

#### GitHub workflow for Checking Plugins and Translations
__Note:__ _This must executed before the plugins will be compiled._
```yaml
name: Check files with ColorLib - Check

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false

    steps:
      - uses: actions/checkout@v2

      - name: Set environment variables
        run: |
          echo "SOURCEMOD_PATH=$GITHUB_WORKSPACE/addons/sourcemod" >> $GITHUB_ENV

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: python3 -m pip install --upgrade pip setuptools wheel

      - name: Clone
        uses: actions/checkout@v2
        with:
          repository: 'c0rp3n/colorlib-check'
          ref: 'master'
          path: 'deps/colorlib-check'

      - name: Install
        run: |
          pip install -r ./requirements.txt
          python3 ./setup.py install
          echo "CHECK_PATH=$GITHUB_WORKSPACE/deps/colorlib-check" >> $GITHUB_ENV
        working-directory: ./deps/colorlib-check/

      - name: Check Files
        run: |
          for file in $(find . -name '*.sp' -o -name '*.phrases.txt')
          do
            echo -e "Checking $file..."
            colorlib_check -re -c "$CHECK_PATH/example_conf.yaml" $file
          done
        working-directory: ${{ env.SOURCEMOD_PATH }}/

```

## Download
 - https://github.com/c0rp3n/colorlib-check
