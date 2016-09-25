import common
import edify_generator

def InstallGapps(info):
  gapps_zip = info.input_zip.read("open_gapps.zip")
  common.ZipWriteStr(info.output_zip, "gapps/open_gapps.zip", gapps_zip)

def FlashGapps(info):
  info.script.AppendExtra("package_extract_dir(\"gapps\", \"/tmp/gapps\");")
  info.script.AppendExtra("run_program(\"/sbin/busybox\", \"unzip\", \"/tmp/gapps/open_gapps.zip\", \"META-INF/com/google/android/*\", \"-d\", \"/tmp/gapps\");")
  info.script.AppendExtra("run_program(\"/sbin/busybox\", \"sh\", \"/tmp/gapps/META-INF/com/google/android/update-binary\", \"dummy\", \"1\", \"/tmp/gapps/open_gapps.zip\");")

def FullOTA_InstallPostEnd(info):
  InstallGapps(info)
  FlashGapps(info)
