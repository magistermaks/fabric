# <u>Installing</u>

Now you've worked out the version of Java you need, you'll need to install that version from your favourite provider.

## <u>Providers</u>
There are multiple providers you can get Java from, each of these are different, some free-licensed and some non-free. 

### <u>AdoptOpenJDK</u>

AdoptOpenJDK is probably the easiest, free-licensed Java provider. Installing is slightly different on each platform, find the appropriate instructions for your platform below. For macOS/Windows you can get the .msi and .pkg files from [the official website](https://adoptopenjdk.net)

<u>Windows</u>

Download the correct .msi file for whether your PC is 32-bit (x86) is 64-bit (x64). Open the .msi file, and accept the license. Keep the default path. Make sure IcedTea-Web and .jnlp file association are disabled if they appear. Keep .jar association and update JAVA_HOME enabled. Hit Install and wait for the install to complete.

<u> macOS </u>
Download the correct .pkg file for whether your PC is 32-bit (x86) is 64-bit (x64). Open the .pkg file, accept the license, keep the default path and hit install.

<u> Debian/Ubuntu </u>

You need the codename of your Debian or Ubuntu version. It is usually recorded in /etc/os-release and can be extracted on Debian by running `cat /etc/os-release | grep VERSION_CODENAME | cut -d = -f 2 ` and on Ubuntu by running `cat /etc/os-release | grep UBUNTU_CODENAME | cut -d = -f 2. `

Ensure the necessary packages are present: `sudo apt install -y wget apt-transport-https gnupg`

Download the AdoptOpenJDK GPG key: `wget https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public`

Make the key accessible by apt: 
`gpg --no-default-keyring --keyring ./adoptopenjdk-keyring.gpg --import public`
and:
`gpg --no-default-keyring --keyring ./adoptopenjdk-keyring.gpg --export --output adoptopenjdk-archive-keyring.gpg`

Clean Up:
`rm adoptopenjdk-keyring.gpg`

Save keyring in root directory:
`sudo mv adoptopenjdk-archive-keyring.gpg /usr/share/keyrings`

Configure AdoptOpenJDK's apt repository by replacing the values necessary: `echo "deb [signed-by=/usr/share/keyrings/adoptopenjdk-archive-keyring.gpg] https://adoptopenjdk.jfrog.io/adoptopenjdk/deb <codename> main" | sudo tee /etc/apt/sources.list.d/adoptopenjdk.list`

Refresh the package indexes: `sudo apt update`

Install Java: `sudo apt install adoptopenjdk-<java version>-hotspot`

### <u>Oracle</u>
Oracle is a provider which provides **non-free** Java. If you really choose to install Oracle Java, you're on your own.

Now move on to [picking an IDE](./ide.md)