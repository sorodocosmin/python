## Requirements
<ol>
<li>Create a Python script that does the following:</li>
</ol>
<ul>
<li>Takes a directory path and a file extension as command line arguments (use sys.argv).</li>
<li>Searches for all files with the given extension in the specified directory (use os module).</li>
<li>For each file found, read its contents and print them.</li>
<li>Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.</li>
</ul>
<ol start="2">
<li>
<p>Write a script using the os module that renames all files in a specified directory to have a sequential number prefix. For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or files that can't be renamed.</p>
</li>
<li>
<p>Create a Python script that calculates the total size of all files in a directory provided as a command line argument. The script should:</p>
</li>
</ol>
<ul>
<li>Use the sys module to read the directory path from the command line.</li>
<li>Utilize the os module to iterate through all the files in the given directory and its subdirectories.</li>
<li>Sum up the sizes of all files and display the total size in bytes.</li>
<li>Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.</li>
</ul>
<ol start="4">
<li>Write a Python script that counts the number of files with each extension in a given directory. The script should:</li>
</ol>
<ul>
<li>Accept a directory path as a command line argument (using sys.argv).</li>
<li>Use the os module to list all files in the directory.</li>
<li>Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.</li>
<li>Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.</li>
</ul>
