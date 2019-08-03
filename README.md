# README - CSCI 0111 WEBSITE

## Management & Structure Side

### Overall website structure:
The following is the structure of different folders and what it contains:

 - **assets**
	 - **css**: Containing one file `main.css`, which is the main stylesheet for the website
	 - **js**: Containing the Javascript/jQuery scripts for the website. `reuseable.js` is included in all pages on our course website, and will load the header and footer (hence reuseable). `json_render.js` is to render the html files (that contain the tables converted from json files (lectures, assignments, projects, labs, etc.)) into the html files that are the pages on the website. `staff_member.js` is to load the `staff-list.html` file into the staff page, then add jquery effects on mouse over and mouse out.
	 - **json**: This contains all the data for the website. This contains:
		 - `assignments.json`: This contains the assignments data, designed as a list of different items of data, each holding: week, assignment (name and link), type (drill/short or weekly/long), out date, in date, a list of support docs, each of the type (name and link), and a solutions item that also of the type (name and link).
		 - `lectures.json`: It is designed similarly as a list of different items of data, each holding data items for Date, Topic, Summary (list, name and link), Readings (list, name and link), and Lecture Capture. All of the names of the lectures for the course has been filled in.
		 - `staff.json`: Containing data of each staff in our course.
		 - `projects.json`: Design is similar to `lectures` and `assignments`, and the fields are: Project, Out, In, Support Docs, and Gear Ups
		 - `labs.json`: Design is similar to everything else, and the fields are: Lab, Week, and Additional Materials.
	 - **img**: Containing the images on the website, including the background pictures, staff pictures (the real pics, of the name format: `...-pic.jpg`) and character pictures of the name format `...-char.jpg`.
	 - **parsers**: Containing the python scripts that (1) `jsonhtml.py` will update all the data (assignments, lectures, labs, projects, etc.) when run, (2) `staff.py` will render the staff website when run, and (3) `toc.py` contains functions that helped with creating a table of content given html text file.
 - **pages**: This contains many files and a folder.
	 - The many files: These are the main pages of our website.
	 - `partials`: This contains the smaller portions of the main pages, that most likely will be changed by the combination of the change in json files (in the json folder earlier) and the running of the `jsonhtml.py` script.
	 - `docs`: This contains the different documents that people will upload onto the website - just put them in the folders of the page that that document will go to (assignments, lectures, labs, etc.) and add the path directory to the json file and then run the script.

### What & Where questions when uploading files:

#### 1. How to update assignments, lectures, labs, projects, etc.

Follow the following steps:

 1. **Upload**:  Upload the `.html` files that you want onto their designated folder(s) in `pages/docs/...`. For example, upload `homework1.html` onto `pages/docs/assignments/homework1.html`
 2. **Update the json file**: Make changes to any of the json files that you wish. Any field with two ids (name and link) will be a file, so just name that file and insert the path to that file.
 3. **Run the `jsonhtml.py` script**: This script (`python jsonhtml.py`) will convert the data in the json files to their designated pages. This script will update all the data on website (aka update all assignments, lectures, projects, labs) so be careful when you execute this script. You can comment out the functions called on the script in order to only do specific things. This file is still subject to change, since I'm still working on how to change staff's data dynamically.

## User Experience Side
