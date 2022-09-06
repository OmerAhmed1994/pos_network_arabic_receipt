# -*- coding: utf-8 -*-
{
    'name'    : "POS Network Printer Arabic Receipt",
    'author'  : 'Omer Ahmed',
    'category': 'POS',
    'summary' : """ This module fix arabic receipt issue with network printer""",
    'license' : 'OPL-1',
    'website' : 'http://github.com/omerahmed1994',
    'description': """ This module fix arabic receipt issue with network printer""",
    'version' : '14.0.1.0.0',
    'depends' : ['point_of_sale'],
    'data'    : [
    ],
    "assets": {
        "point_of_sale.assets": [
            "/pos_network_arabic_receipt/static/src/js/html2canvas.js",
        ],
    },
    'images': ['static/description/banner.jpg'],
    'installable'  : True,
}
