<?php
$upload_dir = 'uploads/';
$files = array_diff(scandir($upload_dir), array('.', '..'));

echo '<h1>Uploaded Files</h1>';
echo '<ul>';
foreach ($files as $file) {
    $file_path = $upload_dir . $file;
    echo '<li><a href="' . $file_path . '" download>' . $file . '</a></li>';
}
echo '</ul>';
?>
