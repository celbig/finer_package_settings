# Finer Package Settings
This sublime text 3 package allow for a finer (per project and per syntax) package configuration.

## Installation

### From package control

1. Install package control
2. Install Finer Package Settings:
   - <kbd>⌘/ctrl</kbd><kbd>shift</kbd><kbd>p</kbd> Package Control: Install Package
   - Type Finer Package Settings

### Manually 

1. Open the Sublime Text package folder (Preferences -> Browse Packages...)
2. Clone the package source repo in this folder


## Usage 
This package uses the `packagesSettings` parameter key to store a list of other packages configurations with the following syntax:

```json
{
    "packagesSettings": [
        {
            "settings_file": "",
            "settings": {}
        }
    ]
}
```

Where:
- the `settings_file` key holds the base name (without extension) of the parameter file to override. For a package this is the name of the `.sublime-settings` file of the package, usually it is the name of the package. 
- the `settings` key hold a json object of the configuration to override. Pre-existing settings not specified will be conserved.


The settings are read using the underlying sublimText api, you can refer to the (Offical Sublime Text Documentation)[https://www.sublimetext.com/docs/3/settings.html] to know which files are consulted and in which order.

## Details

The configuration overriding is deactivated for `.sublime-settings` files so it remains possible to edit them.




## Licence

 <p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/celbig/finer_package_settings">finer package settings</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/celbig">celbig</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p> 
