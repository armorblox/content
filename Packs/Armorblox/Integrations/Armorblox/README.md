Armorblox is an API-based platform that stops targeted email attacks,
  protects sensitive data, and automates incident response.
This integration was integrated and tested with version 1.0 of Armorblox

## Configure Armorblox on Cortex XSOAR

1. Navigate to **Settings** > **Integrations** > **Servers & Services**.
2. Search for Armorblox.
3. Click **Add instance** to create and configure a new integration instance.
4. Select **Fetches incidents** to pull incidents from Armorblox to Cortex
5. Select Classifier as Armorblox-Classifier
6. Select Mapper as Armorblox-Mapper

    | **Parameter** | **Required** |
    | --- | --- |
    | Armorblox tenant name | True |
    | Incident type | False |
    | Trust any certificate (not secure) | False |
    | Use system proxy settings | False |
    | API Key | True |
    | Incidents Fetch Interval | False |
    | Fetch incidents | False |
    | First fetch timestamp (&lt;number&gt; &lt;time unit&gt;, e.g., 12 hours, 7 days) | False |

7. Click **Test** to validate the URLs, token, and connection.
8. Save and Exit to enable the instance.