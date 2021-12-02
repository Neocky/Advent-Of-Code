<#
Day 1 Part 2

#>

$input_file = Get-Content ".\d1-01_input.txt"


[System.Collections.ArrayList]$numbers = @() 
[System.Collections.ArrayList]$sumNumbers = @()
$increased, $decreased = 0

foreach ($measurement in $input_file) {
    [void]$numbers.Add($measurement)

    if ($numbers.count -lt 3) {
        continue
    }

    [int32]$newSum = [int32]$numbers[0] + [int32]$numbers[1] + [int32]$numbers[2]
    [void]$sumNumbers.Add($newSum)
    [void]$numbers.RemoveAt(0)

    if ($sumNumbers.count -lt 2) {
        Write-Output "$measurement (No previous measurement)"
        continue
    }

    if ([int32]$sumNumbers[1] -gt [int32]$sumNumbers[0]) {
        $increased = $increased + 1
        [string]$outputString = [string]$sumNumbers[1] + " (increased)"
        Write-Output $outputString
    }
    elseif ([int32]$sumNumbers[1] -lt [int32]$sumNumbers[0]) {
        $decreased = $decreased + 1
        [string]$outputString = [string]$sumNumbers[1] + " (decreased)"
        Write-Output $outputString
    } else {
        [string]$outputString = [string]$sumNumbers[1] + " (no change)"
        Write-Output $outputString
    }

    $sumNumbers.RemoveAt(0)
}

Write-Output "Increased: $increased"
Write-Output "Decreased: $decreased"
