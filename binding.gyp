#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

{
  'conditions': [
    ['OS=="win"', {
      'variables': {
       'pulsar_cpp_dir%': '<!(echo %PULSAR_CPP_DIR%)',
      },
    }]
  ],
  "targets": [
    {
      "target_name": "Pulsar",
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
      ],
      "defines": ["NAPI_VERSION=4", "NAPI_DISABLE_CPP_EXCEPTIONS=1"],
      "sources": [
        "src/addon.cc",
        "src/Message.cc",
        "src/MessageId.cc",
        "src/Authentication.cc",
        "src/Client.cc",
        "src/Producer.cc",
        "src/ProducerConfig.cc",
        "src/Consumer.cc",
        "src/ConsumerConfig.cc",
        "src/Reader.cc",
        "src/ReaderConfig.cc",
      ],
      'conditions': [
        ['OS=="win"', {
          "include_dirs": [
            "<(pulsar_cpp_dir)\include",
          ],
          "libraries": [
            "-l<(pulsar_cpp_dir)\\build\lib\Release\pulsar.lib"
          ],
          "dependencies": [
            "<!(node -p \"require('node-addon-api').gyp\")"
          ],
          "copies": [
            {
              "destination": "<(PRODUCT_DIR)",
              "files": [
                "<(pulsar_cpp_dir)\\build\lib\Release\pulsar.dll",
                "<(pulsar_cpp_dir)\\vcpkg_installed\\x64-windows\\bin\\*.dll",
              ]
            }
          ]
        }, {  # 'OS!="win"'
          "libraries": [
            "-lpulsar",
          ],
          "dependencies": [
            "<!@(node -p \"require('node-addon-api').gyp\")"
          ],
        }]
      ]
    }
  ]
}
