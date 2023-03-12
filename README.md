# pip-installer
A tool to check and install Python packages using pip. Prints installation status and exits on failure.
<h1>how to use this code ? <h1/>
<p>To use this code, you have to change the <strong>packages list</strong> to include the packages that you want to check and install.</p>
  <p>For example, if you want to check and install <strong>scipy</strong> and <strong>sklearn</strong>, you have to change the line:</p> <code>packages = [“numpy”, “pandas”, “matplotlib”]</code> 
  <p>to</p> 
  <code>packages = [“numpy”, “pandas”, “matplotlib”, “scipy”, “sklearn”]</code>
  <p>Then you can run the code as it is, The code will print messages indicating whether each package is <strong>already installed or not</strong>, and try to install any missing packages using <strong>pip</strong>. If any package fails to install, the code will exit with an error message.</p>

