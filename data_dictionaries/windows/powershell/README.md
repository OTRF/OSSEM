# PowerShell Event Logs

## Data Dictionaries

| EventID | Name | Description |
|--------|---------|---------|
| 400 | [Engine Lifecycle - Start](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/powershell/events/event-400.md) | PowerShell engine state is changed from None to Available |
| 403 | [Engine Lifecycle - Stopped](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/powershell/events/event-403.md) | PowerShell engine state is changed from Available to Stopped |
| 600 | [Provider Lifecycle](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/powershell/events/event-600.md) | Logs the start and stop of PowerShell providers |
| 4103 | [Module Logging](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/powershell/events/event-4103.md) | Detailed logging of all PowerShell command input and output |
| 4104 | [Script Block Logging](https://github.com/Cyb3rWard0g/OSSEM/blob/master/data_dictionaries/windows/powershell/events/event-4104.md) | It records blocks of code as they are executed by the PowerShell engine |

## Resources

* [Greater Visibility Through PowerShell Logging](https://www.fireeye.com/blog/threat-research/2016/02/greater_visibilityt.html)
* [Investigating PowerShell Attacks - Slides](https://www.defcon.org/images/defcon-22/dc-22-presentations/Kazanciyan-Hastings/DEFCON-22-Ryan-Kazanciyan-Matt-Hastings-Investigating-Powershell-Attacks.pdf)
* [Investigation PowerShell Attacks - Paper](https://www.blackhat.com/docs/us-14/materials/us-14-Kazanciyan-Investigating-Powershell-Attacks-WP.pdf)