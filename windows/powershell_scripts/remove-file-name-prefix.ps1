# $folderPath = "C:\Users\UserName\Downloads" # change this to your specific folder
$prefixToRemove = "y2mate.com - "

Get-ChildItem -Path $folderPath -Include *.mp3, *.mp4 -Recurse | ForEach-Object {
    $newName = $_.Name
    if ($newName.StartsWith($prefixToRemove)) {
        $newName = $newName.Substring($prefixToRemove.Length)
        Rename-Item -Path $_.FullName -NewName $newName
    }
}
