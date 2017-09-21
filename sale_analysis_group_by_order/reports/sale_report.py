# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class SaleReport(models.Model):
    _inherit = "sale.report"

    order_id = fields.Many2one(
        string="# Order",
        comodel_name="sale.order",
    )

    def _select(self):
        str_select = super(SaleReport, self)._select()
        str_select += """
            ,
            l.order_id AS order_id
            """
        return str_select
