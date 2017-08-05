# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sales Analysis Group By Brand",
    "version": "8.0.1.0.0",
    "category": "Sales Management",
    "website": "https://opensynergy-indonesia.com/",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "auto_install": True,
    "depends": [
        "sale",
        "product_brand",
    ],
    "data": [
        "reports/sale_report_views.xml",
    ],
}
