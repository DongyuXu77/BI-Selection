# /usr/bin

# fileName=$( git ls-files --other --exclude-standard ).log
# touch "$fileName"
git add $(git ls-files -o --exclude-standard)
git diff --quiet; noChanges=$?
if [ $noChanges -eq 1 ]; then
    git diff test.docx >>./diff.log
    echo -e "\n\n\n">>./diff.log
    git add test.docx
fi
