# Get a list of all local user accounts
$userList = Get-LocalUser | Where-Object { $_.Name -ne 'Administrator' }

# Loop through the list and delete each user account
foreach ($user in $userList) {
    Remove-LocalUser -Name $user.Name
    Write-Host "User account $($user.Name) deleted."
}
