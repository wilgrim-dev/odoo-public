# Task Scheduling

The module adds task scheduling features in Odoo 15.

## Installation

Download ziped file and extra in Odoo 15 addons folder.

Restart Odoo service with;
```bash
service odoo-service restart
```

Navigate to Odoo Apps, while debug mode is active update app list.

Search for ```task_scheduling``` module then install it.

## Usage

Navigate to your main menu, click on ```Task Scheduling``` to navigate to app.

Click on ```Create``` action to create a new record.

## Rest API Usage

To create and update task status using Rest API ensure module is installed and you have a running instance.

1 ```https://{IP}:{PORT}/api/v1/task_create```
An endpoint to create a new task and assign resposible user.
Note: Resposible user must exist to use user_id.

Test using curl;
```bash
curl -d '{"user_id": 6, "name": "Curl Test", "description": "API Test", "duration": 12}' -H 'Content-Type: application/json' http://{IP}:{PORT}/api/v1/task_create

```

2 ```https://{IP}:{PORT}/api/v1/task_start```
An endpoint to update task status to ```In Progress``` state

Test using curl;
```bash
curl -d '{"user_id": 6, "name": "Curl Test"}' -H 'Content-Type: application/json' http://{IP}:{PORT}/api/v1/task_start
```

3 ```https://{IP}:{PORT}/api/v1/task_done```
An endpoint to update task status to ```Done``` state

Test using curl;
```bash
curl -d '{"user_id": 6, "name": "Curl Test"}' -H 'Content-Type: application/json' http://{IP}:{PORT}/api/v1/task_done
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[LGPL-3](https://www.gnu.org/licenses/lgpl+gpl-3.0.txt)
