**REC - PKST DESIGN SYSTEM**

# Figma JSON to CSS

This script is designed to streamline the process of **generating structured JSON files from Figma Design System variables**, providing flexibility to convert these structured files into any format needed for web or app projects.

Figma offers the ability to export design variables as JSON files, which include detailed properties used to build components within a design system. This tool processes those JSON exports, restructuring them into new JSON files that can be easily converted into CSS, or any other format required for your project, ensuring consistency across development environments.

&nbsp; 
&nbsp; 

## Key Features

### Figma JSON Export to Flexible JSON Structure (scripts/generate_json)
The script takes the raw JSON files exported from Figma, restructures them, and generates new JSON files with a clean structure that can be further used to create various file formats (e.g., CSS, SCSS, XML, etc.), making it easier to integrate into any web or app project.

### JSON to CSS (scripts/generate_css)
The script takes the restructured **JSON files** generated from the raw Figma exports, which contain various design variables (like colors, typography, spacing, etc.), and automatically generates corresponding CSS files. This ensures that the CSS is based on clean, well-organized data that can be easily maintained and updated.

### Pixel to REM (scripts/px_to_rem)
The tool converts pixel (px) values into rem units in the final output (e.g., CSS), ensuring that the design is scalable, responsive, and accessible, adhering to modern web development best practices and supporting compliance with [accessibility standards](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/) by allowing users to adjust text size based on their preferences.

### Variable Replacement (scripts/update_css_variables)
As part of the conversion process, the tool replaces hardcoded values with corresponding CSS variables, making the stylesheets more maintainable and aligned with design system principles.

### Add Fallbacks (scripts/add_fallbacks)
The function enhances CSS variables by adding fallback values, ensuring that your styles remain consistent even if a variable is not defined or fails to load.

&nbsp; 
&nbsp; 

---

&nbsp; 
&nbsp; 

# Steps to follow
To successfully integrate the generated CSS files into the **REC - Pkst Design System**, follow these steps carefully.

&nbsp; 
&nbsp; 

**Step 1: Open the Figma Files**

## Pkst Design System Libraries

The **REC - Pkst Design System** is organized into several libraries, each serving a specific purpose and scope within the design system. Below are the details of these libraries and their usage:

### [Pkst Foundations](https://www.figma.com/design/GHVHUg8lOVKAP3ItIbF3EK/Pkst---Foundations?node-id=0-1&t=caygYBaxgWq7qUrN-1)
This is the **main library** and serves as the foundation for the entire Pkst Design System. It contains the core design tokens and elements that are used across all products and landing pages.
**Contents:** Colors, Typography, Spacing, Grids, Shadows.

### [Pkst Components](https://www.figma.com/design/vDpfDVUTNQRm1WWEIzQ5tX/Pkst---Components?node-id=0-1&t=dUvkpqjYnw24J93o-1)
This library houses the primary components that can be reused across various Pkst products and landing pages.
**Contents**: Buttons, Input, Forms, Icon, Illusstrations, Modals, etc.

### [Pkst Studio](https://www.figma.com/design/LdjW135ZKrdELkwOl2X2PS/Pkst-Studio?node-id=20-80&t=rXF4kYxEMdorVuXp-1)
This library is **exclusive to the Pkst Studio** product and is not intended for use in other Pkst products or landing pages.

&nbsp; 
&nbsp; 

**Step 2: Export and paste JSON**
## Figma File & JSON 

Once you open the Figma files, find and run the Figma plugin [Variables Exporter for Dev Mode](https://www.figma.com/community/plugin/1306814436222162088/variables-exporter-for-dev-mode). 

Within the plugin, click the **Export Variables** button to generate the JSON code containing your design variables.

Once the JSON is generated, **copy the entire code snippet** provided by the plugin.

### Handling JSON Export from Pkst Foundations
When exporting the JSON from the **Pkst Foundations** library, you will copy code that contains two distinct groups of variables: **Tokens** and **Foundations**. To properly integrate these variables into the **REC - Pkst Design System**, this single JSON file needs to be separated into two separate JSON files, each representing one of these groups:
- Tokens into `fimgma-json/tokens.json`
- Foundations into `figma-json/foundations.json`

### Handling JSON Export from Pkst Components
When exporting the JSON from the **Pkst Foundations** library, you will copy code that contains just one group of variables. You should copy it and paste it inside `figma-json/compontents.json`.

### Handling JSON Export from Pkst Studio
When exporting the JSON from the **Pkst Studio** library, you will copy code that contains two distinct groups of variables: **Template** and **Streaming**. To properly integrate these variables into the **REC - Pkst Design System**, this single JSON file needs to be separated into two separate JSON files, each representing one of these groups:
- Template into `figma-json/studio-template.json`
- Streaming into `figma-json/studio-streaming.json`

&nbsp; 
_**IMPORTANT**: Do not leave any comments inside the JSON files, as this will prevent the script from functioning correctly._

&nbsp; 
&nbsp; 

**Step 3: Run Script & Generate Flexible JSON and CSS**

## Running the Script
Once you have correctly pasted the JSON files into their respective locations, follow these steps to generate the structured JSON files and CSS:

**1. Navigate to the Scripts Folder:**
Open your terminal and navigate to the **scripts folder** within your project directory where the processing script is located.

**2. Execute the Script:**
Run the script by entering the following command in your terminal: `python3 run_all.py`

**3. Review the Output:**
Check the terminal for any errors or issues. If the script runs successfully, it will generate the corresponding JSON files and CSS files in their respective folders.

This step finalizes the process, converting your Figma design tokens into usable CSS.

&nbsp; 
&nbsp; 

## Verifying JSON File Generation
After running the script, ensure the following folder structure and files are generated:

**JSON Files**
Check the `json/variables` and `json/studio` directories for the newly structured JSON files.

```bash
└── json
    └─ variables
    │    ├── tokens
    │    ├── foundations
    │    └── components
    └─ studio
        └─ template
        └─ streaming
```

**CSS Files**
```bash
└── css
    └─ variables
    │    ├── tokens
    │    ├── foundations
    │    └── components
    └─ studio
        └─ variables
            ├── template
            └── streaming
```

#### Tokens Variables:
Check the directory: `css/variables/tokens`.
This folder should contain the CSS files generated from the **variables/tokens** folder.

#### Foundations Variables:
Check the directory: `css/variables/foundations`.
This folder should contain the CSS files generated from the **variables/foundations** folder.

#### Component Variables:
Check the directory: `css/variables/components`.
This folder should contain the CSS files generated from the **variables/components** folder.

#### Studio Template Variables:
Check the directory: `css/studio/variables/template`.
This folder should contain the CSS files generated from the **studio/template** folder.

#### Studio Streaming Variables:
Check the directory: `css/studio/variables/streaming`.
This folder should contain the CSS files generated from the **studio/streaming** folder.

_**IMPORTANT:** If the CSS files have been successfully generated, please commit your changes to the repository._

&nbsp; 
&nbsp; 


**Step 4: Integrate with REC - Pkst Design System**

## Update CSS files on Design System

Follow these steps to update the CSS files in the **REC - Pkst Design System:**

&nbsp; 
**1. Access the REC - Pkst Design System**: Navigate to the [REC - Pkst Design System](https://github.com/Peekast/pkst-ds) repository.

&nbsp; 
**2. Locate the DIST Folder**: In the `pkst-ds`, locate the following folders. (As you can see, the structure of the folders are similar from `pkst-ds-json`)

```bash
└── css
    └─ variables
    │    ├── generals
    │    └── components
    └─ studio
        └─ variables
            ├── template
            └── streaming
```


&nbsp; 
**3. Copy and Paste CSS Files**: 
Carefully copy the CSS files from `pkst-ds-json` and paste them into the corresponding directories in the `pkst-ds` project.

_**IMPORTANT**: Do not replace the entire folders. Instead, replace only the individual CSS files within each folder to ensure that manually created files are not overwritten._

&nbsp; 
**4. Verify the Integration**: 
After pasting the files, review the folder contents to ensure all necessary CSS files are correctly placed without affecting any existing manual files.

&nbsp; 

---

&nbsp; 

If you have any question, please contact to [macarena@peekast.com](mailto:macarena@peekast.com).

