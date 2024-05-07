#!/bin/bash
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

int_test_base_folder="dagify/test/integration"
test_data_folder="test_data"
test_references_folder="test_references"
test_output_folder="test_outputs"

has_failed=0
for test_file in $int_test_base_folder/$test_data_folder/*.xml; do
test_name=`echo $test_file | cut -d "/" -f 5 | cut -d "." -f 1`
python3 dagify.py --source-path=$test_file --output-path=$int_test_base_folder/$test_output_folder/$test_name > /dev/null
diff -b -I '^#' -I '^ #' $int_test_base_folder/$test_output_folder/$test_name $int_test_base_folder/$test_references_folder/$test_name

if [ $? -eq 0 ]; then
    echo "integration test for test file $test_name passed."
else
    echo "integration test for test file $test_name failed."
    has_failed=1
fi
rm -rf $int_test_base_folder/$test_output_folder/*
done

if [ $has_failed -eq 0 ]; then
    echo "SUCCESS: All integration tests have passed!"
else
    echo "Error: One or more integration tests have failed!"
fi
exit $has_failed
