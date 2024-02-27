# access_control_system
Access Control System for gate pass.

Odoo version: 16
Odoo installation: https://www.odoo.com/documentation/17.0/administration/install/source.html
In order to print employee cards we need wkhtmltopdf package installed in the machine (MacOS, Windows, Linux)
wkhtmltopdf version: wkhtmltopdf 0.12.6.1 (with patched qt)
wkhtmltopdf installation: https://wkhtmltopdf.org/downloads.html

Running Odoo command (from odoo source folder): python3 odoo-bin --addons-path=addons,(path to access_control_system module) -d (databaseName) -i base
after running odoo install Access Control System by searching: access_control_system (remove app filter from searchbar in odoo apps)