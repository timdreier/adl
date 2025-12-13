# 📚 ADL

Download ebooks from Adobe `.acsm` files and transfer them to your ebook reader.

This tool provides basic functions to handle books protected by Adobe ADEPT DRM. On Windows, macOS, and Android, Adobe offers Adobe Digital Editions (ADE) for these tasks. Unfortunately, there's no Linux version of ADE, and Wine hasn't proven reliable.

This command-line tool performs the same tasks and works on Linux, macOS, and iOS (via iSH).

⚠️ **Note:** Unlike some other tools, `adl` will **not** attempt to remove DRM from your books.

## ✨ Features

- 🔐 **Login** with your Adobe ID (or anonymously with restrictions)
- 📱 **Activate** ebook readers that support Adobe ADEPT DRM
- 📥 **Download** EPUB files from `.acsm` files
- 📲 **iOS Support** via iSH - download ebooks directly on your iPhone/iPad and transfer them to your ebook reader

### What it does

If your book is protected by DRM, you'll receive an encrypted EPUB. If your device is activated with the same Adobe ID used to download the book, it will be able to read the file.

### What it will NOT do

- ❌ Remove DRM from your books

## ⚖️ License & Disclaimer

This tool is published under the **GPLv3**.

This tool is suited primarily for my personal use. It has not been extensively tested in other environments. **Use at your own risk.**

## 📦 Installation

### Option 1: Alpine Package (Recommended for iSH on iOS)

For Alpine Linux systems (including iSH on iOS), install the pre-built package:

1. Download the appropriate `.apk` file for your Alpine version from the [📥 Releases page](https://github.com/timdreier/adl/releases)
2. Install it:
   ```sh
   apk add --allow-untrusted adl-<version>-alpine-<alpine-version>.apk
   ```

**Example for Alpine 3.14:**
```sh
wget https://github.com/timdreier/adl/releases/download/0.1.0/adl-0.1.0-alpine-3.14.apk
apk add --allow-untrusted adl-0.1.0-alpine-3.14.apk
```

### Option 2: From Source

Requires **Python 3.6+**

```sh
git clone https://github.com/timdreier/adl.git
cd adl
pip install -r requirements.txt
```

---

## 🚀 Quick Start

### Login to Adobe

```sh
adl login -u your-adobe-id@example.com
```

You'll be prompted for your password. This only needs to be done once to exchange encryption keys.

💡 **Recommendation:** Use an Adobe ID (free to create on Adobe's website) instead of anonymous login. With an Adobe ID, your keys and books are tied to your account, allowing you to recover them from other devices.

### Download an Ebook

```sh
adl get -f book.acsm
```

The EPUB file will be saved in your current directory.

### Transfer to Your E-Reader

Simply copy the downloaded `.epub` file to your e-reader's filesystem.

📱 For Adobe DRM-protected books, make sure your e-reader is activated with the same Adobe ID (see [Device Activation](#-activate-a-device) below).

---

## 📖 Usage

### Login

```sh
adl login -u <adobeID>
```

**Anonymous login** (not recommended):
```sh
adl login
```

⚠️ **Warning:** Anonymous login is risky. If something goes wrong, you may lose access to your books permanently.

You can log in with multiple accounts if needed.

### Download a Book

```sh
adl get -f <file.acsm>
```

The `.acsm` file is usually provided by your library or ebook store. Running this command will download the actual EPUB file.


### Manage Accounts

List all accounts:
```sh
adl account list
```

Switch active account:
```sh
adl account use <account-urn>
```

Delete an account:
```sh
adl account delete <account-urn>
```

### Activate a Device

Mount your e-reader's root filesystem and activate it:

```sh
adl device register <mountpoint>
```

**Force re-authorization** of an already activated device:
```sh
adl device register --force <mountpoint>
```

**What happens:**
- ✅ **Never activated:** Device will be activated with your Adobe ID
- ✅ **Already activated by you:** Nothing changes, but the device is registered in adl's database
- ⚠️ **Activated by another account:** Error shown. Use `--force` to override (⚠️ this makes books from the previous account unreadable)


## 📱 Using on iOS with iSH

[iSH](https://ish.app) is an Alpine Linux shell emulator for iOS/iPadOS. With `adl`, you can download ebooks **directly on your iPhone or iPad**!

### Setup

1. **Install iSH** from the [App Store](https://ish.app)
2. **Install adl** in iSH:
   ```sh
   wget https://github.com/timdreier/adl/releases/download/0.1.0/adl-0.1.0-alpine-3.14.apk
   apk add --allow-untrusted adl-0.1.0-alpine-3.14.apk
   ```


### Downloading Ebooks on iOS

1. **Get your `.acsm` file** from your library or ebook provider
2. **Mount a folder** from the iOS Files app:
   ```sh
   mkdir -p /mnt/downloads
   mount -t ios . /mnt/downloads
   ```
   iSH will show a popup - select the folder containing your `.acsm` file
3. **Login** (first time only):
   ```sh
   adl login -u your-adobe-id@example.com
   ```
4. **Download the book:**
   ```sh
   cd /mnt/downloads
   adl get -f book.acsm
   ```
5. ✅ The `.epub` file is now in your Files app!


### Reading the Downloaded Book

You can:
- 📱 **Open directly** with any EPUB reader app on iOS (if it supports Adobe DRM)
- 📲 **Transfer to an e-reader** via USB or cloud storage

⚠️ **Note:** The book will be DRM-protected. To read on an e-reader, activate it first (see below).

---

### Activating an E-Reader Device (Tolino, Kobo, PocketBook, etc.)

To read DRM-protected books on a dedicated e-reader, activate it with your Adobe ID:

1. **🔌 Connect your e-reader** to your iOS device via USB (using Lightning or USB-C adapter)
2. **📂 Open Files app** - your e-reader should appear as an external device
3. **Mount in iSH:**
   ```sh
   mkdir -p /mnt/reader
   mount -t ios . /mnt/reader
   ```
   Select your e-reader from the popup
4. **Check active account:**
   ```sh
   adl account list
   adl account use <account-urn>  # if needed
   ```
5. **🔐 Activate the device:**
   ```sh
   adl device register /mnt/reader
   ```
   
   To override existing authorization:
   ```sh
   adl device register --force /mnt/reader
   ```

6. ✅ **Done!** Your e-reader is now authorized

## 📜 Credits

Original project by [Adrien Metais](https://github.com/adrienmetais/adl)

This fork adds iOS/iSH support and additional features.