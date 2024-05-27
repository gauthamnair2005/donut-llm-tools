# Donut LLM Tools
Donut LLM Tools is a suite of two programs that helps you create dataset from wikipedia data and your own LLM with the created or already existing dataset.

*Latest Version 24.05.27*

## How to install, import and use DonutLLM?
### Installation
* Before installing Donut LLM Tools, make sure you have Python `3.9` or later till Python `3.11`. *Note : Python `3.12` is not supported by PyTorch, hence Donut LLM Tools will also have troubles running.* 
* The dependencies for installing Donut LLM Tools are:
    1. CreateLLM (`pip install CreateLLM`)
    2. torch (Required by CreateLLM)
    3. torchvision (Required by CreateLLM, PyTorch)
    4. torchaudio (Required by CreateLLM, PyTorch)
    5. Wikipedia
    
    *Note : You need to check [PyTorch](https://pytorch.org) website to find more about installation on devices with only CPU or with GPU. Donut LLM Tools support CPU, however it is very slow to train a model in CPU.*
* After ensuring the installation of the above mentioned dependencies, do `pip install donut-llm-tools`.
* You have now installed Donut LLM Tools in your device.

### Importing and Using
```python
from donutllmtools import Tools

Tools.DatasetCreator() # For creating wikipedia based datasets.

Tools.LLMCreator() # For creating/loading AI model from the above created dataset or a custom dataset.
```

The above code snippet is used to create a dataset and also train/load an AI model

```python
from donutllmtools import HelpAndInfo

HelpAndInfo.help() # To view help.

HelpAndInfo.about() # To view details of the program.

HelpAndInfo.create_llm() # Also create LLM from HelpAndInfo class.

HelpAndInfo.create_dataset() # ALso create dataset from HelpAndInfo class.

HelpAndInfo.main() # To get a menu based interface for dataset creation or model load/creation.
```
