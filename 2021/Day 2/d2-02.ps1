<#
Day 2 Part 2

#>

$input_file = Get-Content ".\d2-01_input.txt"

$aim, $horizontal_position, $depth = 0
foreach ($move_cmd in $input_file) {
    $move_cmd -match "\d"
    [int32]$number = $Matches[0]
    if ($move_cmd.Contains("forward")) {
        $horizontal_position += $number
        $depth += ($number * $aim)
    } elseif ($move_cmd.Contains("down")) {
        $aim += $number
    } elseif ($move_cmd.Contains("up")) {
        $aim -= $number
    }

    Write-Host $number
    Write-Host $move_cmd
}

$position_sum = $horizontal_position * $depth 
Write-Host "Horizontal Position: $horizontal_position"
Write-Host "Depth: $depth"
Write-Host "Sum: $position_sum"
