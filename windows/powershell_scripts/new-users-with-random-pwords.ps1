# Define variables
$baseUsername = "User"
$userList = @()

# Function to generate a random word
function Get-RandomWord {
    $wc = Invoke-WebRequest -Uri "https://www.randomwordgenerator.org/random-word-generator.php" -UseBasicParsing
    $word = ($wc.AllElements | Where {$_.tagName -eq "strong"})[0].InnerText
    $word
}

# Loop to create 100 users
for ($i=1; $i -le 100; $i++) {
    $username = $baseUsername + $i
    $fullname = "User $i"
    $passwordPrefix = Get-RandomWord
    $passwordSuffix = Get-Random -Minimum 100 -Maximum 999
    $password = $passwordPrefix + "@" + $passwordSuffix
    $securePassword = ConvertTo-SecureString -String $password -AsPlainText -Force
    New-LocalUser -Name $username -FullName $fullname -Password $securePassword -PasswordNeverExpires:$false -UserMayNotChangePassword:$false
    Write-Host "User $username created with password $password"
    $userList += [PSCustomObject] @{
        Username = $username
        Password = $password
    }
}

# Save usernames and passwords to a CSV file
$userList | Export-Csv -Path "C:\UserList.csv" -NoTypeInformation

# Display a final message when the script completes
Write-Host "All local user accounts have been created, and the usernames and passwords have been saved to C:\UserList.csv."
