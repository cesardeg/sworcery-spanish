This info plist fix the orientation issue on iOS/iPadOS 16.X

```xml
<key>UISupportedInterfaceOrientations</key>
<array>
    <string>UIInterfaceOrientationPortrait</string>
</array>
<key>UISupportedInterfaceOrientations~ipad</key>
<array>
    <string>UIInterfaceOrientationPortrait</string>
</array>
```

unzip S:SS.ipa

zip -qr S:SS-patched.ipa Payload
