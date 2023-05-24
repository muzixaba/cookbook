# Define variables
$baseUsername = "User"
$password = ConvertTo-SecureString "explore@123" -AsPlainText -Force

# Loop to create 10 users
for ($i=1; $i -le 10; $i++) {
    $username = $baseUsername + $i
    $fullname = "User $i"
    New-LocalUser -Name $username -Password $password -FullName $fullname -PasswordNeverExpires:$false -UserMayNotChangePassword:$false
    Write-Host "User $username created with password explore@123"
}
