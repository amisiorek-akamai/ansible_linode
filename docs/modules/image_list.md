# image_list

List and filter on Linode images.


- [Examples](#examples)
- [Parameters](#parameters)
- [Return Values](#return-values)

## Examples

```yaml
- name: List all of the events for the current Linode Account
  linode.cloud.event_list: {}
```

```yaml
- name: List the latest 5 events for the current Linode Account
  linode.cloud.event_list:
    count: 5
    order_by: desc
    order: created
```

```yaml
- name: List all Linode Instance creation events for the current Linode Account
  linode.cloud.event_list:
    filter:
      - name: action
        values: linode_create
```










## Parameters

| Field     | Type | Required | Description                                                                  |
|-----------|------|----------|------------------------------------------------------------------------------|
| `order` | `str` | Optional | The order to list events in.  (Choices:  `desc`  `asc` Default: `asc`) |
| `order_by` | `str` | Optional | The attribute to order events by.   |
| [`filters` (sub-options)](#filters) | `list` | Optional | A list of filters to apply to the resulting events.   |
| `count` | `int` | Optional | The number of results to return. If undefined, all results will be returned.   |





### filters

| Field     | Type | Required | Description                                                                  |
|-----------|------|----------|------------------------------------------------------------------------------|
| `name` | `str` | **Required** | The name of the field to filter on. Valid filterable attributes can be found here: https://www.linode.com/docs/api/images/#images-list__responses   |
| `values` | `list` | **Required** | A list of values to allow for this field. Fields will pass this filter if at least one of these values matches.   |






## Return Values

- `images` - The returned images.

    - Sample Response:
        ```json
        [
           {
              "action":"ticket_create",
              "created":"2018-01-01T00:01:01",
              "duration":300.56,
              "entity":{
                 "id":11111,
                 "label":"Problem booting my Linode",
                 "type":"ticket",
                 "url":"/v4/support/tickets/11111"
              },
              "id":123,
              "message":"None",
              "percent_complete":null,
              "rate":null,
              "read":true,
              "secondary_entity":{
                 "id":"linode/debian9",
                 "label":"linode1234",
                 "type":"linode",
                 "url":"/v4/linode/instances/1234"
              },
              "seen":true,
              "status":null,
              "time_remaining":null,
              "username":"exampleUser"
           }
        ]
        ```
    - See the [Linode API response documentation](https://www.linode.com/docs/api/images/#images-list__response-samples) for a list of returned fields


