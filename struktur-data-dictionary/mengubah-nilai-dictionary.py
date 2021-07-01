skill = {
    "utama": "python",
    "lainnya": ["java", "html", "php"]
}

# mencetak isi utama
print(skill["utama"])

# mwngubah isi utama
skill["utama"] = "rust"

# mencatak isi skill utama
print(skill["utama"])

# mengahpus dictionary
del skill["utama"]
print(skill)