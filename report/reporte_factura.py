# -*- coding: utf-8 -*-

from odoo import api, models

class ReporteFactura(models.AbstractModel):
    _name = 'report.ticket_kam.reporte_factura'

    @api.model
    def _get_report_values(self, docids, data=None):
        self.model = 'account.invoice'
        docs = self.env[self.model].browse(docids)

        return {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
        }
