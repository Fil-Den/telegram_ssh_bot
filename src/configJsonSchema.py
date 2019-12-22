'''store json schema for config'''


CONFIG_JSON_SCHEMA = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "telegram",
    "allow_all_commands",
    "commands"
  ],
  "properties": {
    "telegram": {
      "$id": "#/properties/telegram",
      "type": "object",
      "title": "The Telegram Schema",
      "required": [
        "api_token",
        "proxy_url",
        "proxy_username",
        "proxy_password",
        "allowed_users"
      ],
      "properties": {
        "api_token": {
          "$id": "#/properties/telegram/properties/api_token",
          "type": "string",
          "title": "The Api_token Schema",
          "default": "",
          "pattern": "^(.*)$"
        },
        "proxy_url": {
          "$id": "#/properties/telegram/properties/proxy_url",
          "type": "string",
          "title": "The Proxy_url Schema",
          "default": "",
          "pattern": "^(.*)$"
        },
        "proxy_username": {
          "$id": "#/properties/telegram/properties/proxy_username",
          "type": "string",
          "title": "The Proxy_username Schema",
          "default": "",
          "pattern": "^(.*)$"
        },
        "proxy_password": {
          "$id": "#/properties/telegram/properties/proxy_password",
          "type": "string",
          "title": "The Proxy_password Schema",
          "default": "",
          "pattern": "^(.*)$"
        },
        "allowed_users": {
          "$id": "#/properties/telegram/properties/allowed_users",
          "type": "array",
          "title": "The Allowed_users Schema",
          "items": {
            "$id": "#/properties/telegram/properties/allowed_users/items",
            "type": "integer",
            "title": "The Items Schema",
            "default": 0
          }
        }
      }
    },
    "allow_all_commands": {
      "$id": "#/properties/allow_all_commands",
      "type": "boolean",
      "title": "The Allow_all_commands Schema",
      "default": False
    },
    "commands": {
      "$id": "#/properties/commands",
      "type": "array",
      "title": "The Commands Schema",
      "items": {
        "$id": "#/properties/commands/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "command_name",
          "command"
        ],
        "properties": {
          "command_name": {
            "$id": "#/properties/commands/items/properties/command_name",
            "type": "string",
            "title": "The Command_name Schema",
            "default": "",
            "pattern": "^(.*)$"
          },
          "command": {
            "$id": "#/properties/commands/items/properties/command",
            "type": "string",
            "title": "The Command Schema",
            "default": "",
            "pattern": "^(.*)$"
          }
        }
      }
    }
  }
}
