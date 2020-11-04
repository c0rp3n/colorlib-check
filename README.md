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
# for more info use ./color_gen.py -h
colorlib_check -re -c "./example_conf.yaml" "./colorlib_example.sp"
```

#### Example GitHub workflow for SourcePawn
__Note:__ _This must executed before the plugins will be compiled._
```yaml
- name: Set up Python
  uses: actions/setup-python@v2
  with:
    python-version: '3.x'

- name: ColorLib Check - Install Dependencies
  run: python3 -m pip install --upgrade pip setuptools wheel

- name: ColorLib Check - Download
  run: |
    cd tools
    git clone https://github.com/c0rp3n/colorlib-check.git

- name: ColorLib Check - Install
  run: |
    cd tools/colorlib-check
    pip install -r ./requirements.txt
    python3 ./setup.py install

- name: ColorLib Check - Check Files
  run: |
    for file in $(find . -name '*.sp' -name '*.phrases.txt')
    do
      echo -e "\Checking $file..."
      colorlib_check -re -c "./example_conf.yaml" $file
    done
```

## Download
 - https://github.com/c0rp3n/colorlib-check
